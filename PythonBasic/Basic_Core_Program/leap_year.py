'''
Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not

'''

def find_leap_year(year):
    if(year>999 and year<10000):
       if (year%400==0 and year%100==0 or year%4==0 and year%100!=0):
           return True 
       else:
           return False
    else:
        return None

def main():
    year=input('Enter the year in format YYYY :=>')
    is_leap=find_leap_year(int(year))
    if(is_leap):
        print("The Year : %s is a leap Year"%(year))
    elif(is_leap==None):
        print('Not a valid input should be in format YYYY')
    else:
        print("Year : %s Not a leap year"%(year))
  
main()