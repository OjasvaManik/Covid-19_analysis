from scripts.downloader import download_csv
from scripts.data_cleaning import load_and_preprocess_data
from scripts.analysis import plot_case_growth, plot_vaccination_vs_cases, compare_continent_stats

# URL and file path
url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
file_path = "data/compact.csv"

# Download the dataset
print("Downloading dataset...")
download_csv(url, file_path)

# Load and preprocess data
print("Loading and preprocessing data...")
data = load_and_preprocess_data(file_path)

# Perform analysis
print("Starting analysis...")
plot_case_growth(data, "India")
plot_vaccination_vs_cases(data, "India")
compare_continent_stats(data)

print("Analysis complete!")
