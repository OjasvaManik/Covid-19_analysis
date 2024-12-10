import pandas as pd

def load_and_preprocess_data(filepath):
    # Load data
    covid_data = pd.read_csv(filepath)

    # Select relevant columns
    relevant_columns = [
        "country", "date", "total_cases", "new_cases_smoothed",
        "total_deaths", "new_deaths_smoothed", "total_vaccinations",
        "people_vaccinated", "people_fully_vaccinated",
        "total_cases_per_million", "stringency_index", "population", "continent"
    ]
    covid_data = covid_data[relevant_columns]

    # Convert 'date' to datetime
    covid_data["date"] = pd.to_datetime(covid_data["date"])

    # Fill missing values with 0 where appropriate
    covid_data.fillna(0, inplace=True)

    return covid_data
