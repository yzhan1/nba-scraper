# hupu-scraper

Simple flask application that scrapes all the news titles on HUPU's NBA section.

Utilized Redis task queue to handle the scraping

+ User can download the scraped data as JSON file and use them for NLP training.

+ To run the app:

    +  Download the folder
    
    +  Install packages in requirement.txt using ```pip3 install```
    
    +  Run ```python3 app.py```

+ API route for corpus data in JSON format: ```/get-json```

+ Live at: https://powerful-cove-80847.herokuapp.com/
