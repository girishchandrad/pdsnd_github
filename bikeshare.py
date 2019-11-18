import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

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
    
    
    while True:
        city = input('Experience the best way to get around Chicago, New York City or Washington. Which city you want to explore? \n ->')        
        if city.lower() in ['chicago', 'new york city', 'washington']:
            city = city.lower()
            break
        else:
            print('-> hmm! input is incorrect. Please type correct input.')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Great! Now select a month. The options are :\n \'all\' to select all or January, February, March, April, May, June  \n ->' )   
        if month.lower() in MONTHS:
            month = month.lower()
            break
        else:
            print('-> hmm! input is incorrect. Please type correct input.')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Awesome! Now select a day. The options are :\n \'all\' to select all or Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday  \n ->' )
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            day = day.lower()
            break
        else:
            print('-> hmm! input is incorrect. Please type correct input.')
    

    print('-'*40)
    #print(city, month, day)
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
    #load data, convert the  Start Time column to datetime
    df = pd.read_csv(CITY_DATA[city])
    #print(df.columns)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # get month and day of week from column Start Time and create new columns for filtering
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if all is not selected and create new dataframe
    if month != 'all':
        month = MONTHS.index(month.lower()) + 1
        df = df[df['month'] == month]
    # apply filter to day of week if all is not selected and create new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week: ', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_and_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Common Start and End Station: ', most_common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time :',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time :',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: ',user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('Gender Count: Data not available for Washington!')
    else:
        genders = df['Gender'].value_counts()
        print('Gender Count :',genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('Earliest, Most Recent and Most Common Year of Birth: Data not available for Washington!')
    else:       
        year_of_birth = df['Birth Year']
        most_common_yob = year_of_birth.mode()[0]
        most_recent_yob = year_of_birth.max()
        earliest_yob = year_of_birth.min()    
        print('Earliest, Most Recent and Most Common Year of Birth: ',earliest_yob,',', most_recent_yob,',',most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_records(df):
    """Displays 5 lines of raw data in each iteration  if user specifies."""
    index = 0
    display = input('\nWould you like to see user data? Enter yes to continue or no.\n')
    # TO DO:Clean data to remove extra columns added for filter.
    df = df.drop(['month','day_of_week','hour'],axis=1)
    # TO DO: Display five user details on yes prompt or exit loop.
    while True:
        if display.lower() != 'yes':
            break
        else:
            print(df[index : index + 5])
            index = index + 5   

        display = input('\nWould you like to see next five rows of user data? Enter yes to continue or no.\n')
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        display_records(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
