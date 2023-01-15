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


To counteract this, I debugged and implemented a new integration of the Python server-side output through the JSON, which would output HTML in a cleaner fashion. The output would now look like this:


