# Udacity
# Intro to Python

# Lesson 3: Data Stuctures and loops

# Lists

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number - 1]

print(how_many_days(8))


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list

print(eclipse_dates[-3:])


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    if len(input_list) < 3:
        return sorted(input_list, reverse=True)
    else:
        return sorted(input_list, reverse=True)[0:3]


def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    if len(numbers) % 2:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index] ) / 2


test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))


# For Loops

def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for item in input_list:
        sum += item

    return sum


#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))



"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(strList):
    count = 0
    for item in strList:
        if ('<' in item) and ('>' in item):
            count += 1
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))



#define the  html_list function

def html_list(strList):
    htmlstr = '<ul>\n'
    for item in strList:
        htmlstr += '<li>{}</li>\n'.format(item)
    htmlstr += '</ul>'
    return htmlstr

print(html_list(['first string', 'second string']))
print(html_list([1, 2, 3]))
print(html_list(["strings", 2.0, True, "and other types too!"]))



def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    # todo: print this line height-2 times, instead of three times
    for i in range(height - 2):
        print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5) # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!


# While loop

#TODO: Implement the nearest_square function
def nearest_square(limit):
    i = 1
    while i * i < limit:
        i += 1
    return (i-1) * (i-1)

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

i = 0
while True:
    news_ticker += headlines[i] + ' '
    i += 1
    if len(news_ticker) >= 140:
        break
news_ticker = news_ticker[0:140]

print(news_ticker)


def check_answers(my_answers,answers):
    """
    Checks the answers provided to a multiple choice quiz and returns the results.
    """
    results= []
    for i in range(len(answers)):
        if my_answers[i] == answers[i]:
            results.append(1)
        else:
            results.append(0)

    # Total correct answers
    count_correct = sum(results)

    # Display message based on number of correct answers
    if count_correct / 5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif (len(results) - count_correct)/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


 # Define the remove_duplicates function
def remove_duplicates(collection):
    new_collection = []
    for item in collection:
        if item not in new_collection:
             new_collection.append(item)
    return new_collection


# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers
n = 1
squares = set()
while n ** 2 < 2000:
    squares.add(n ** 2)
    n += 1


# Dictionaries II

from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1


# Quiz: Prolific Year
#Write a function most_prolific that takes a dict formatted like
# Beatles_Discography example above and returns the year in which
# the most albums were released. If you call the function on the
# Beatles_Discography it should return 1964, which saw more releases
# than any other year in the discography.

def most_prolific(dict):
    year_count = {}
    prolific_year = []

    for item in dict:
        if dict[item] in year_count:
            year_count[dict[item]] += 1
        else:
            year_count[dict[item]] = 1

    max_release = max(year_count.values())
    for year in year_count:
        if year_count[year] == max_release:
            prolific_year.append(year)

    if len(prolific_year) == 1:
        return prolific_year[0]
    else:
        return prolific_year


# Compound Data Structures

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(yearly_record):
    total = 0
    for month in monthly_takings:
        total += sum(monthly_takings[month])
    return total