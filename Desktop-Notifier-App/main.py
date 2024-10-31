import requests
import xml.etree.ElementTree as ET

# URL of news RSS feed
RSS_FEED_URL = "https://www.hindustantimes.com/feeds/rss/editors-pick/rssfeed.xml"

def loadRSS():
    ''' 
    Utility function to load RSS feed with headers to avoid access restrictions
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Create HTTP request response object with headers
    resp = requests.get(RSS_FEED_URL, headers=headers)

    # Print the raw content to ensure we are getting a valid response
    print("RSS Feed Content:", resp.content[:500])  # Print the first 500 characters for brevity

    # Return response content
    return resp.content

def parseXML(rss):
    ''' 
    Utility function to parse XML format RSS feed 
    '''
    # Create element tree root object
    root = ET.fromstring(rss)

    # Create empty list for news items
    newsitems = []

    # Iterate news items
    for item in root.findall('./channel/item'):
        news = {}

        # Iterate child elements of item
        for child in item:
            # Special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text
        newsitems.append(news)

    # Print parsed news items for debugging
    print("Parsed News Items:", newsitems[:5])  # Print first 5 news items

    # Return news items list
    return newsitems

def topStories():
    ''' 
    Main function to generate and return news items 
    '''
    # Load RSS feed
    rss = loadRSS()

    # Parse XML
    newsitems = parseXML(rss)

    # Print the top stories for debugging
    print("Top Stories:", newsitems[:5])  # Print first 5 top stories

    return newsitems

# Call the topStories function to test
topStories()
