import random
import pandas as pd

def generate_real_estate_data(filename="real_estate_data.csv", rows=50):
    districts = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
    property_types = ["new_build", "secondary"]

    data = {
        "City": ["New York"] * rows,
        "District": [random.choice(districts) for _ in range(rows)],
        "Price ($)": [random.randint(200000, 5000000) for _ in range(rows)],
        "Area (m²)": [random.randint(30, 300) for _ in range(rows)],
        "Rooms": [random.randint(1, 6) for _ in range(rows)],
        "Floor": [random.randint(1, 50) for _ in range(rows)],
        "Year Built": [random.randint(1900, 2023) for _ in range(rows)],
        "Property Type": [random.choice(property_types) for _ in range(rows)],
        "Distance to Metro (km)": [round(random.uniform(0.1, 5.0), 2) for _ in range(rows)],
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"File {filename} has been successfully created with {rows} rows of data.")

if __name__ == "__main__":
    generate_real_estate_data()
