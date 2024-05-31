import mechanize
from bs4 import BeautifulSoup

def scrape_college_links() -> None:
    """
    Scrapes and saves full URLs of college links from the SLU catalog programs page.
    This function specifically looks for links under the '/colleges-schools/' path,
    appends a fragment '#requirementstext' to each link, and writes them to a text file.
    """
    # Setup the browser
    br = mechanize.Browser()
    br.set_handle_robots(False)  # Ignore robots.txt
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Open the target webpage and read the HTML
    response = br.open('https://catalog.slu.edu/programs/')
    html = response.read()

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)

    # Prepare to write links to a file
    file_path = 'full_college_links.txt'
    base_url = 'https://catalog.slu.edu'

    # Write full URLs to a file
    with open(file_path, 'w', encoding='utf-8') as f:
        for link in links:
            href = link['href']
            if href.startswith('/colleges-schools/'):
                full_url = base_url + href + '/#requirementstext'
                text = link.get_text(strip=True)
                f.write(f"{full_url}, {text}\n")

    print(f"Full links have been successfully written to {file_path}.")

if __name__ == "__main__":
    scrape_college_links()
