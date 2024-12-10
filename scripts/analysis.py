import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def plot_case_growth(data, region):
    # Filter data for the specified region
    region_data = data[data["country"] == region]

    # Plot total cases over time
    plt.figure(figsize=(12, 6))
    plt.plot(region_data["date"], region_data["total_cases"], label="Total Cases", color="blue")

    # Set titles and labels
    plt.title(f"COVID-19 Case Growth in {region}", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Total Cases (Number)", fontsize=12)

    # Format the Y-axis to display large numbers in a readable way (e.g., 1M, 10M)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1e6)}M"))

    # Add grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


def plot_vaccination_vs_cases(data, region):
    # Filter data for the specified region
    region_data = data[data["country"] == region]

    # Plot total cases and vaccination progress
    plt.figure(figsize=(12, 6))
    plt.plot(region_data["date"], region_data["total_cases"], label="Total Cases", color="blue")
    plt.plot(region_data["date"], region_data["people_fully_vaccinated"], label="Fully Vaccinated", color="green")

    # Set titles and labels
    plt.title(f"Vaccination Progress vs Cases in {region}", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Number of People", fontsize=12)

    # Format the Y-axis to display large numbers in a readable way
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1e6)}M"))

    # Add grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()


def compare_continent_stats(data):
    # Group data by continent and calculate total cases and vaccinations
    continent_data = data.groupby("continent").agg({
        "total_cases": "max",
        "people_fully_vaccinated": "max"
    }).reset_index()

    # Plot comparison
    plt.figure(figsize=(12, 6))
    x = range(len(continent_data))
    plt.bar(x, continent_data["total_cases"], width=0.4, label="Total Cases", color="blue", align="center")
    plt.bar([p + 0.4 for p in x], continent_data["people_fully_vaccinated"], width=0.4, label="Fully Vaccinated", color="green", align="center")

    # Set titles, labels, and ticks
    plt.title("Total Cases vs Fully Vaccinated by Continent", fontsize=14)
    plt.xlabel("Continent", fontsize=12)
    plt.ylabel("Number of People", fontsize=12)
    plt.xticks([p + 0.2 for p in x], continent_data["continent"], fontsize=10)

    # Format the Y-axis to display large numbers in a readable way
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1e6)}M"))

    # Add grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)

    # Show the plot
    plt.tight_layout()
    plt.show()

