
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_university_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Add specific scraping logic based on website structure
    return {
        "university_name": "Example University",
        "country": "Country",
        "city": "City",
        "website": url
    }

def scrape_courses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = []
    # Add specific scraping logic here
    return courses

def main():
    university_urls = [
        "https://www.harvard.edu",
        "https://www.stanford.edu",
        "https://www.ox.ac.uk",
        "https://www.utoronto.ca",
        "https://www.unimelb.edu.au"
    ]
    
    universities = []
    courses = []
    
    for idx, url in enumerate(university_urls, start=1):
        uni_id = f"U{idx:03d}"
        uni_info = scrape_university_info(url)
        uni_info["university_id"] = uni_id
        universities.append(uni_info)
        
        scraped_courses = scrape_courses(url)
        for c_idx, course in enumerate(scraped_courses, start=1):
            course["course_id"] = f"C{idx:03d}{c_idx:02d}"
            course["university_id"] = uni_id
            courses.append(course)
    
    df_universities = pd.DataFrame(universities)
    df_courses = pd.DataFrame(courses)
    
    with pd.ExcelWriter("University_Course_Data.xlsx") as writer:
        df_universities.to_excel(writer, sheet_name="Universities", index=False)
        df_courses.to_excel(writer, sheet_name="Courses", index=False)

if __name__ == "__main__":
    main()
