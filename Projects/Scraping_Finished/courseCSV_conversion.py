from bs4 import BeautifulSoup
import pandas as pd
import mechanize

# Function to scrape course data for a given link
def scrape_course_data(major_link):
    # Initialize mechanize browser
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Open the course page
    base_url = "https://catalog.slu.edu"
    link = base_url + major_link
    br.open(link)
    html = br.response().read()
    soup = BeautifulSoup(html, "html.parser")

    # Find all course blocks
    course_blocks = soup.find_all("div", class_="courseblock")

    # Initialize list to store course data
    courses_data = []

    # Extract data from each course block
    for block in course_blocks:
        course_title = block.find("p", class_="courseblocktitle noindent")
        credits = block.find("p", class_="courseblockextra noindent")
        
        # Find prerequisite information
        prerequisites = "NaN"
        concurrent_enrollment = "NaN"

        for extra in block.find_all("p", class_="courseblockextra noindent"):
            if extra.find("strong") and "Prerequisite(s):" in extra.find("strong").text:
                prereq_links = extra.find_all("a")
                prereqs = [link.text.strip() for link in prereq_links]
                prerequisites = ', '.join(prereqs)
                
                # Check for concurrent enrollment info
                sup_tags = extra.find_all("sup")
                for sup in sup_tags:
                    if sup.next_sibling and "Concurrent enrollment allowed." in sup.next_sibling:
                        concurrent_enrollment = "Concurrent enrollment allowed."
                        break
                break

        courses_data.append({
            'Course Title': course_title.text.strip() if course_title else 'NaN',
            'Credits': credits.text.strip() if credits else 'NaN',
            'Prerequisites': prerequisites,
            'Concurrent Enrollment': concurrent_enrollment
        })

    return courses_data

# Read the major links from the file
major_links_file = 'major_links.txt'
with open(major_links_file, 'r') as file:
    lines = file.readlines()

# Initialize a list to store all courses data
all_courses_data = []

# Process each major link
for line in lines:
    major_link, major_name = line.strip().split(', ', 1)
    major_courses_data = scrape_course_data(major_link)
    
    # Add major name to each course entry
    for course in major_courses_data:
        course['Major'] = major_name
    
    all_courses_data.extend(major_courses_data)

# Convert the combined data to a DataFrame
all_courses_df = pd.DataFrame(all_courses_data)

# Save the DataFrame to a CSV file
csv_filename = "all_slu_courses.csv"
all_courses_df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")
