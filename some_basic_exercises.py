Exercises --

##print "Example 2: using a variable to store first location"
##first_location = "test".find("t") # here we store the first location of "t"
##print "test".find("t", first_location + 1)

## Write Python code that prints out the number of hours in 7 weeks.

##hoursInSevenWeeks = 7 * 7 * 24
##print hoursInSevenWeeks

##s = 'udacity'
##t = 'bodacious'

##print s[:2] + t[3:]

##sentence = "A NOUN went on a walk. It can VERB really fast."
##substring1 = sentence[0:2]
##substring2 = sentence[6:30]
##substring3 = sentence[34:]

##noun_replacement = "dog" # your noun here
##verb_replacement = "be" # your verb here

##new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3

##print new_sentence
### your code here

## Mary is a world class spy with different aliases across the world.

## Mary is known as Randa in America. 
## But in Europe, her alias Randa has another alias known as Katie.
## In Asia, the alias Katie has another alias known as Salwa.
## In Australia, the alias Salwa is known as Kathleen.
## In South America, the alias Kathleen is known as the alias Gabriel.

## You're a spy yourself and you want to be able to print the real name associated with
## all of these alias names to keep track of Mary, but you only know that 
## gabriel = kathleen, and kathleen = salwa, etc..

## Your mission: knowing how each alias relates to each other, assign the variables 
## gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
## the values for each alias will point to the string "Mary"

## NOTE: We can't simply assign all variables to "Mary".

##mary = "Mary"
### Your code goes here

##randa = mary
##katie = randa 
##salwa = katie
##kathleen = salwa 
##gabriel = kathleen
##kathleen = randa

### In South America, the alias Kathleen is known as the alias Gabriel, this means that:
###gabriel = kathleen

### Test to see if all of these variables will print out the string "Mary"
##print gabriel
##print kathleen
##print salwa
##print katie
##print randa
##print mary

#test = "how are you?"
#test.find("are")

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
## >>> 18
#text = 'all zip files are compressed'
## >>> -1

##text = "all zip files are zipped" 

## ENTER CODE BELOW HERE

#firstOccurrence = text.find('zip')
#secondOccurrence = text.find('zip', firstOccurrence + 1)
#print secondOccurrence

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function


# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

#sentence = "A NOUN went on a walk. They can VERB really well."
#sentence = sentence.replace('NOUN', 'duck')
#sentence = sentence.replace('VERB', 'waddle')

#print sentence

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

#def bigger (a,b):
    #if (a>b):
        #return a
    #else:
        #return b






#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3
# ---

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(a):
    if a == 'D':
        return a
    return false

print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False

# ------

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest (a,b,c):
    return max (a,b,c)
    #if a>b:
        #big = a
    #else:
        #big = b
    #if big>c:
        #return big
    #else:
        #return c


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

# - ----

def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
    
print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

# -----

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers (number):
 counter = 0
 while (counter < number):
        
        counter = counter + 1
        print counter
        
        if counter > 100:
         break

print_numbers(100000000000)
#>>> 1
#>>> 2
#>>> 3

# ----

# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b
    
def printInches(n):
    print str(n) + " inches"

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)

## -----


# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text):
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')

## -----

# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    length = len(sub)
    part_before = somestring[:length+location]
    part_after = somestring[location+length:]
    return part_before + part_after 

# 
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"

## ----

ano = int(input())
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Ano Bissexto")
else:
    print("Não é um ano Bissexto!")


## ----

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# ----



# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown (number):
    while number>0:
        print number
        number = number-1
        if number == 0:
            print 'Blastoff'

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


# -----

# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    if mad_lib.find("NOUN"):
        new_string = mad_lib.replace("NOUN", word_transformer("NOUN"))
        if new_string.find("VERB"):
            return new_string.replace("VERB", word_transformer("VERB"))
    else:
        return mad_lib.replace("VERB", word_transformer("VERB"))    
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

# ----

# Let's put it all together. Write code for the function process_madlib,
# which takes in a string "madlib" and returns the string "processed", where
# each instance of "NOUN" is replaced with a random noun and each instance of
# "VERB" is replaced with a random verb. You're free to change what the
# random functions return as verbs or nouns for your own fun, but for
# submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    index = 0
    word_length = 4
    while index<len(mad_lib):
        frame = mad_lib[index:index+word_length]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add) == 1:
            index += 1
        else:
            index += 4
    return 
     
         
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

# ----

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):

 return days_in_month[month_number-1]

print how_many_days(2)
#>>> 31

print how_many_days(9)
#>>> 30

# ---

# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

print (countries[0][2])/(countries[2][2])

# -----

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(lista):
    result = 0
    for soma in lista:
        result = result + soma
    return result

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134

# ----

def measure_udacity(name_list):
    result = 0
    for names in name_list:
        if name_list[:1] == "U":
            result = result + 1
    return result

# ----

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list,match_list):
    count = 0
    for element in list:
        if element == match_list:
            return count 
        count = count + 1
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'alpha')
#>>> -1

# ----

#We now want to create a list filled with random numbers. The list should be
#of length 20
#What we need to do: Use a While loop to populate this list of random integers.


import random

#print "Random number generated: " + str(random.randint(0,10))

def random_list(number):
    count = 0
    while count < number:
        count += 1
        aleat = str(random.randint(0,10))
        if count == 1:
            mylist = []
        mylist.append(aleat)
        
    print mylist
    print len(mylist)
    
random_list(20)

# ----

#Problem 2 - For Loops
#This problem is taken from Project Euler 25
#If we list all the natural numbers below 10 that are multiples of 3 or 
#5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

smallList = range(1000)
eulerResult = 0
for number in smallList:
    if number%3 == 0 or number%5 == 0:
        eulerResult += number

print eulerResult

# ----

def isLeapYear(year):
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return "This is leap"
            else:
                return "This is not leap"
        else:
            return "This is leap"
    else:
        return "This is not leap"
    
print isLeapYear(2012)
print isLeapYear(2013)

# ----

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < 30:
        day += 1
    else:
        if month < 12:
            month += 1
            day = 1
        else:
            year += 1
            month = 1
            day = 1
            
    return(year, month, day)

print nextDay(2012,12,30)

# ----

#THIS SOLUTION DOESN'T WORK

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year1, month1, day1):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day1 < 30:
        day1 += 1
    else:
        if month1 < 12:
            month1 += 1
            day1 = 1
        else:
            year1 += 1
            month1 = 1
            day1 = 1
            
    return(year1, month1, day1)
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    if year1 <= year2 and month1 <= month2 and day1 <= day2:
        nOfDays = 0
        while nextDay < (year2, month2, day2):
            
            nOfDays += 1
            
    return nOfDays

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
# ----

# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def changeNumberOfDaysInMonth(month):
    return days_in_month[month-1]

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < changeNumberOfDaysInMonth(month):
        if isLeapYear:
            days_in_month[1] += 1
            return year, month, day + 1
        else:
            return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
            
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

#print daysBetweenDates(1900,1,1,1999,12,31) 37199

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
