
from flask import Flask, request, render_template
from flask import Flask, request, render_template,jsonify
from bs4 import BeautifulSoup
import requests
import re



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')


def output(sold_good):
def websearchfunc(sold_good): #function to webscrape
    url = f"https://www.newegg.ca/p/pl?d={sold_good}&N=4131"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    document = BeautifulSoup(page, "html.parser")

    page_text = doc.find(class_="list-tool-pagination-text").strong
    page_text = document.find(class_="list-tool-pagination-text").strong
    pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
    # tested, working correctly: print(pages)

def output(sold_good):
    for page in range(1, pages + 1):
        url = f"https://www.newegg.ca/p/pl?d={sold_good}&N=4131&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        document = BeautifulSoup(page, "html.parser")

        div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
        div = document.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
        #looking for each item that can be bought
        items = div.find_all(text=re.compile(sold_good))

def output(sold_good):
            if parent.name != "a":
                continue

            link = parent['href']
            hyperlink = parent['href']
            next_parent = item.find_parent(class_="item-container")
            try:
                price = next_parent.find(class_="price-current").find("strong").string
                items_found[item] = {"price": int(price.replace(",", "")), "link": link} 
                items_found[item] = {"price": int(price.replace(",", "")), "link": hyperlink} 
            except:
                pass
            #tested, working properly, print(item)
def output(sold_good):
    #processing a dictionary:
    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

    for item in sorted_items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-----------------------------")




    # MAKE THE PAGE REDIRECTUSING FLASK TO AN HTML PAGE WITH ALL THE OUTPUT
    out = []
    for item in sorted_items:
        item_name = str(item[0])
        item_price = str(f"${item[1]['price']}")
        item_link = str(item[1]['link'])
        out.append(" Item: " + str(item_name) + " Price: " + str(item_price) + " Link: " + str(item_link) + " ")

    return out





@app.route('/', methods=['POST'])
def intake_and_output(text1):
   sold_good = text1
   output = websearchfunc(sold_good) 
   return output
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    sold_good = request.form['variable']
    output(sold_good)



    app.run(host='localhost', port=5000)


    text1 = request.form['text1']
    word = request.args.get('text1')
    output = intake_and_output(text1)
    result = {
        "output": output
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
        app.run()








    app.run(debug=True, host='0.0.0.0', port=5000)
