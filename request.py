import requests
from bs4 import BeautifulSoup

URL = "https://pisa.ucsc.edu/class_search/index.php"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

subjects = soup.find(id='subject')
# print(subjects.prettify())


subjectListText = [i.text for i in subjects.findAll('option')]
subjectListValues = [i.attrs.get('value') for i in subjects.findAll('option')]

#Quick check to make sure the lengths are the same
assert len(subjectListText) == len(subjectListValues)
# print (len(subjectListText))

#Print the text shown to the user, and the value of that option
# for x in range(len(subjectListText)):
#     print(subjectListText[x])
#     print(subjectListValues[x])

#NOTE: These are the computer science and engineering elements
# print(subjectListText[21])
# print(subjectListValues[21])

# Form data that will be sent with the post requests
info = {
    'action': 'results', #This is the line that 'clicks' the search button
    'binds[:term]': '2202',
    'binds[:reg_status]': 'all',
    'binds[:subject]': 'CSE'
        }

# https://requests.readthedocs.io/en/master/api/#requests.Response
response = requests.post(URL, data=info)

# Looks ugly. Use beautifulSoup to make it look better
# This should now be the returned html page
soupResponse = BeautifulSoup(response.text, 'html.parser')
# print(soupResponse.prettify())



#This returns the div of the first class [HARDCODED]
# print(soupResponse.find(id='rowpanel_0').prettify())

#This returns the name of the first class [HARDCODED]
# print(soupResponse.find(id='class_id_62232').text)


# Returns the panel body (the div that all the classes are contained in)
allClassesdiv = soupResponse.find('div', attrs={"class": "panel-body"})



# These are the steps taken to return the name of the first class [DEBUG]
# -----------------
# Hardcoded pulling the very first class' box
temp = allClassesdiv.find(id='rowpanel_0')

# Enter the heading div that contains the class name
temp2 = temp.find('div', attrs={'class': 'panel-heading'})

# Print out the class name
temp3 = temp2.find('a')
# print(temp3.text)
# ----------------



# The links contain the class names and class numbers
allLinks = allClassesdiv.find_all('a')

# This gets the names and numbers of each class listed
# NOTE: only lists everything on the current page(first), not on the next page
classNamesResults = [elem.text.replace(u'\xa0', u' ') for elem in allLinks if "CSE" in elem.text]
classNumbersResults = [elem.text for elem in allLinks if elem.text.isdigit()]


for x in range(len(classNamesResults)):
    print(classNamesResults[x]+'\n'+classNumbersResults[x]+'\n')
