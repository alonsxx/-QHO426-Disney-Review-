import visual
from process import (
    load_data,
    get_reviews_by_park,
    count_reviews_by_park_and_location,
    average_rating_by_park_and_year,
    count_reviews_by_park,
    average_rating_for_chart



)
import tui


def handle_view_data(data):
    while True:
        tui.display_view_data_submenu()
        sub_choice = tui.get_user_choice("Enter option (1-4): ")

        if sub_choice == "1":
            park = input("Enter park name (example: Disneyland_HongKong): ")
            reviews = get_reviews_by_park(data, park)
            for r in reviews[:10]:  # show first 10 rows
                print(r)
            print("Total reviews:", len(reviews))

        elif sub_choice == "2":
            park = input("Enter park name: ")
            location = input("Enter reviewer location: ")
            count = count_reviews_by_park_and_location(data, park, location)
            print(f"Total {count} reviews from {location} for {park}")

        elif sub_choice == "3":
            park = input("Enter park name: ")
            year = input("Enter year (example: 2019): ")
            avg = average_rating_by_park_and_year(data, park, year)
            if avg is None:
                print("No reviews found for that year.")
            else:
                print("Average rating:", round(avg, 2))

        elif sub_choice == "4":
            break

        else:
            print("Invalid option.")

def handle_view_charts(data):
    reviews_by_park = count_reviews_by_park(data)
    visual.plot_reviews_per_park(reviews_by_park)

    avg_rating = average_rating_for_chart(data)
    visual.plot_average_rating_by_year(avg_rating)

def handle_export(data):
    park = input("Enter park name to export reviews for: ")
    reviews = get_reviews_by_park(data, park)

    if not reviews:
        print("❌ No reviews found for that park.")
        return

    filename = input("Enter filename to save CSV (example: output.csv): ")
    from process import export_reviews_to_csv
    export_reviews_to_csv(reviews, filename)



def main():
    tui.display_title()
    data = load_data()
    print("\nLoaded", len(data), "review")

    while True:
        tui.display_main_menu()
        choice = tui.get_user_choice()

        if choice == "Q":
            print("Exiting. Goodbye!")
            break
        elif choice == "A":
            handle_view_data(data)
        elif choice == "B":
            handle_view_charts(data)
        elif choice == "C":
            handle_export(data)
        else:
            print("Invalid choice. Try again.")


if _name_ == "_main_":
    main()
