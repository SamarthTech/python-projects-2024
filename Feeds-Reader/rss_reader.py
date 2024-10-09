import feedparser
import datetime
import webbrowser

FEEDS = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://www.reddit.com/r/news/.rss"
]

def parse_feeds(feeds):
    news_items = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            news_items.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.get('published', 'No date'),
                'source': feed.feed.title
            })
    return news_items

def display_news(news_items):
    for i, item in enumerate(news_items, 1):
        print(f"{i}. {item['title']}")
        print(f"   Source: {item['source']}")
        print(f"   Published: {item['published']}")
        print(f"   Link: {item['link']}")
        print()

def main():
    news_items = parse_feeds(FEEDS)
    news_items.sort(key=lambda x: x['published'], reverse=True)
    
    while True:
        display_news(news_items)
        
        choice = input("Enter the number of the article to open (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        
        try:
            article_index = int(choice) - 1
            if 0 <= article_index < len(news_items):
                webbrowser.open(news_items[article_index]['link'])
            else:
                print("Invalid article number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    main()