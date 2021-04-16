import os

import pandas
import matplotlib.pyplot as plt
import seaborn

def main():
    cwd = os.getcwd()
    if(not os.path.exists(os.path.join(cwd, "Results"))):
        os.makedirs(os.path.join(cwd, "Results"))

    csvFile = os.path.join(cwd, 'Temps.csv')

    df = pandas.read_csv(csvFile)

    city_temp_label = 'city_temp'
    global_data_label = 'global_temp'

    minWindow = 10
    minPeriods = 1

    # Fill the NaN with a rolling average of 10 years if possible.
    df = df.fillna(df.rolling(window=minWindow, min_periods=minPeriods, center=True).mean())
    city_temp_10yr_rolling_avg = df[city_temp_label].rolling(window=minWindow, min_periods=minPeriods, center=True).mean()
    city_temp_max = df[city_temp_label].max()
    city_temp_min = df[city_temp_label].min()
    city_temp_range = city_temp_max - city_temp_min
    global_temp_10yr_rolling_avg = df[global_data_label].rolling(window=minWindow, min_periods=1, center=True).mean()
    global_temp_max = df[global_data_label].max()
    global_temp_min = df[global_data_label].min()
    global_temp_range = global_temp_max - global_temp_min
    df.insert(len(df.columns), column='city_temp_10yr_rolling_avg', value=city_temp_10yr_rolling_avg)
    df.insert(len(df.columns), column='global_temp_10yr_rolling_avg', value=global_temp_10yr_rolling_avg)
    print("City Max: {} Min: {} Range: {}".format(city_temp_max, city_temp_min, city_temp_range))
    print("Global Max: {} Min: {} Range: {}".format(global_temp_max, global_temp_min, global_temp_range))

    # x and y need to match the 
    # seaborn.scatterplot(x="year", y="global_data", data=df)
    axes = df.plot(x='year', legend=True)
    axes.set_ylabel("Degrees(C)")
    axes.set_title("City(Miami) vs Global Yearly Average Temperature")

    # plt.show() doesn't work in WSL because of headless console or something
    plt.savefig('Results/Analysis.png')
    df.to_csv('Results/InterpolatedTemperatures.csv')
    
if __name__ == "__main__":
    main()