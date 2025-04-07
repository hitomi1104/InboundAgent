from fastapi import FastAPI
from pydantic import BaseModel
import csv
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define a simple schema for carrier input
class Carrier(BaseModel):
    mc_number: str



@app.get("/")
def root():
    return {"message": "Welcome to the HappyRobot API!"}


@app.get("/verify_carrier")
def verify_carrier(mc_number: str):
    # Simulate logic — later this can be an API call to FMCSA
    if mc_number == "123456":
        return {
            "carrier_name": "carrier_name",
            "status": "active",
            "mc_number": mc_number
        }
    else:
        return {
            "carrier_name": "Unknown",
            "status": "not found",
            "mc_number": mc_number
        }
    

	# reference_number=rff123, Load #1 is returned.
	# lane=Atlanta to Los Angeles, Load #2 is returned.
@app.get("/loads/{reference_number}")
def get_load_by_reference(reference_number: str):
    try:
        with open("loads.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["reference_number"].lower() == reference_number.lower():
                    return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    raise HTTPException(status_code=404, detail="Load not found")



class BookingConfirmation(BaseModel):
    carrier_name: str
    mc_number: str
    reference_number: str

@app.post("/confirm_booking")
async def confirm_booking(data: BookingConfirmation):
    return {
        "message": "Booking confirmed",
        "carrier": data.carrier_name,
        "mc_number": data.mc_number,
        "reference_number": data.reference_number
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)