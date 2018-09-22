from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests

def init():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    mars_data = {}

    # Stop webdriver and return data
    #browser.quit()
    # return data
    return mars_data


def scrape():
    browser = init()
    mars_dict = {}

# ## NASA Mars News

    # Mars News URL
    url = "https://mars.nasa.gov/news/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get title & description
    news_title = soup.find('content_title').text
    news_p = soup.find('article_teaser_body').text

    # Adding to dict
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    # return news_title, news_p
    return(news_title)
    return(news_p)
    print(news_title)

# JPL Mars URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through the pages
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get featured image
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    mars_dict["featured_image_url"] = featured_image_url

    print("FEATURED IMAGE ACQUIRED")


# ## Mars Weather

    # Twitter API Keys
    consumer_key = "IqqOcoOSlCxcEUAuZQY1Kb02L"
    consumer_secret = "4ISKPBgy56BXsp7a8Ja639ToJ9xhjeAya13yg3bRU7wnfkL9f3"
    access_token = "922955283172876289-OK82xypOTTZsmZnsG2sxZxjVC9wlymW"
    access_token_secret = "zyJNP5AaGcAuKuKiNEWiUwiBccWdEWrMawvksujYJigq3"
    # Use Tweepy to Authenticate our access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Target User
    target_user = "@MarsWxReport"

    # Get tweet
    tweet = api.user_timeline(target_user, count=1)[0]

    # Store weather
    mars_weather = tweet['text']

    mars_dict["mars_weather"] = mars_weather

    print("WEATHER ACQUIRED")


# ## Mars Facts

    # Mars Facts URL
    url = "https://space-facts.com/mars/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Empty dictionary for info
    mars_profile = {}

    # Get info
    results = soup.find('tbody').find_all('tr')

    # Storing profile information
    for result in results:
        key = result.find('td', 'column-1').text.split(":")[0]
        value = result.find('td', 'column-2').text
        
        mars_profile[key] = value
        
    # Creating a DataFrame
    profile_df = pd.DataFrame([mars_profile]).T.rename(columns = {0: "Value"})
    profile_df.index.rename("Description", inplace=True)

    # Converting to html
    profile_html = "".join(profile_df.to_html().split("\n"))

    # Adding to dictionary
    mars_dict["profile_html"] = profile_html

    print("FACTS ACQUIRED")


# ## Mars Hemispheres

    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Empty list of image urls
    hemisphere_image_urls = []



    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']
    valles_title = "Valles Marineris Hemisphere"
    # Create dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(valles_marineris)



    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']
    cerberus_title = "Cerberus Hemisphere"
    # Create dictionary
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(cerberus)



    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']
    schiaparelli_title = "Schiaparelli Hemisphere"
    # Create dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(schiaparelli)



    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    syrtis_link = soup.find('div', 'downloads').a['href']
    syrtis_title = "Syrtis Major Hemisphere"
    # Create dictionary
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(syrtis_major)

    # Adding to dictionary
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

    print("HEMISPHERE IMAGES ACQUIRED")
    print("----------------------------------")
    print("SCRAPING COMPLETED")

    return mars_dict


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape())
