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
This is what the app does

### App Structure
![appstructure][appstructure]

This is how the app works

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

### Jenkins
![jenkins][jenkins]

### Testing
![testlog][testlog]
![testcoverage][testcoverage]

## Project Planning
Trello Board: https://trello.com/b/ULYL5Kwb/band-generator

The board has been designed such that elements of the project move from left to right from their point of conception to being finished and fully implemented. Each card is also colour-coded according to which element of the project it pertains, e.g. Flask, Database, Jenkins, User Stories, etc.


## Risk Assessment
Risk Assessment: https://docs.google.com/spreadsheets/d/13zB-tZh8uB5HHjGJrKiGPnghNLfGiHh3k5TVSR7YIIc/edit?usp=sharing

![riskassessment][riskassessment]

As the purpose of this project was largely to learn and implement tools for continuous deployment, most of the risks I identified and aimed to tackle were in relation to continuous availability of the app on the user end. One of the many benefits of using Docker – in particular Docker Swarm in conjunction with Docker Stack – is its ability to deploy updates to services incrementally, such that an update can be rolled out without affecting the user experience at all. The assessment was therefore written from the perspective of the developer having produced the app and considering the risks associated with deploying it.

## Future Improvements

[appstructure]: https://i.imgur.com/SJFN8R0.png
[jenkins]: https://i.imgur.com/27WGWMm.png
[riskassessment]: https://i.imgur.com/jAQ9cS5.png
[gui]: https://i.imgur.com/aNbbWGP.png
[cd]: https://i.imgur.com/nIAf4pX.png
[testcoverage]: https://i.imgur.com/J23nSPD.png
[initadminpass]: https://i.imgur.com/AWA5LRF.png
