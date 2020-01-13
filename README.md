# Randomised Band Generator App

## Quick Links
Jenkins: http://35.197.206.61:8080

Webapp: http://34.89.67.13/home

Coverage Reports:
- http://34.89.67.13/home/coveragereport
- http://34.89.67.13/service2/coveragereport
- http://34.89.67.13/service3/coveragereport
- http://34.89.67.13/service4/coveragereport

## Functionality
This app is a basic Flask-based web app that produces randomised band information at the click of a button, i.e.:
* Band name
* Genre
* Band members
* Popularity score
* Pretentiousness score

![gui][gui]

If the pretentiousness score is above a certain level (currently set to 50) it will begin to randomly accent vowels in the band name and the names of its members, in the vein of Motörhead's superfluous umlaut over the second 'o'. That's pretty much it for the app.

### App Structure
![appstructure][appstructure]

The app is made up of five distinct services:
- NGINX:
   NGINX is a web server that can handle load balancing and reverse proxies. It allows users to connect to the service over HTTP on port 80 and redirects the requests to the appropriate services on the machines local network to their specific ports, such as 5000 for the Flask services in this application. Its functionality is dictated by the `nginx.conf` file in the 'nginx' directory in this repo.

- Service 1:
   Functions as the server that renders the HTML templates, submit form and GET requests to the other services in the system. When the **Generate Band** button is pressed, the server sends a GET request to Service 4, which will response with a JSON object containing the randomised band information. The server will then display this to the user.

- Service 2:
   Generates a band name and the genre that the band plays.

- Service 3:
   Generates numerical statistics about the band: the number of members it has, its popularity score and its pretentiousness score.

- Service 4:
   After receiving a GET request from Service 1 (the server), Service 4 makes two more GET requests to Services 2 & 3. Once it has received these two requests, it uses the number of members value to generate that many names and the pretentiousness value to dictate whether to randomly accent vowels in the band name and the band members' names. Once it has done this it returns these values in a JSON package to the server.

## Installation Instructions
### Requirements:
* Installation of Ansible on your machine (instructions can be found here: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* Create two GCP instances called bg-jenkins-2 and bg-swarm-manager
   * bg-jenkins-2 MUST be running Ubuntu 16+ or other Linux machine capable of using Python 3.6 or above – Debian 9 is currently only compatible with Python 3.5.3 which will cause issues when running Pytest due to f-string interpolation only being introduced in 3.6
* Edit the ansible/inventory file to include the IP addresses of your Jenkins VM and Swarm Manager VM
* Creation of a .env file containing the following environmental files that will allow your app to connect the SQL database you have creates:
   * MYSQL_USER=(your MySQL instance user)
   * MYSQL_PASSWORD=(your MySQL instance password)
   * MYSQL_URL=(the URL to your MySQL instance)
   * MYSQL_DATABASE=(name of the database)
   * MYSQL_SECRETKEY=(a randomised secret key)

### Installation
1. Open Terminal
2. Fork this repository and git clone it to your machine `git clone https://github.com/your-username/band_generator`
3. Change the directory to ansible folder in the cloned repo `cd ~/YOUR-PATH/band_generator/ansible`
4. Run Ansible `ansible-playbook -i inventory _all`
5. Copy the Jenkins Initial Admin Password, which will be found in the 'debug' TASK proceeding the 'Initial admin password' TASK

![initadminpass][initadminpass]

6. In your browser, navigate to the public IP of your bg-jenkins-2 machine on port 8080, e.g. 34.234.12.9:8080
7. Paste the initial admin password when prompted and install recommended plugins
8. Create a new Pipeline job called 'staging' 
   * Under **Build Triggers** tick 'GitHub hook trigger for GITScm polling'
   * Setup a webhook on your forked repository on GitHub
   * Under **Pipeline**, set the following:
      * *Definition* to 'Pipeline script from SCM'
      * Paste the repository URL into the *Repository URL* box
      * *Script Path* to jenkins/Jenkinsfile
   * Press **Save**
9. To deploy the app, either press Build on the Jenkins job or make a commit to the git repository
10. Navigate to the public IP for bg-swarm-master followed by /home (e.g. 35.24.124.1/home) to use the app

## System Structure
![cd][cd]

Pictured above is the development and deployment pipeline. It consists of the following elements:

### Ansible
Ansible is a configuration automation tool used to easily install and configure all the tools and dependencies on each machine in the system. It runs on the concept of idempotency, meaning that running it will cause each system to revert back to its original state should an issue arise. It is run from a single control machine outside of the deployment pipeline.

### Jenkins
![jenkins][jenkins]

### Docker
Docker is a collection of 'platform as service' tools that are used to containerise applications in lightweight OS environments. These containers can be saved as images and stored in registries. This allows each iteration of the application run on any system because all its dependencies are contained within the Docker container.

### Docker Compose
Docker Compose is an additional module for Docker that allows you to easily build and run multiple containers at once on the same network. These are configured using `docker-compose.yaml` files. In this system, Jenkins runs this to build the images of each of the services to be saved in the local private registry on the machine.

### Docker Swarm
Docker also has a collection of deployment functionalities that allow for seamless continuous deployment and easy replication of services across machines. Docker Swarm handles the replication of services (collections of containers) such that machine may be running many of the same service. For web apps such as our Band Generator App, this means that multiple users can be using different dedicated replicas of the same services rather than sharing the same process. It also means that if once service fails, another one is ready to handle the process instead.

Swarm can also orchestrate services across different machines, known as nodes. Nodes can either be Managers or Workers. Managers handle the orchestration (i.e. that's where you control the services) and Workers simply run the services. Manager nodes will automatically replicate services across Workers such that resources are being shared equally between each. It will also automatically rebalance the services if a Worker node goes offline.

### Docker Stack
Docker Stack is a command in Docker that allows you to manage a collection of containers across a Docker Swarm. Simply running `docker stack deploy your-docker-compose.yaml` on a Manager node will deploy your containers across your Swarm with as many replicas as you specify in docker-compose.yaml. Each time you run `docker stack deploy`, Stack will update each container with the image version you've specified (e.g. the latest one) one-by-one, such that each container is pulled down individually and run back up with the updated image while the other containers are left running. This allows updates to be rolled out without interrupting the user experience.

### Testing
pytest is used to run unit tests on the app. The logs for each test can be viewed in the 'staging' job

![testcoverage][testcoverage]

pytest also produces a coverage report to show how much of the code in the app has been successfully tested. Jenkins automatically moves this report to the 'templates' folder so that it can be navigated to in a browser, as shown in the image above. Currently only the most recent coverage report can be viewed from the browser, but each report is stored on the bg-swarm-manager machine with its build number.

## Project Planning
Trello Board: https://trello.com/b/ULYL5Kwb/band-generator

The board has been designed such that elements of the project move from left to right from their point of conception to being finished and fully implemented. Each card is also colour-coded according to which element of the project it pertains, e.g. Flask, Database, Jenkins, User Stories, etc.


## Risk Assessment
Risk Assessment: https://docs.google.com/spreadsheets/d/13zB-tZh8uB5HHjGJrKiGPnghNLfGiHh3k5TVSR7YIIc/edit?usp=sharing

![riskassessment][riskassessment]

As the purpose of this project was largely to learn and implement tools for continuous deployment, most of the risks I identified and aimed to tackle were in relation to continuous availability of the app on the user end. One of the many benefits of using Docker – in particular Docker Swarm in conjunction with Docker Stack – is its ability to deploy updates to services incrementally, such that an update can be rolled out without affecting the user experience at all. The assessment was therefore written from the perspective of the developer having produced the app and considering the risks associated with deploying it.

## Future Improvements
- Worker node implementation
- More replication
- Docker registry on a dedicated VM
- Better tests involving mock responses
- Full automated installation with Ansible
   - Persistence of Jenkins configuration and logs
   - Automated initial SSH handshake
   - Automated spinning up of VMs on GCP
- Greater complexity of the band generation


[appstructure]: https://i.imgur.com/SJFN8R0.png
[jenkins]: https://i.imgur.com/27WGWMm.png
[riskassessment]: https://i.imgur.com/jAQ9cS5.png
[gui]: https://i.imgur.com/aNbbWGP.png
[cd]: https://i.imgur.com/nIAf4pX.png
[testcoverage]: https://i.imgur.com/J23nSPD.png
[initadminpass]: https://i.imgur.com/AWA5LRF.png
