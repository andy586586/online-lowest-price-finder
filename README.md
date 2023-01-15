# Online lowest-price-finder for products

## Welcome to a Python based web-scraping application that parses and scrapes common online sites to find the lowest price of purchasable products!

### Description:
This web application that allows a user to search for the lowest price of electronics online was made using Python, HTML5, CSS, Javascript, Flask, JSON. It uses a python back-end to parse and web-srape for a specfic key-word that the user inputs 

### Features:
+ Search Bar for User's Desired Input
+ Configured to output a 10-item list to display possible choices
+ List items contain Product name, Price, Link and Additional Information

### Process:
I spent many hours tinkering with the concept of web-scraping before figuring out how to extract code from HTML and processing it in python. Many thanks to W3Schools, FreeCodeCamp.org, Programming with Mosh, Python Documentation and other youtubers/developpers for helping me understand how to use and understand Beautifulsoup, and other python syntax/algorithmic processes.

Now that I figured out how to do the backend web-scraping and filtering for the desired product, I had to connect this output data to the front end HTML page.








One of the larger problems was when the JSON output would become scrambled and the text would appear as a giant wall of random characters. I've attached an image to show you what it was like.

![image](https://user-images.githubusercontent.com/111328484/212561981-d95c166a-3ea5-4ee5-b427-29f2055d32da.png)


To counteract this, I debugged and implemented a new integration of the Python server-side output through the JSON, which would output HTML in a cleaner fashion. The output would now look like this:

![image](https://user-images.githubusercontent.com/111328484/212563812-d9d96155-bddc-464a-b778-32da66552220.png)

### Further fixes and tasks for this project:
+ Add better CSS to make it more visually appealing
+ Next-word predictor for the search bar based on the user's previous



### Legal Disclaimer:
This project was made so that I could practice passing front-end user input to back-end processes and sending processed data out to the front end, as an HTML/CSS refresher and get some practice with sorting relatively small amounts of publicly available data. Web scraping for publicly availible information is used widely by companies and developpers alike (evidence of this is all over the internet), though some say it is a legal gray area. However, I did not actually use this web-scraping program for for financial gain, I only used it for testing and learning purposes. Please engage in legal, responsible and ethical practices if you are consulting this repository, and I am not responsible for any consequences of anyone using this public repository or information gained from this public repository to commit crimes or copyright violations. For example, a site like Newegg uses various security measures to stop third-party bots and such from scraping their website for public data such as products and prices. Please don't try to circumvent these measures as they are protected by the site's terms of service (and maybe other documents).



