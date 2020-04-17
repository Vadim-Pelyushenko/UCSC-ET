import requests
from bs4 import BeautifulSoup

URL = "https://pisa.ucsc.edu/class_search/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

# subjects = soup.find(id='admin_subject')
# print(subjects.prettify())

subjects = soup.find(id='subject')
# print(subjects.prettify())


subjectListText = [i.text for i in subjects.findAll('option')]
subjectListValues = [i.attrs.get('value') for i in subjects.findAll('option')]

#Quick check to make sure the lengths are the same
assert len(subjectListText) == len(subjectListValues)
print (len(subjectListText))

#Print the text shown to the user, and the value of that option
for x in range(len(subjectListText)):
    print(subjectListText[x])
    print(subjectListValues[x])


# for subjectText in subjectListText:
#     print(subjectText)
    # print(subject.text)