Web Scraping is a technique to simulate the behavior of a website user to effectively
use the website itself as a web service to retrieve data. Scraping can gather data/information
from World Wide Web and you can get data as per your requirements. Investors need to have
comprehensive data of similar companies and their corresponding stock values which appear
in the stock market every day. Web Scraper software can be used to keep a constant watch on
this data. You can get all the required information from a financial source at the click of a
button.
In this project, we scraped financial data from a financial website. The scraped data is
parsed using the Beautiful soup object. The extracted information is emailed in the form of a pie chart
and used by investors for analysis.

Language used: Python

Project Specifications:
* Identify a website which you want to scrape
* Identify patterns in URL and inspect objects
* Take input in a file as with every addition of ticker symbol we don’t have to change
code
* Use your Gmail account to send email
* Email body should contain stock symbols and its current price in the form of pie-
chart.
* Subject should be: “Stock Report”
* Mail should go with proper ‘From’ name and not with email id
* To should have a recipient mail address

Libraries used:
* Requests
* Beautiful soup
* Urllib.request
* Smtplib
* Csv
* Email
* Matplotlib


Execution Process:
1. Provide the input stock symbols in the csv format.
    Note: Only stock symbols should be given Eg: GOOG for Google
2. In the code enter the credentials details
    From address and To address.
    Note: For from address you need to specify the login credentials
3. The output will be shown in the pie chart file in PNG format.

