import pandas as pd


def recommend_destinations(data, budget_level, interest):
    filtered = data[
        (data["budget_level"].str.lower() == budget_level.lower()) |
        (data["category"].str.lower() == interest.lower())
    ]

    if filtered.empty:
        return data.head(3)

    return filtered.head(5)