# UrlCapture1.0

# Overview



# Installation

Installing dependencies, run the following command 
pip install bs4
pip install requests
pip install flask

# RUnning in Localhost
flask command ===>> flask run


#Running Project as a Docker Container
1. Creating Dockerile in project directory (Script in Repo)

2. Creating docker-compose.yml file in project directory (Script in repo)

3. In the terminal run command ===>> docker-compose up
4. Check the generated localhost connection in the format HostIP:Port_number(http://172.20.0.2:5000/)

#Deploying Project to Azure Devops
 1. Create a resource group and subscription on azure(https://portal.azure.com/)
 2. Create a new resource as web app and configure it with the already created resource group abd subscription
 Hint: YOu can choose to deploy your project as code or Container
 NB: It might sometimes take extra minutes to have your configuration fully functioning
 3. login into free tier account on azure devops and create a new project(https://dev.azure.com/)
 NB: Your portal account and azure devops dev.azure account much have same user credentials. This is to
 ensure that the resource group, subscription and web app canreflect in the pipline setup process
 4. 

#Deploying Project to Amazon BeanStalk
 1. Rename app.py to application.py
 2. zip the following files and folders together
  .ebextensions
  application.py
  requirement.txt
  templates
 3. On AMazon Web service, search for Elastic Beanstalk
 4. 

