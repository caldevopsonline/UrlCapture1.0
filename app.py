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


# Initialise a connection for submitting data
@app.route('/capture', methods=['POST'])
def url_capture():
    # Call form input field from app.html
    if request.method == 'POST':
        web_url = request.form['weburl']

        # Capture and Concatenate web address with HTTPS Prefix
        url_data = requests.get("https://www." + web_url + "/")

        # Initialise data fetching process with the help of BeautifulSOup Library
        fetch_data = BeautifulSoup(url_data.content, 'html.parser')
        return render_template()


# Begin application running process
if __name__ == '__main__':
    app.debug = True
    app.run()
