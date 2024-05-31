import mechanize
from bs4 import BeautifulSoup

def scrape_course_links() -> None:
    """
    Scrapes and saves URLs related to course listings from the SLU catalog website.
    The function navigates to the 'Courses A-Z' section and extracts links that start
    with '/courses-az', then writes these links and the text descriptions to a file.
    """
    # Initialize mechanize browser
    br = mechanize.Browser()
    br.set_handle_robots(False)  # Ignore robots.txt

    # Open the main catalog page and follow the link to 'Courses A-Z'
    br.open("https://catalog.slu.edu/")
    br.follow_link(text_regex=r"(?i)courses a-z", nr=0)  # Navigate to courses-az section

    # Double-check navigation success
    response = br.follow_link(text_regex=r"(?i)courses a-z", nr=0)
    print(f"Title of the page: {br.title()}")
    print(f"URL of the page: {response.geturl()}")

    # Collect links that are relevant to courses
    majors = {link.text: link for link in br.links() if link.url.startswith("/courses-az")}

    # Print collected majors to verify
    print("Majors found:", majors.keys())

    # Write the relevant links to a file
    with open('major_links.txt', 'w', encoding='utf-8') as f:
        for text, link in majors.items():
            f.write(f"{link.url}, {text}\n")

    print("Links have been successfully written to major_links.txt.")

if __name__ == "__main__":
    scrape_course_links()





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