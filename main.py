from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
FMCSA_API_KEY = os.getenv("FMCSA_API_KEY")

print("🔑 FMCSA_API_KEY:", FMCSA_API_KEY)

app = FastAPI()

class Carrier(BaseModel):
    mc_number: str

@app.get("/")
def root():
    return {"message": "Welcome to the HappyRobot API!"}

@app.get("/verify_carrier")
def verify_carrier(mc_number: str):
    url = f"https://mobile.fmcsa.dot.gov/qc/services/carriers/docket-number/{mc_number}?webKey={FMCSA_API_KEY}"
    response = requests.get(url)

    print("FMCSA API status:", response.status_code)
    print("Response:", response.text[:300])

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="FMCSA API error")

    try:
        data = response.json()
        content = data.get("content")

        if not content or not isinstance(content, list):
            raise HTTPException(status_code=404, detail="Carrier not found")

        carrier_data = content[0].get("carrier", {})

        return {
            "carrier_name": carrier_data.get("legalName", "Unknown"),
            "status": "active" if carrier_data.get("allowedToOperate") == "Y" else "inactive",
            "mc_number": mc_number
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error parsing FMCSA response")

@app.get("/loads/{reference_number}")
def get_load_by_reference(reference_number: str):
    try:
        with open("loads.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["reference_number"].strip().lower() == reference_number.strip().lower():
                    return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    raise HTTPException(status_code=404, detail="Load not found")

class BookingConfirmation(BaseModel):
    carrier_name: str
    mc_number: str
    reference_number: str
    commodity: str
    origin: str
    destination: str
    pickup_time: str
    delivery_time: str
    special_requirements: str
    agent_name: str
    caller_sentiment: str

@app.post("/confirm_booking")
async def confirm_booking(data: BookingConfirmation):
    return data.model_dump()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main2:app", host="127.0.0.1", port=10000, reload=True)