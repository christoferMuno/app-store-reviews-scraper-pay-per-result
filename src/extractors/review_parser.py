thonimport json

def parse_review_data(data):
    parsed_data = []
    for review in data:
        parsed_review = {
            'id': review['id'],
            'user': review['userName'],
            'score': review['score'],
            'title': review['title'],
            'content': review['text'],
            'date': review['date'],
            'app_id': review['appId'],
            'country': review['country'],
            'url': review['url']
        }
        parsed_data.append(parsed_review)
    return parsed_data