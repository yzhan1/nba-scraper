# hupu-scraper

Simple flask application that scrapes all the news titles on HUPU's NBA section.

Utilized Redis task queue to handle the scraping

+ User can download the scraped data as JSON file and use them for NLP training.

+ To run the app:

    +  Download the folder
    
    +  Install packages using ```pip3 install -r requirements.txt```
    
    +  Run ```python3 app.py``` and visit 0.0.0.0/5000

+ API route for corpus data in JSON format: ```/api/get-json```
