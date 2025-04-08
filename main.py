from fastapi import FastAPI
from pydantic import BaseModel
import csv
from fastapi import FastAPI, HTTPException
import requests




app = FastAPI()

# Define a simple schema for carrier input
class Carrier(BaseModel):
    mc_number: str



@app.get("/")
def root():
    return {"message": "Welcome to the HappyRobot API!"}


FMCSA_API_KEY = "cdc33e44d693a3a58451898d4ec9df862c65b954"
# FMCSA_API_KEY = "4745a64a6506b2dda4b9b79f5aed274e936f4d70"
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
    


    except Exception as e:
        # Fallback
        if mc_number == "123456":
            return {
                "carrier_name": "Simulated Carrier Inc.",
                "status": "active",
                "mc_number": mc_number
            }
        raise HTTPException(status_code=500, detail="FMCSA API error or carrier not found")
    


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


confirmed_bookings = []
class BookingConfirmation(BaseModel):
    carrier_name: str
    mc_number: str
    reference_number: str

@app.post("/confirm_booking")
async def confirm_booking(data: BookingConfirmation):
    confirmed_bookings.append(data.model_dump()) 
    return {
        "carrier": data.carrier_name,
        "mc_number": data.mc_number,
        "reference_number": data.reference_number
    }

@app.get("/confirmed_bookings")
def get_confirmed_bookings():
    return confirmed_bookings


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)