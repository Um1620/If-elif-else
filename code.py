# Using conditional statements, check if the number is:
# Even or Odd.
# Positive, Negative, or Zero.
# Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and
# print statement for each case.


# Positive, Negative, or Zero.

num:int=int(input("Enter your input"))
def conditional_statement():
    if num > 0:
        print("The num is Positive")
    elif num < 0:
        print("The number is Negatve")
    else:
        print("The num is zero ")

    
    # Even or Odd.

    if num % 2 ==0:
        print("The number is Even")
    else:
        print("The num is Negative")



# Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and
# print statement for each case.

if num % 2 == 0 and num % 3 ==0 :
    print("num is divisible by 2 and 3")
elif num % 2 == 0:
    print("The num is divisible by 2 not 3")
elif num % 3 == 0:
    print("The num is divsible by 3 not 2")
else:
    print("The num is not divisible by two nor 3")

# Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
 # Check if a year is a leap year or not.  

month:int=int(input("Enter your input :")) 
 def day_in_month(year, month):
    if month == 1:
        print("January(31 days)")
    elif month ==2:
        print("February(28 days)")
    elif month ==3:
        print("March(31 days)")
    elif month ==4:
        print("April(30 days)")
    elif month ==5:
        print("May(31 days)")
    elif month ==6:
        print("June(30 days)")
    elif month ==7:
        print("July(31 days)")
    elif month ==8:
        print("August(31 days)")
    elif month ==9:
        print("September(30 days)")
    elif month ==10:
        print("October(31 days)")
    elif month ==11:
        print("November(30 days)")
    elif month ==12:
        print("December(31 days)")
    else:
        print("This year is leap year or not")

def is_leap_year(year):
    # Leap year if divisible by 4, but not divisible by 100 unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
       else:
        return False

#  Write a program that takes the age of a person as input and determines whether they are a child (0-12 years),
#  teenager (13-19 years)
#  adult (20-59 years) 
# senior citizen (60 years and above)

age:int=int(input("Enter your input :"))

if age <= 12:
    print("They are child")
elif age <= 19:
    print("They are teenagers")
elif  age <= 59:
    print("They are adult")
else:
    print("They are are senior citizen")


# Take the user age.
 #  If the age is 18 or above:
# Ask if they have a nationality of "Pakistani".
# If yes, print "You are eligible to vote."
# If no, print "Please obtain a valid ID to vote.

def user_age():
    if user_age >= 18:
        output=input("Do you have "Pakistani"nationalit (yes/no)")
        if output == "yes":
            print("They are eligible to vote")
        elif output =="No":
            print("plz obtain a valid id")
        else:
            print("You are not eligible to vote")