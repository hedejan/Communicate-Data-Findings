# Bike sharing analysis with Ford GoBike dataset
## by Mr. Hussain Balhareth

## Dataset

The data consists of information regarding 1,863,721 bike hiring, including age, timeframe, gender, station, and others. The dataset can be found in Ford GoBike website.  
Dataset: (https://s3.amazonaws.com/fordgobike-data/index.html)  
The data consisted of 16 different variables such as birthday, gender, pickup and drop dates/time, station data and others. It contains 3.31 billion rides. Ages in dataset from 18 to 65 takes 99% of the users in dataset. There were users more than 100 years old. So, we can remove users more than 65 years old as a cleaning and tidy up.
Also, i generated new fields such as age group in order to make grouping and analyze the date by using groups.


## Summary of Findings

* more than 88% of users are subscribers and more than 73% are male users .
* the peak time of day for both round trips is at 8-9AM and 5-6PM which look like work-related to business hours starting and ending periods.
* the group of majority use is '30-34' followed by '25-29'
* the midweek has the largest proportion of use amongt the other weekdays, namely, Tuesdays, Wednesdays and Thursdays.
* a gradual increase in the proportion of use along the year peeking on October and declining towards year end.
* stations 67, 30, 58, 15, and 21 are amongst the most frequently used stations.
* most of the distribution of duration is between 3 - 30 minutes with a percentage of +90%.
* IQR range in hourly base lies between 4 minutes at 5AM to 16 minutes at 3AM and 14PM which represents 50% of the duration data range.
* the mean duration of use by user type is different than the count perspective where the casual customer is >25 minutes while the subscriber is 11 minutes on average.
* females spent the most on average with 14.6 minutes.
* the mean age of most of the users whether by type or gender is between 33 and 36 yrs.
* the distribution of duration by with another dimension which is the start hour where we notice the peaks at 12PM and 21PM. So this graph mixes two univariate graphs and gives more insight on the critical business hours to focus on as duration translates to income.
* midweek days, e.g. Tuesdays, Wednesdays and Thursdays, has the highest rate of duration distribution
* From another dimension (month), I observe that the peaking months are (again) October followed by 3rd quarter.
* the moving duration average with respect to age was steady but I noticed that this average experiences ups and downs peaks above the age of 100 probably due to the lack of sufficient data.
* a steadily increasing duration mean and sudden jump after Friday which is the weekend.
* subscribers are the most frequent bike users overall the time of day with peaks on centain hours.
* Another look at the use count behavior of both customer and subscriber along the weekdays. We notice a drop on the weekends for the subscribers while the trend in customers is more steady although smaller.
* The seasonality of bikers, both customers and subscribers, are normally changing over the course of a year. This trend is more obvious with subscribers.
* distribution of different mean durations for both customers and subscribers demonstrates a dominating curve for subscribers.
* high density of usage per age of both user types are below 150 minutes and below 50 years old.
* In general, I observe that customers tends to use the bikes for longer periods.
* Also, I observe that females have slightly higher records of duration for both user types.
* On the other hand, males age tends to be higher than female genders.
* Also, the age of subscribers tends to be slighly higher regardless of gender.
* I observe that younger customers tends to use bikes for longer periods than olders.
* customer females have the highest mean duration. Probably it's a good idea to attract this class of customers.
* subscriber males have the lowest mean duration.
* I observe mean duration of both user types along the x-axis of age. I observe sharp trends due to lack of sufficient data or users for ages above 65 (counts for less than 1%).


## Key Insights for Presentation

During the analysis work, it was easy for the first look to make a quick conclusion but as we dived into more details and added a second and third dimension, we were able to make more insights and better conclusions considering all given variables whether numeric, categorical, timebased or string data. This gives an idea of the importtance of analytical visualization compared to one-dimensional statistical and mathematical analysis.
