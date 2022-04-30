from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome(executable_path=r"C:\Users\Salma4391\Desktop\c126ws\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    # planet_data would be to save all the details of the planet. We will 
    # create a csv from these lists. Now, let’s just try to scrape the 
    # first page only. Before we do that, let’s inspect the page. We can 
    # see that all the rows in the table are ul tags with class as exoplanet .
    for i in range(0, 201):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #Earlier, the chrome window we opened with Selenium, we named it
        # as browser. Now, we are creating a BeautifulSoup object where we 
        # are passing the browser’s page source and asking our bs4 to use 
        # html.parser in it, which means it will read the page as an HTML.
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()