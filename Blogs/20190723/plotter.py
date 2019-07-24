from sys import argv

data_path = argv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_path')
print("The imported data has the following columns:")
print(df.columns)
print("Please enter column number to plot on y-axis:")
y_label = input(prompt)
y_data = df[[ylabel.astype(str)]]

print("Please enter column number to plot on x-axis (default is index):")
x_label = input(prompt)

y_data = df[[ylabel.astype(str)]]

clean_data = y_data.loc[~y_data.isna()]

print("""What kind of plot would you like?
1. Histogram
2. Box and Whiskers
3. Scatter plot"""
plot_flag = input(prompt)

if plot_flag == 1:
    plt.hist(y_data,len(ydata)/10, facecolor='g')
    plt.show()
elif plot_flagg == 2:
    plt.boxplot(y_data)
    plt.show()
elif plot_flag == 3:
    plt.plot(x_data, y_data, 'o')
