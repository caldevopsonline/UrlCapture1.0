from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

# Flask initialization
app = Flask(__name__)


# Setting up the route of the application
@app.route('/')
# Function to connect script to HTML interface app.html
def main():
    return render_template('app.html')


@app.route('/capture', methods=['POST'])
def url_capture():
    if request.method == 'POST':
        return render_template()


# Begin application running process
if __name__ == '__main__':
    app.debug = True
    app.run()
