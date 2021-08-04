# UrlCapture1.0

# Overview
This is a simple flask application that allows users to enter a url from HTML user interface and get a response that retrieves data from the web address. The the data captured is displayed to the user and a copy of the data is saved as txt file.The project has been deployed in localhost, Azure Devops and Amazon Beanstalk.

# Project Links
1. Azure DeVops :    https://webscraper-app.azurewebsites.net
2. Amazon Beanstalk: http://flaskupdate-env.eba-ki2hcsgk.us-east-1.elasticbeanstalk.com/

# Video Demo Links 
 https://drive.google.com/file/d/10idWZspb1Keg0ql9Xk2KVFL-CXPx484a/view
# Installation
Installing dependencies, run the following command 
1. pip install bs4
2. pip install requests
3. pip install flask

# Running in Localhost
flask command ===>> flask run

# Running Project as a Docker Container
1. Creating Dockerile in project directory (Script in Repo)

2. Creating docker-compose.yml file in project directory (Script in repo)

3. In the terminal run command ===>> docker-compose up
4. Check the generated localhost connection in the format HostIP:Port_number(http://172.20.0.2:5000/)

# Deploying Project to Azure Devops
 1. Create a resource group and subscription on azure(https://portal.azure.com/)
 2. Create a new resource as web app and configure it with the already created resource group abd subscription
 Hint: YOu can choose to deploy your project as code or Container
 NB: It might sometimes take extra minutes to have your configuration fully functioning
 3. login into free tier account on azure devops and create a new project(https://dev.azure.com/)
 NB: Your portal account and azure devops dev.azure account much have same user credentials. This is to
 ensure that the resource group, subscription and web app can reflect in the pipline setup process
 4. Create a new pipeline
 5. select the project from azure repo or github repo.
 6. Configure the pipeline with the your subscription and web app name.
 7. Perform a build and deploy process.
 8. Test url link for web app to view project running on azure
# Running Automated Test Suite
The project contains a test script that test the function _URL_CAPTURE() in app.py. The SENND() function is responsible for reading user input and capturing data from url using BeautifulSoup library and request. The test suit is made of a test_app.py and conftest.py. To run this, use the command--> pytest

# Deploying Project to Amazon BeanStalk
 1. Rename app.py to application.py
 2. zip the following files and folders together
  .ebextensions
  application.py
  requirement.txt
  templates
 3. On AMazon Web service, search for Elastic Beanstalk
 4. Create a bew Virtual environment
 5. Upload the zip file to the virtual environment to replace the default sample page.
# Using Github Action for Continuous Integration
This repo has a continuous integration enabled from the Actions panel. Each time a commit is made, a continous integration process is triggered to build the project and also provides an alert when a bug is found.

# Using a Post method and Request
The flask application makes use python HTTP request library and  Post method. The post method is linked to the path '/capture' which captures the data from the input field and sends an HTTP get request to the intended URL. 

