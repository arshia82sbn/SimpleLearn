import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data to predict up to 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series([i for i in range(1880, 2051)])
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    plt.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (using data from year 2000 to predict up to 2050)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, 'green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (do not change)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
