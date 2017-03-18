import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

# Name: Mingda Tang
# Section Day/Time: Friday 1-2PM
# References: 
# Expected score: 150/150
# Other notes

# Part One
i = 0
url_nyt = 'http://www.nytimes.com'
html_nyt = urllib.request.urlopen(url_nyt).read()
soup_nyt = BeautifulSoup(html_nyt, 'html.parser')

print ('New York Times -- First 10 Story Headings')
# Finding all lines of the story-heading class
for story_heading in soup_nyt.find_all(class_='story-heading'):
    if story_heading.a and story_heading.a.text:
        # Getting text from anchor tag and stripping whitespace
        print (story_heading.a.get_text().strip())
        i += 1
    # If heading is not in anchor tag (Ex: text heading on videos)
    elif story_heading.text:
        print (story_heading.get_text().strip())
        i += 1
    else:
        continue
    # After 10 headings are printed, exit loop
    if i >= 10:
    	break
# Printing blank line to separate output
print ('')


# Part Two
url_md = 'http://www.michigandaily.com'
html_md = urllib.request.urlopen(url_md).read()
soup_md = BeautifulSoup(html_md, 'html.parser')

print ('Michigan Daily -- MOST READ')
# Finding all lines of the item-list class
for item_list in soup_md.find_all(class_='item-list'):
    for story_heading in item_list.find_all('a'):
        print (story_heading.get_text())

print ('')


# Part Three
url_collemc = 'http://www.collemc.people.si.umich.edu/data/gallery.html'
html_collemc = urllib.request.urlopen(url_collemc).read()
soup_collemc = BeautifulSoup(html_collemc, 'html.parser')

print ("Colleen's page -- Alt tags")
# Finding all lines of the img tag
for image in soup_collemc.find_all('img'):
    # If there is no alt attribute
    if image.get('alt') == None:
        print ("No alternative text provided!!")
    else:
        # Printing alt text
        print (image.get('alt'))

print ('')


# Part Four

# Program to print single faculty email
# url = input('Enter UMSI faculty page URL-')
'''
url = 'https://www.si.umich.edu/node/9949'
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html, 'html.parser')

print ("Email of linked faculty")
# Using regex to extract email address and splitting regex into two lines due to length
for email in re.findall('mailto:([a-zA-Z9-9_.+-]+@'
    '[a-zA-Z9-9_.+-]+.[a-zA-Z9-9_.+-]+)', html):
    print (email)
    
print ('')
'''

# Program to print out all emails of directory page
# url_umsi = input('Enter UMSI directory listing URL-')
url_umsi = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=1'
html_umsi = urllib.request.urlopen(url_umsi).read().decode()
soup_umsi = BeautifulSoup(html_umsi, 'html.parser')
lst = []

print ('Emails connected to UMSI directory')
# Finding all anchor tags with the string Contact Details
for url in soup_umsi.find_all('a',string='Contact Details'):
    # Appending new urls to list
    lst.append('https://www.si.umich.edu' + url.get('href'))
for newurl in lst:
    # Accessing new urls
    html2_umsi = urllib.request.urlopen(newurl).read().decode()
    for email in re.findall('mailto:([a-zA-Z9-9_.+-]+@'
        '[a-zA-Z9-9_.+-]+.[a-zA-Z9-9_.+-]+)', html2_umsi):
        print (email)

print ('')

print ('Expected grade: 150/150')


