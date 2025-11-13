thonimport os
import json
import requests
from datetime import datetime

def fetch_reviews(app_id, country_code, max_results=200):
    base_url = f"https://itunes.apple.com/{country_code}/rss/customerreviews/id={app_id}/json"
    params = {
        'limit': max_results,
        'country': country_code
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    return response.json()

def parse_reviews(response):
    reviews = []
    for entry in response['feed']['entry']:
        review = {
            'parentId': entry.get('id', {}).get('label'),
            'id': entry.get('id', {}).get('label'),
            'date': entry.get('updated', {}).get('label'),
            'userName': entry.get('author', {}).get('name', {}).get('label'),
            'userUrl': entry.get('author', {}).get('uri', {}).get('label'),
            'version': entry.get('im:version', {}).get('label'),
            'score': int(entry.get('im:rating', {}).get('label', 0)),
            'title': entry.get('title', {}).get('label'),
            'text': entry.get('content', {}).get('label'),
            'url': entry.get('link', {}).get('href'),
            'country': response.get('country', ''),
            'appId': entry.get('id', {}).get('label')
        }
        reviews.append(review)
    return reviews

def save_reviews(reviews, output_file):
    with open(output_file, 'w') as file:
        json.dump(reviews, file, indent=4)

if __name__ == "__main__":
    app_id = "835599320"
    country_code = "US"
    output_file = "reviews_output.json"
    
    response = fetch_reviews(app_id, country_code)
    reviews = parse_reviews(response)
    save_reviews(reviews, output_file)
    print(f"Saved {len(reviews)} reviews to {output_file}")