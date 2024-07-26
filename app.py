from flask import Flask, request, render_template,jsonify
from bs4 import BeautifulSoup
import requests
import re



app = Flask(__name__)



def websearchfunc(sold_good): #function to webscrape and pass the final_result on to the @app.route
    url = ""
    page = requests.get(url).text
    document = BeautifulSoup(page, "html.parser")

    page_text = document.find(class_="list-tool-pagination-text").strong
    pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
    # tested, working correctly: print(pages)


    #making a dictionary to store the results of searching for the sold_good name, link and price
    items_found = {}


    #loops through to get every page of the search result on the website
    for page in range(1, pages + 1):
        url = ""
        page = requests.get(url).text
        document = BeautifulSoup(page, "html.parser")
        
        div = document.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
        #looking for each item that can be bought
        items = div.find_all(text=re.compile(sold_good))

        for item in items:
            parent = item.parent
            if parent.name != "a":
                continue

            hyperlink = parent['href']
            next_parent = item.find_parent(class_="item-container")
            try:
                price = next_parent.find(class_="price-current").find("strong").string
                items_found[item] = {"price": int(price.replace(",", "")), "link": hyperlink} #replaces the , in price with nothing
            except:
                pass
            #tested, working properly, print(item)
    #another dictionary which contains the price and link as another value, and letting the key be the sold_good searched for



    #processing a dictionary:
    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# this creates an array called out that can store all of these values
    out = []
    for item in sorted_items:
        item_name = str(item[0])
        item_price = str(f"${item[1]['price']}")
        item_link = str(item[1]['link'])
        out.append(str(" Item: " + str(item_name) + "<br> Price: " + str(item_price) + "<br> Link: " + str(item_link) + " "))

 
# now using this array we can make everything a string, and output all the strings joined together using spaces and line breaks
    first10OutString = map(str, out[:10])
    top_10="<br><br> ".join(first10OutString)


    return top_10




# converting to json, while also taking in the HTML user input
def intake_and_output(text1):
   sold_good = text1
   output = websearchfunc(sold_good) 
   return output
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    output = intake_and_output(text1)
    print(output)
    result = {
        "output": output
        
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
