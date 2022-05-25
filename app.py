

# To check if a website allows web scraping or not you can use status_code as follows:

# import requests

# from bs4 import BeautifulSoup 

# r=requests.get(" ENTER URL OF YOUR CHOICE")

# r.status_code

# The output to this should be 200. Anything other than 200 means that the website your trying to scrape either does not allow web scraping or allows partially.

# https://getsongbpm.com/api

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_data():
    return render_template('index.html')