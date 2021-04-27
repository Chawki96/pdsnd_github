import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'C:/Users/dell/Desktop/chicago.csv',
              'new york': 'C:/Users/dell/Desktop/new_york_city.csv',
              'washington': 'C:/Users/dell/Desktop/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city=input('whould you like to see data for chicago,new york or washington? \n').lower()
    city_list=['chicago','new york','washington']
      #exception
    while city not in city_list:
        print('\!/ mistake detected')
        print()
        city=input('please type out the full city name : ').lower()
    
    print('looks like you want to hear about {}! if this not true ,restart the program now !'.format(city))
    
    #in this function i used a list of months and days to deal with exceptions

    # get user input for month (all, january, february, ... , june)

    month =input('whould you like to filter the data by a specific month ?if yes which month?january,february ,march......june?if no type "all"  :').lower().title()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    months = ['January', 'February', 'March', 'April', 'May', 'June','All']
    while month not in months:
        print('\!/ mistake detected')
        month=input('please type out the full month name or type "all" if you don\'t want to filter by month  :').lower().title()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('whould you like to filter tha data by a specific day ?if yes which day?monday, tuesday, ... sunday?if no type "all"  :').lower().title()
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday','All']
    while day not in days:
        print('\!/ mistake detected')
        day=input('please type out the full day name or type "all" if you don\'t want to filter by day:').lower().title()
    print('-'*80)
    return city, month,day








def load_data(city, month, day):
    """
    loads Data for one city and filter its data as the user specification (month and day)
    """

    load = pd.read_csv(CITY_DATA[city])
    df=pd.DataFrame(load)
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['day_week']=df['Start Time'].dt.day_name()
    df['month']=df['Start Time'].dt.month_name()
    df['hour']=df['Start Time'].dt.hour

    if month!='All' :
        df=df[df['month']==month ]
    
       
        
    
    if day!='All' :
        
        df=df[df['day_week']==day]
    
    #creat Gender and birth year in case the city is washington

    if city=='washington':
        df['Gender']=np.nan
        df['Birth Year']=''
    
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month :',df['month'].mode()[0])
    print()

    # display the most common day of week
    print('the most common day of week : ',df['day_week'].mode()[0])


    # display the most common start hour
    print('the most start hour : ',df['hour'].mode()[0])
    print()
    print('********************In summary*********************************')
    print(' The Most Frequent Times of Travel is: hour:{}/Day:{}/Month:{}'.format(df['hour'].mode()[0],df['day_week'].mode()[0],df['month'].mode()[0]))
    print('****************************************************************')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular Start Station is : ',df['Start Station'].mode()[0])


    # display most commonly used end station
    print('The most popular End Station is :',df['End Station'].mode()[0])
    
    # display most frequent combination of start station and end station trip
    
    print('most frequent combination of start station and end station trip',df.groupby(['Start Station'])['End Station'].max().head(1))

    print('********************In summary*********************************')
    print('The Most Popular Stations and Trip: Start Station:{}/End Station:{}/(Start Station,End Station):{}'.format(df['Start Station'].mode()[0],df['End Station'].mode()[0],df.groupby(['Start Station'])['End Station'].max().head(1)))
    print('****************************************************************')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time :',df['Trip Duration'].sum())


    # display mean travel time
    print('The Average travel time :',df['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of users types:\n ',df['User Type'].value_counts())
    

    # Display counts of gender
    print('counts of gender:\n',df['Gender'].value_counts())
    
    if df['Gender'].count()==0:
        print('There is no gender information in our database for this city "washington" ')



    # Display earliest, most recent, and most common year of birth
    print('Most common year of birth: ',df['Birth Year'].mode()[0])
    
    if df['Birth Year'].mode()[0]=='':
        print('Sorry there is no information in our database on the date of birth of users for this city')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)



def more_information(df):
    print(df.info())
    print(df.describe())


while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)
    option =input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc=0
    while option=='yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        option=input('do you want to continue yes or no \n')
    option2 =input('Do you want to display some statistics about the data "yes" or "no"\n').lower()
    if option2=='yes':
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
    info=input('do you want more information about the data "yes" or "no" \n').lower()
    if info=='yes':
        more_information(df)

    

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break







       

