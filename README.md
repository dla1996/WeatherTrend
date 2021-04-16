# WeatherTrend

Denwis La
Weather Trends
	Tools Used: Python, Pandas, Matplotlib
	I extracted the temperature data from the SQL schema by filtering by the closest large city to me, which is Miami. Only the city_temp, global_temp, and year information was extracted to a single CSV file. 
I chose to use matplotlib to plot the data as it is the method that I am most familiar with. 
From there, I used Python with pandas and matplotlib to calculate and plot the data. The extracted city_temp information for the city of Miami had some years of missing temperature data. I filled in the missing years with running averages up to 10 years if 10 years was available prior to the missing year as an attempt to interpolate the data for the missing years, then I calculated 10 year running averages for both the city and global temperatures. 
 
![Plot](https://github.com/dla1996/WeatherTrend/blob/master/Results/Analysis.png)

Observations
1.	Miami city has a much higher average temperature compared to the global temperature and has been consistent each year. This could be due to more areas being cold than areas being hot. Data averages can be skewed by outliers.
2.	Miami has larger deltas in temperature averages each year than the global average temperatures. The range of Miami’s yearly average temperature is about 9.3799 degrees Celsius and the global range is about 2.99 degrees Celsius. 
3.	Overall, the trend looks to be that the average temperature is increasing over the past few hundred years. 
4.	Even though Miami has a higher temperature than the global average, the general movement of average temperatures are the same; if the global average goes down for a couple of years, so does Miami. Though with Miami, these decreases or increases in temperature are more pronounced since again, averages can be skewed by either extreme lows or extreme highs.
5.	The beginning of the dataset trend for the first 100 years don’t really match up due to what I believe to be a lack of temperature records. For Miami, there were some years where there was no average temperature data, which could be due to no data having been recorded at that certain year, which brought me to try to interpolate the first 100 years. After that point, the general trend matches pretty close.
