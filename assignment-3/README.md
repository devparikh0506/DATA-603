# Chicago Crime EDA

## Overview
This project conducts an Exploratory Data Analysis (EDA) on the Chicago Crime dataset. The analysis aims to uncover insights related to crime trends, types, and patterns over time using Apache Spark.

## Dataset
The dataset used in this analysis is sourced from the City of Chicago's open data portal, which contains reported incidents of crime from 2001 to the present. The dataset includes various features such as crime type, location, date, and more.

## Technologies Used
- Python
- PySpark
- Jupyter Notebook
- Matplotlib (for visualization)

## Features
- Data cleaning and preprocessing
- Merging similar crime types into broader categories
- Analysis of crime trends over the last decade
- Visualization of crime occurrences by hour and type

## Installation

To run this notebook, ensure you have the following installed:

1. **Python** (version 3.6 or higher)
2. **Apache Spark** (with PySpark)
3. **Jupyter Notebook**
4. **Matplotlib** for visualizations

You can install the required libraries using pip:

```bash
pip install pyspark matplotlib requests
```
## Usage

1. Clone this repository or download the Jupyter Notebook file.

2. Open a terminal and navigate to the directory containing the Chicago_Crime_EDA.ipynb file.

3. Start Jupyter Notebook:

      ```bash
      jupyter notebook
      ```

4. Open Chicago_Crime_EDA.ipynb in your web browser.

5. Run the cells sequentially to perform the EDA on the Chicago Crime dataset.

## Analysis Steps

1. Data Loading: Load the Chicago Crime dataset from the provided API endpoint.
2. Data Cleaning: Handle null values, convert data types, and filter relevant records.
3. Merging Crime Types: Group similar crime types into broader categories for better analysis.
4. Trend Analysis: Analyze crime trends over the last ten years.
5. Visualization: Create visual representations of data including:
   - Year-wise crime trends
   - Hourly distribution of crimes
   - Bar charts for top crime types

## Results
The results of this analysis will provide insights into crime patterns in Chicago, highlighting periods of increased activity and prevalent crime types.

## License
This project is licensed under the MIT License.

## Acknowledgments
- City of Chicago Open Data Portal for providing the dataset.
- Apache Spark documentation for guidance on using PySpark.
