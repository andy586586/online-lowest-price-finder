from flask import Flask, request, render_template,jsonify
from bs4 import BeautifulSoup
import requests
import re



app = Flask(__name__)
