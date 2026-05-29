import csv
import os

# SECTION A - Load Data
def load_data(file_path="data/disneyland_reviews.csv"):
    data = []
    with open(file_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# SECTION B - View Data
def get_reviews_by_park(data, park_name):
    reviews = []
    for review in data:
        if review["Branch"].lower() == park_name.lower():
            reviews.append(review)
    return reviews

def count_reviews_by_park_and_location(data, park_name, location):
    count = 0
    for review in data:
        if (review["Branch"].lower() == park_name.lower()) and (
            review["Reviewer_Location"].lower() == location.lower()
        ):
            count += 1
    return count

def average_rating_by_park_and_year(data, park_name, year):
    ratings = []
    for review in data:
        if (review["Branch"].lower() == park_name.lower()) and review[
            "Year_Month"
        ].startswith(str(year)):
            ratings.append(int(review["Rating"]))
    if len(ratings) == 0:
        return None
    else:
        return sum(ratings) / len(ratings)

# SECTION C - Helper for Chart
def count_reviews_by_park(data):
    reviews_by_park = {}
    for review in data:
        park = review["Branch"]
        if park not in reviews_by_park:
            reviews_by_park[park] = 0
        reviews_by_park[park] += 1
    return reviews_by_park

def average_rating_for_chart(data):
    result = {}

    for review in data:
        park = review['Branch']
        year = review['Year_Month'].split('-')[0]
        rating = int(review['Rating'])

        if park not in result:
            result[park] = {}

        if year not in result[park]:
            result[park][year] = {'total': 0, 'count': 0}

        result[park][year]['total'] += rating
        result[park][year]['count'] += 1

    for park in result:
        for year in result[park]:
            total = result[park][year]['total']
            count = result[park][year]['count']
            result[park][year] = total / count

    return result

# SECTION D - Export
def export_reviews_to_csv(reviews, filename):
    if len(reviews) == 0:
        print("No reviews to export.")
        return

    os.makedirs("export", exist_ok=True)
    filepath = os.path.join("export", filename)

    with open(filepath, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=reviews[0].keys())
        writer.writeheader()
        writer.writerows(reviews)

    print(f"✅ Exported {len(reviews)} reviews to {filepath}")
