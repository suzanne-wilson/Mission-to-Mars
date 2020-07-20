# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_hemi():
    global hemi_list
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # initialize dictionary and list
    hemi_list = []
#      hemispheres = ['cerberus', 'schiaparelli', 'valles_marineris', 'syrtis_major']
#      hemi_dict = ['data_cerberus', 'data_schiaparelli', 'data_valles_marineris', 'data_syrtis_major']
#      hemi_proper = ['Cerberus', 'Schiaparelli', 'Valles Marineris', 'Syrtis Major']
# 
#    for hemi, title in hemispheres, hemi_proper:
#        # Run all scraping functions and store results in dictionary

    hemisphere_image(browser)

    # Stop webdriver and return data
    browser.quit()
    return hemi_list

# go to astropedia and pull 4 images of the hemispheres of Mars
def hemisphere_image(browser):
    global hemi_list
    # Visit URL
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
    browser.visit(hemi_url)

    def hemi( plain, proper, forlist ):
        
        # Find the Hemisphere enhanced button and click that
        browser.is_element_present_by_text(f'{proper} Hemisphere Enhanced', wait_time=1)
        image_elem = browser.links.find_by_partial_text(f'{proper} Hemisphere Enhanced')
        image_elem.click()

        # Find and click the full image button
        wide_image_elem = browser.links.find_by_partial_text(f'{plain}_enhanced.tif')[0]
        wide_image_elem.click()


    # Parse the resulting html with soup
        html = browser.html
        img_soup = soup(html, 'html.parser')
        
        img = img_soup.find('div', id="wide-image")
        img_url_rel = img.find('img', class_="wide-image").get('src')
    
        img_title = img_soup.find('h2', class_='title').get_text()
        print("img_title")  
        print(img_title)  
        # Add try/except for error handling
        try:
            # Find the relative image url
            print("img_url_rel")  
            print(img_url_rel)

        except AttributeError:
            return None

        # Use the base url to create an absolute url
        img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
        print("img_url")
        print(img_url)
        
    # Run all scraping functions and store results in dictionary
        forlist = {}
        forlist = {
            "img_url": img_url,
            "title": img_title
        }

        return forlist

    hemi(plain="cerberus", proper="Cerberus", forlist="dic1")
    hemi_list = hemi_list.append(dic1)
    print("hemi_list") 
    print(hemi_list)     

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_hemi())
