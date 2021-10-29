import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs    
    city = input("please select a city from chicago or new york city or washington: " ).lower()
    while city not in CITY_DATA.keys():
        print ("The city you type is not covered\n\n")
        city = input("please select a city from chicago or new york city or washington: " ).lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("\nTo select month, please type the month or all for all months:\n* january\n* february\n* march\n* april\n* may\n* june\n* all\n\n").lower()
        if month in months:
            break
        else:
            print ("error value")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    while True:
        day = input("\nTo select day, please type the name of day or all for all days of week:\n* saturday\n* sunday\n* monday\n* tuesday\n* wednesday\n* thursday\n* friday\n* all\n\n").lower()
        if day in days:
            break
        else:
            print ("error value")
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('most common month: \n', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('most common day: \n', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print ('most common hour: \n', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print ('most commonly used start station: \n', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print ('most commonly used end station: \n', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    most_combination_stations = group_field.size().sort_values(ascending=False).head(1)
    print('most frequent combination of start station and end station trip: \n', most_combination_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    print('total travel time: \n',total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time: \n',mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('counts of user types: \n',counts_of_user_types)
    

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender = df['Gender'].value_counts()
        print('Gender: \n', Gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth = df['Birth Year'].min()
        print('\nearliest year of birth: \n', earliest_year_of_birth)
        most_recent_year_of_birth = df['Birth Year'].max() 
        print('\nmost recent year of birth: \n', most_recent_year_of_birth)
        most_commen_year_of_birth = df['Birth Year'].mode()[0]
        print('\nmost commen year of birth: \n', most_commen_year_of_birth)
 

    print("\nThis took %s seconds." % (time.time() - start_time))  
    print('-'*40)


def display_raw_data(df):
    
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            if view_data != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()