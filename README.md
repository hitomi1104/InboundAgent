# 📞 Inbound Voice Agent for HappyRobot Logistics

This project simulates a voice-enabled AI agent for carrier sales reps at **HappyRobot Logistics**. The agent validates carrier MC numbers using the FMCSA API, matches them with available loads based on reference numbers, and confirms bookings via a RESTful API.

---

## Project Summary

- AI Agent answers inbound calls from carrier reps  
- Collects MC number and Reference Number  
- Validates carrier with FMCSA API  
- Searches available loads from CSV based on Reference Number
- Classifies carrier intent (e.g. interested, too expensive, etc.)
- Extracts additional context like **sentiment** and **decline reason**
- Confirms bookings via `POST` to a backend endpoint 

---

## 🚀 Features

- FMCSA API integration  
- Load lookup from CSV  
- Booking confirmation via POST  
- Extract carrier sentiment and intent 
- Classify carrier intent from conversation
- Deployed via Render  
- Environment-secured API keys

---

## 📂 API Endpoints

| Method | Endpoint                          | Description                             |
|--------|-----------------------------------|-----------------------------------------|
| `GET`  | `/loads/{reference_number}`       | Look up load details by reference ID    |
| `GET`  | `/verify_carrier?mc_number=123456`| Validate carrier via FMCSA              |
| `POST` | `/confirm_booking`                | Confirm and record booking details      |

---

## 🔍 Sample API Usage
 (Doc: https://inboundagent.onrender.com/redoc#operation/root__get)
### ✅ GET `/loads/{reference_number}`
Retrieve the full details of a load from loads.csv, based on the reference number the carrier saw online.

**Example Request**
'''
https://inboundagent.onrender.com/loads/REF09460
'''
**Example Response**
```json
{
  "reference_number": "REF09460",
  "origin": "Denver, CO",
  "destination": "Detroit, MI",
  "equipment_type": "Dry Van",
  "rate": "868",
  "commodity": "Automotive Parts"
}
```

---

### ✅ `GET /verify_carrier?mc_number={mc_number}`  
Validate carrier's MC number using the FMCSA API.

**Example Request**
```
GET https://inboundagent.onrender.com/verify_carrier?mc_number=302238
```

**Example Response**
```json
{
  "carrier_name": "P I T A TRUCKING INC",
  "status": "active",
  "mc_number": "302238"
}
```

---

### ✅ `POST /confirm_booking`  
Store a booking confirmation submitted by a verified carrier.

**Example Request**
```
POST https://inboundagent.onrender.com/confirm_booking
```

**Request Body**
```json
{
  "carrier_name": "P I T A TRUCKING INC",
  "mc_number": "302238",
  "reference_number": "REF09460",
  "commodity": "Automotive Parts",
  "origin": "Denver, CO",
  "destination": "Detroit, MI",
  "pickup_time": "2025-04-10 08:00",
  "delivery_time": "2025-04-11 14:00",
  "special_requirements": "TWIC",
  "agent_name": "Paul",
  "caller_sentiment": "happy"
}
```

**Example Response**
```json
{
  "carrier_name": "P I T A TRUCKING INC",
  "mc_number": "302238",
  "reference_number": "REF09460",
  "commodity": "Automotive Parts",
  "origin": "Denver, CO",
  "destination": "Detroit, MI",
  "pickup_time": "2025-04-10 08:00",
  "delivery_time": "2025-04-11 14:00",
  "special_requirements": "TWIC",
  "agent_name": "Paul",
  "caller_sentiment": "happy"
}
```

---

## 🎥 Demo

> [https://www.loom.com/share/23ac5d47b2e9402db1342fa479732333?sid=99c94c4f-94f5-4d8b-aa20-700474d090c4]  
> This 5-minute video walks through the HappyRobot Inbound Voice Agent in action. It simulates a real call between a carrier and the AI agent, showcasing how the system:
- Collects and verifies carrier information using the FMCSA API
- Finds available loads based on reference numbers
- Presents detailed load offers including rate, location, equipment, and timing
- Classifies the carrier’s response (e.g. interested, too expensive)
- Extracts caller sentiment and booking details
- Automatically confirms the booking via a POST request to the backend
- It also includes a high-level overview of the system architecture and the tech stack used to build and deploy the solution.
