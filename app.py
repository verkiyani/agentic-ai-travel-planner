import pandas as pd
import streamlit as st

from src.budget_calculator import estimate_budget
from src.planner import generate_itinerary
from src.recommender import recommend_destinations
from src.utils import load_destination_data

st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Agentic AI Travel Planning System")
st.write("A capstone prototype for personalized AI-driven travel planning.")

data = load_destination_data("data/sample_destinations.csv")

st.sidebar.header("Trip Preferences")

destination = st.sidebar.text_input("Preferred Destination", "Seattle")
days = st.sidebar.slider("Number of Travel Days", 1, 10, 3)
budget_level = st.sidebar.selectbox("Budget Level", ["Low", "Medium", "High"])
interest = st.sidebar.selectbox("Main Interest", ["City", "Nature", "Beach", "Entertainment"])

if st.sidebar.button("Generate Travel Plan"):
    st.subheader("Recommended Destinations")

    recommendations = recommend_destinations(data, budget_level, interest)
    st.dataframe(recommendations)

    selected = recommendations.iloc[0]
    estimated_budget = estimate_budget(selected["avg_daily_cost"], days)

    st.subheader("Estimated Budget")
    st.metric("Estimated Trip Budget", f"${estimated_budget}")

    st.subheader("Generated Itinerary")
    itinerary = generate_itinerary(destination, days, interest)
    itinerary_df = pd.DataFrame(itinerary)
    st.dataframe(itinerary_df)

    st.subheader("AI Planning Explanation")
    st.write(
        f"The system selected recommendations based on the user's budget level "
        f"({budget_level}), travel interest ({interest}), and number of travel days ({days}). "
        f"This demonstrates a simplified agentic workflow using user preferences, "
        f"destination data, recommendation logic, and budget estimation."
    )
else:
    st.info("Use the sidebar to enter trip preferences and generate a travel plan.")