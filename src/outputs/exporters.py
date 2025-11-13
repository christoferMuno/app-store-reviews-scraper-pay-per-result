thonimport json

def export_reviews_to_json(reviews, output_filename):
    with open(output_filename, 'w') as f:
        json.dump(reviews, f, indent=4)

def export_reviews_to_csv(reviews, output_filename):
    import csv
    keys = reviews[0].keys()
    with open(output_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(reviews)