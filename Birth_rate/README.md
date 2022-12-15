#Birth Rate Analysis
This project is an exploratory data analysis of birth data in the United States. The data is loaded using the pandas library and basic statistics are calculated using the describe() method. The day column is converted to a datetime data type and missing values are imputed with zeros. A decade column is created by dividing the year by 10 and rounding down to the nearest integer.

A pivot table is created to visualize the total number of births by gender and decade, and this is plotted using the plot() method from the matplotlib library. Outliers are removed from the data by filtering out values that are more than 5 standard deviations from the mean.

Finally, a pivot table is created to visualize the average number of births by day of the week for each decade. This is also plotted using the plot() method.

In conclusion, this project demonstrates how to analyze birth data using the pandas and matplotlib libraries. It also shows how to clean and transform data, create pivot tables, and create plots to visualize the data.
