import requests
import os

from bs4 import BeautifulSoup
from transformers import pipeline


class DataSources:
    def __init__(self) -> None:
        pass

    # Function to scrape and parse a webpage
    def scrape_website(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Failed to fetch {url}")
            return None

    # Function to use GPT to analyze webpage content
    def analyze_content(self,content):
        gpt_pipeline = pipeline("text-generation")
        analyzed_content = gpt_pipeline(content)
        return analyzed_content

    # Function to identify reliable data sources
    def identify_reliable_sources(self):
        # Provided list of suggested data sources
        suggested_sources = [
            "https://www.ci.richmond.ca.us/1404/Major-Projects",
            "https://www.bakersfieldcity.us/518/Projects-Programs",
            "https://www.cityofwasco.org/311/Current-Projects",
            "https://www.eurekaca.gov/744/Upcoming-Projects",
            "https://www.cityofarcata.org/413/Current-City-Construction-Projects",
            "https://www.mckinleyvillecsd.com/news-and-project-updates",
            "https://www.cityofsanrafael.org/major-planning-projects-2/",
            "https://www.novato.org/government/community-development/planning-division/planning-projects?locale=en",
            "https://www.cityofmillvalley.org/258/Projects",
            "https://riversideca.gov/utilities/projects",
            "https://www.moval.org/cdd/documents/about-projects.html",
            "https://www.coronaca.gov/government/departments-divisions/department-of-water-and-power/construction",
            "http://www.cityofsacramento.org/public-works/engineering-services/projects",
            "https://www.citrusheights.net/292/Current-Projects",
            "https://www.elkgrovecity.org/southeast-policy-area/development-projects",
            "https://www.ci.oceanside.ca.us/government/development-services/engineering/capital-improvement-program/current-projects",
            "https://www.chulavistaca.gov/departments/development-services/city-projects",
            "https://www.ontarioca.gov/Planning/CurrentPlanning",
            "https://www.fontanaca.gov/765/Current-Projects",
            "https://www.sbcity.org/city_hall/community_development_and_housing/development_projects",
            "https://www.atascadero.org/?option=com_content&view=article&id=652&Itemid=1723",
            "https://www.prcity.com/363/City-Projects",
            "https://www.slocity.org/government/department-directory/parks-and-recreation/current-projects"
        ]

        reliable_sources = []

        # Iterate through suggested sources
        for source in suggested_sources:
            # Scrape webpage
            soup = self.scrape_website(source)
            if soup:
                # Use GPT to analyze webpage content
                analyzed_content = self.analyze_content(str(soup))
                # Assess reliability based on GPT analysis
                reliability_score = 0  # Placeholder for now, you can define your own criteria
                if reliability_score >= 0.5:  # Adjust threshold as needed
                    reliable_sources.append({"url": source, "reliability_score": reliability_score})

        return reliable_sources

    # Function to document sources
    def document_sources(self,sources):
        dir = "data_urls"
        if not os.path.exists(dir):
            os.makedirs(dir)

            # Construct the file path
        file_path = os.path.join(dir, "reliable_sources.txt")
        # Create a document or spreadsheet to store the sources
        with open(file_path, "w") as file:
            for source in sources:
                file.write(f"URL: {source['url']}, Reliability Score: {source['reliability_score']}\n")

# Main function
def main():
    # Identify reliable sources
    obj = DataSources()
    reliable_sources = obj.identify_reliable_sources()
    # Document sources
    obj.document_sources(reliable_sources)

if __name__ == "__main__":
    main()
