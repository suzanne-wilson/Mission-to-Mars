# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_hemi():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # initialize dictionary and list
    data_cerberus = {}
    hemi_list = []
#      hemispheres = ['cerberus', 'schiaparelli', 'valles_marineris', 'syrtis_major']
#      hemi_dict = ['data_cerberus', 'data_schiaparelli', 'data_valles_marineris', 'data_syrtis_major']
#      hemi_proper = ['Cerberus', 'Schiaparelli', 'Valles Marineris', 'Syrtis Major']
# 
#    for hemi, title in hemispheres, hemi_proper:
#        # Run all scraping functions and store results in dictionary

    hemisphere_image(browser)
    # hemi_list = hemi_list.append(data_cerberus)
     
    # Stop webdriver and return data
    browser.quit()
    return hemi_list

# go to astropedia and pull 4 images of the hemispheres of Mars
def hemisphere_image(browser):

    # Visit URL
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
    browser.visit(hemi_url)

    # Find the Hemisphere enhanced button and click that
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    image_elem = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    image_elem.click()

    # Find and click the full image button
    wide_image_elem = browser.links.find_by_partial_text('Original')[0]
    wide_image_elem.click()


# Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # img_url_rel = img_soup.find_all('img').get("href")
    # img_url_rel = img_soup.find("wide-image").get("href")
    for link in img_soup.find_all('a'):
        print(link.get('href'))

    # print("img_url_rel")  
    # print(img_url_rel)  

    # img_title = img_soup.find('class')
    # print("img_title")  
    # print(img_title)  
    # Add try/except for error handling
    try:
        # Find the relative image url
        #img_url_rel = img_soup.find_all("wide-image").get("href")
        print(img_url_rel) 
    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced{img_url_rel}'

    title = 'Cerberus Hemisphere Enhanced'
# Run all scraping functions and store results in dictionary
    data_cerberus = {
        "img_url": img_url,
        "title": title
    }
    return data_cerberus, img_url, title

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_hemi())
