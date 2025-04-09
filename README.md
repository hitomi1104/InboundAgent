# 📞 Inbound Voice Agent for HappyRobot Logistics

This project simulates a voice-enabled AI agent for carrier sales reps at **HappyRobot Logistics**. The agent validates carrier MC numbers using the FMCSA API, matches them with available loads based on reference numbers, and confirms bookings via a RESTful API.

---

## 🧠 Project Summary

- AI Agent answers inbound calls from carrier reps  
- Collects MC number and Reference Number  
- Validates carrier with FMCSA API  
- Searches available loads from CSV based on Reference Number  
- Confirms bookings via `POST` to a backend endpoint  
- Extracts additional context like **sentiment** and **decline reason**

---

## 🚀 Features

✅ FMCSA API integration  
✅ Load lookup from CSV  
✅ Booking confirmation via POST  
✅ Extract carrier sentiment and intent  
✅ Deployed via Render  
✅ Environment-secured API keys

---

## 📂 API Endpoints

| Method | Endpoint                          | Description                             |
|--------|-----------------------------------|-----------------------------------------|
| `GET`  | `/loads/{reference_number}`       | Look up load details by reference ID    |
| `GET`  | `/verify_carrier?mc_number=123456`| Validate carrier via FMCSA              |
| `POST` | `/confirm_booking`                | Confirm and record booking details      |

---

## 🔍 Sample API Usage

### ✅ GET `/loads/REF09460`

**Response**
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

### ✅ `GET /verify_carrier?mc_number=...`  
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
Content-Type: application/json
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

> [Insert Loom/Youtube link here]  
> Includes walkthrough of API functionality, GET & POST examples, and explanation of code structure.
