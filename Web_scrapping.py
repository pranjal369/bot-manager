import requests
from bs4 import BeautifulSoup
import csv

# Replace this URL with the webpage you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

   
    article_titles = soup.find_all('h2', class_='title')

    # Create and open a CSV file to write the data
    with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Article Titles'])  # Write header

        # Extract the text from the elements and write to the CSV file
        for title in article_titles:
            writer.writerow([title.get_text()])

    print("Data has been successfully scraped and saved to 'scraped_data.csv'.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
