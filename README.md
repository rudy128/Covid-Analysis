# COVID Cases Analysis System (CCAS)

## Overview

The COVID Cases Analysis System (CCAS) is a Python application that allows users to analyze and visualize COVID-19 data from different states. Utilizing a graphical user interface, users can easily load CSV data files and perform various analyses, including comparisons and visualizations of confirmed, recovered, active, and death cases.

## Features

- **Data Loading**: Select and load CSV files containing COVID-19 statistics.
- **Data Analysis**: Options to analyze cases by state, calculate totals and percentages, and find top states.
- **State Comparisons**: Compare COVID-19 statistics between different states.
- **Graphical Visualization**: Generate bar charts and pie charts to visualize data.

## Requirements

- Python 3.x
- `pandas`
- `matplotlib`
- `tkinter` (usually included with Python installations)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rudy128/Covid-Analysis.git
   cd covid-cases-analysis
   ```

2. **Install the required packages**:

   ```bash
   pip install pandas matplotlib tk
   ```

## Usage

1. Run the application:

   ```bash
   python CCDA.py
   ```

2. A file dialog will open, prompting you to select a CSV file containing COVID-19 data. The expected columns are:
   - `State`
   - `Confirmed`
   - `Recovered`
   - `Deaths`
   - `Active`
   - `Total`

3. Choose an option from the menu to analyze the data:
   - Analyze COVID cases by state
   - Calculate total and percentage of cases
   - Find top states by confirmed cases
   - Compare statistics between states
   - Graphically visualize state-specific data
   - Graphically visualize overall country data

## Example CSV Structure

Ensure your CSV file has the following structure:

```csv
State,Confirmed,Recovered,Deaths,Active,Total
State1,1000,800,50,150,2000
State2,2000,1800,100,100,3000
...
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please submit a pull request or open an issue.
