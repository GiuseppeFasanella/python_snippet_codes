from datetime import datetime
import pandas as pd
import glob

available_regrs = glob.glob('test*')
available_dates = []


for regr in available_regrs:
    available_dates.append(datetime.strptime(regr.split("_")[1], '%Y-%m-%d'))
available_dates = sorted(available_dates)


# test_2015-07-05  test_2016-01-05  test_2017-02-01  test_2017-02-08

my_forecastdates = [datetime(2017,2,1),datetime(2017,2,2),datetime(2017,2,3),datetime(2017,2,4),datetime(2017,2,5),datetime(2017,2,6),datetime(2017,2,7),datetime(2017,2,8)]
for my_forecastdate in my_forecastdates:
    #print('**********************')                                                                                                                                                    
    #for date_regr in available_dates:                                                                                                                                                  
    #    print(my_forecastdate, date_regr)                                                                                                                                              
    #    print((my_forecastdate - date_regr).total_seconds()>=0)                                                                                                                        


    closest_date_regr = max(date_regr for date_regr in available_dates if (my_forecastdate - date_regr).total_seconds()>=0)
    print(my_forecastdate,closest_date_regr)

