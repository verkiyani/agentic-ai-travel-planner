def generate_itinerary(destination, days, interests):
    itinerary = []

    for day in range(1, days + 1):
        itinerary.append({
            "Day": day,
            "Morning": f"Explore popular attractions in {destination}",
            "Afternoon": f"Enjoy activities related to {interests}",
            "Evening": f"Relax, try local food, and review the next day's plan"
        })

    return itinerary