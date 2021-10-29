# Project Name 
Bike Share Data

## Project description
use data from 3 cities in US "Chicago, New York City, and Washington" and computing some of their descriptive statistics. 

## Requirements 
code should provide the following information:
1. Popular times of travel
2. Popular stations and trip
3. Trip duration
4. User info

## Installation

This project need this files to work (bikeshare.py - chicago.csv - new_york_city.csv - washington.csv)
 "bikeshare.py" this file contain the code of the projct. 
 "csv" files contain the data needed in the porjct. 

 to run the projct you should run this commend into terminal: python bikeshare.py
 or from VS code you can click on the run button.


## Functionality

This project contains six functions:
# city, month, day = get_filters()
Asks user to specify a city, month, and day to analyze.

# df = load_data(city, month, day)
Loads data for the specified city and filters by month and day if applicable.

# time_stats(df)
Displays statistics on the most frequent times of travel

# station_stats(df)
Displays statistics on the most popular stations and trip.

# trip_duration_stats(df)
Displays statistics on the total and average trip duration.

# user_stats(df)
Displays statistics on bikeshare users. 


## Ref 

* Python If ... Else:
https://www.w3schools.com/python/python_conditions.asp
* Pandas DataFrame:
https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
