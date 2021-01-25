###### Datatime conversion.
import pytz
[x for x in pytz.all_timezones if x.startswith("Eu") ]
tz = pytz.timezone('Europe/Zurich')
import datetime
date = datetime.datetime(2020,1,1,tzinfo=pytz.timezone("GMT"))
date.astimezone(tz)
date = datetime.datetime(2020,6,1,tzinfo=pytz.timezone("GMT"))
date.astimezone(tz)


name                hour

2019-01-02 00:00:00    1
2019-01-02 01:00:00    2
2019-01-02 02:00:00    3
2019-01-02 03:00:00    4
2019-01-02 04:00:00    5

name                hour

2019-06-03 00:00:00    2
2019-06-03 01:00:00    3
2019-06-03 02:00:00    4
2019-06-03 03:00:00    5
2019-06-03 04:00:00    6
*****
