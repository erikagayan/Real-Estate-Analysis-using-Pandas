# Real Estate Analysis Using Pandas

## Overview

This project focuses on analyzing real estate data using Python's Pandas library. The analysis aims to uncover insights into property prices, distributions, and correlations with various factors such as distance to metro stations, number of rooms, and year built.

## Dataset

The dataset used for this analysis includes the following columns:

- **City**: Name of the city where the property is located.
- **District**: Specific district within the city.
- **Price ($)**: Listing price of the property in US dollars.
- **Area (m²)**: Total area of the property in square meters.
- **Rooms**: Number of rooms in the property.
- **Floor**: Floor number where the property is situated.
- **Year Built**: Year the property was constructed.
- **Property Type**: Indicates whether the property is a new build or secondary (resale).
- **Distance to Metro (km)**: Distance from the property to the nearest metro station in kilometers.

## Analysis Steps

1. **Data Loading**: Import the dataset using Pandas.

2. **Data Cleaning**: Handle missing values, correct data types, and ensure data consistency.

3. **Feature Engineering**:
   - Calculate the price per square meter and add it as a new column.

4. **Descriptive Statistics**:
   - Compute average property prices in different cities.
   - Identify the most expensive and cheapest properties.
   - Calculate correlations between price and other variables such as distance to metro, number of rooms, and year built.

5. **Data Visualization**:
   - Plot histograms to show the distribution of property prices.
   - Create scatter plots to visualize the relationship between price and distance to metro.
   - Generate box plots to compare property prices across different cities.

## Tools and Libraries

- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static visualizations.
- **Seaborn**: For enhanced statistical data visualization.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/erikagayan/Real-Estate-Analysis-using-Pandas.git
# Real-Estate-Analysis-using-Pandas