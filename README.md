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

**Request**
