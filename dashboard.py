import streamlit as st
import pandas as pd

# Simulate some confirmed booking data
confirmed_bookings = [
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
    },
    {
        "carrier_name": "ABC LOGISTICS",
        "mc_number": "123456",
        "reference_number": "REF04684",
        "commodity": "Agricultural Products",
        "origin": "Dallas, TX",
        "destination": "Chicago, IL",
        "pickup_time": "2025-04-11 09:00",
        "delivery_time": "2025-04-12 16:00",
        "special_requirements": "None",
        "agent_name": "Emily",
        "caller_sentiment": "neutral"
    }
]

# Convert to DataFrame
df = pd.DataFrame(confirmed_bookings)

st.title("📦 Booking Confirmations Dashboard")

# Optional filter
sentiment = st.selectbox("Filter by Caller Sentiment", ["All"] + list(df["caller_sentiment"].unique()))
if sentiment != "All":
    df = df[df["caller_sentiment"] == sentiment]

agent = st.selectbox("Filter by Agent", ["All"] + list(df["agent_name"].unique()))
if agent != "All":
    df = df[df["agent_name"] == agent]

st.write("### Filtered Confirmed Bookings")
st.dataframe(df)

st.write("### Summary Stats")
st.metric("Total Bookings", len(df))
st.metric("Unique Carriers", df["carrier_name"].nunique())