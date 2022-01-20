# Finalproject
# QA DFECloud2

# Project Brief

To create a web application that integrates with a database across two tables and demonstrates CRUD functionality.-
To utilise containers to host and deploy your application.-
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.x

# Technologies:

Python

Pytest

Flask

Docker/Docker Compose

MySQL


The MVP for this project is a website that allows create read update delete functionality on a basic book logging page.
This must include SQL, Python, HTML, Docker, FLask.

# Project management

This project was version controlled using GITHUB, tasks were written as user stories then translated onto a trello board using the MoSCoW 
prioritisation method. Due to the short time frame to complete this project some features originally planned were not implemented.

![trelloboard](/webapp/docs/trellostart.jpeg)
![trelloboard](/webapp/docs/trello2.png)

# Risk assesment

![risk](/webapp/docs/risk.png)

Architechture

![pipe](/webapp/docs/pipe.png)


# Unit tests are run using pyTest.
Docker Compose builds an image with the application code and pushes two versions to Docker Hub tagged as: numbered version and latest. In the event of a problem with the latest version being deployed, previous versions can be used to roll back the application to a working version.

![arch](/webapp/docs/arch.png)

# Database relationship

![db](/webapp/docs/dbr.png)

# Unit testing

I tested the backend of the application which includes 172 tests, using maven.

![unit testing](/webapp/docs/unitt.png)

# Front End Testing

Unfortunately after several attempts at automating the frontend testing via Jenkins it was found that doing so was not achievable in the given time frame for the project. In order to do so, Selenium scripts were required but this process would have required a large amount of learning towards the end of the project. This should be considered for future improvements.


# ONE DRIVE LINK TO VIDEO

https://onedrive.live.com/embed?cid=7DCBAD4451AB20BD&resid=7DCBAD4451AB20BD%2124968&authkey=AP4agZ1l9QMbisE


# END POINT

by the end of the project I have met the MVP in having a CRUD app that is deployed using Docker.
Timescales have led to Jenkins to not be completed.
While this project has 90% of the required functionality and deployability i will continue to learn and work to get it complete.

# Future possibilities

- integrate a login page 
- Link login to Book entries
- Integrate book recommendations from the internet

# Author

shaun cullen
