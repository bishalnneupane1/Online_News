from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

# Initiate Flask Start
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
# Initiate Flask End

# Defining a Function
def index():

        # Data Preparation Start
        url = "https://www.gadgetbytenepal.com/blog-news-list/"
        req = requests.get(url)
        soup = BeautifulSoup(req.content,"html.parser")
        outerdata = soup.find_all("div",class_="td_module_10 td_module_wrap td-animation-stack",limit=6)
        finalNews=""
        # Data Preparation End

        # Main Logic Start
        for data in outerdata:
            news = data.div.a["title"]
            finalNews += "\u2022" + news + "\n"
        return render_template("index.html",News=finalNews)
        # Main logic End

        #To run the code type "flask run" in terminal