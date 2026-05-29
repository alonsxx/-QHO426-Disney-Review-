import matplotlib.pyplot as plt

# Function to draw bar chart for reviews per park
def plot_reviews_per_park(reviews_by_park):
    parks = list(reviews_by_park.keys())
    counts = list(reviews_by_park.values())

    plt.figure(figsize=(8, 5))
    plt.bar(parks, counts, color='skyblue')
    plt.title("Number of Reviews per Park")
    plt.xlabel("Park Name")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to draw line chart for average rating per year per park
def plot_average_rating_by_year(avg_rating):
    for park, year_data in avg_rating.items():
        years = sorted(year_data.keys())
        ratings = [year_data[year] for year in years]

        plt.plot(years, ratings, marker='o', label=park)

    plt.title("Average Rating by Year (per Park)")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
