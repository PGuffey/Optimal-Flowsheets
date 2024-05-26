from bs4 import BeautifulSoup
import pandas as pd
# import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# import re
import mechanize

br = mechanize.Browser()
br.open("https://catalog.slu.edu/")
br.follow_link(text_regex=r"(?i)courses a-z", nr=0) # looks for link to go to courses-az and goes into it

# Testing to make sure it goes through link
response1 = br.follow_link(text_regex=r"(?i)courses a-z", nr=0)
print(br.title())
print(response1.geturl())

majors = {}
for link in br.links():
    if link.url.startswith("/courses-az"):
        majors[link.text] = link
majors = [link for link in br.links() if link.url.startswith("/courses-az")]

print(majors)

with open('major_links.txt', 'w', encoding='utf-8') as f: # writes a link to each major and the major into a file
        for link in br.links(): # mainly wrote into a file to make sure it worked
            if link.url.startswith("/courses-az"):
                f.write(f"{link.url}, {link.text}\n")





# br.set_handle_equiv(True) # sounds like this should be true
# br.set_handle_redirect(True) # follows HTTP redirections // if website page changes location because of web servers
# br.set_handle_referer(True) # security // prob not needed XD SLU
# br.set_handle_robots(False) # nothing sus here... shhhhh... i am ethical.

# # Temp "link" value for testing, should be replaced with a loop of some sort to go through each major link to record data
# link = "https://catalog.slu.edu/courses-az/csci/"
# br.open(link)

# html = br.response().read()
# soup = BeautifulSoup(html, "html.parser")

# course_blocks = soup.find_all("div", class_="courseblock")

# courses_data = []
# for block in course_blocks:
#      course_title = block.find("p", class_="courseblocktitle noindent")
#      credits = block.find("p", class_="courseblockextra noindent")
#     #  prerequisites = block.select('p:has(strong.Prerequisite)')
#      prerequisites = block.find("a", class_="courseblockextra noindent") # doesnt work
     

#      courses_data.append({
#                 'Course Title': course_title,
#                 'Credits': credits,
#                 'Prerequisites': prerequisites
#             })

# print(courses_data)
# # create a for loop that loops through eachblock and extracts the course title, credts, prerequisite(s), and restrictions and attributes if they have them, else enter NaN
# # interesting cases include CSCI 4830 where its "offered occasionally"
# # CSCI 4961 where the prereqs arent accurate andgrad classses