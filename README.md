# Finalproject
QA DFECloud2

Project Brief
To create a web application that integrates with a database across two tables and demonstrates CRUD functionality.-
To utilise containers to host and deploy your application.-
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.x

Technologies:

Python-
Pytest-
Flask-
Docker/Docker Compose-
MySQL-

The MVP for this project is a website that allows create read update delete functionality on a basic book logging page.
This must include SQL, Python, HTML, Docker, FLask.

Project management
This project was version controlled using GITHUB, tasks were written as user stories then translated onto a trello board using the MoSCoW 
prioritisation method. Due to the short time frame to complete this project some features originally planned were not implemented.

![trelloboard](/webapp/docs/trellostart.jpeg)
![trelloboard](/webapp/docs/trello2.png)

Risk assesment

![risk](/webapp/docs/risk.png)

Architechture

![pipe](/webapp/docs/pipe.png)


Unit tests are run using pyTest.
Docker Compose builds an image with the application code and pushes two versions to Docker Hub tagged as: numbered version and latest. In the event of a problem with the latest version being deployed, previous versions can be used to roll back the application to a working version.

![arch](/webapp/docs/arch.png)

Database relationship

![db](/webapp/docs/dbr.png)

Unit testing

I tested the backend of the application which includes 172 tests, using maven.

![unit testing](/webapp/docs/unitt.png)

Front End Testing
Unfortunately after several attempts at automating the frontend testing via Jenkins it was found that doing so was not achievable in the given time frame for the project. In order to do so, Selenium scripts were required but this process would have required a large amount of learning towards the end of the project. This should be considered for future improvements.



user stories

as a user I would like somewhere to log my reading. this must be a simple slick place to log all my books i have read
When using the app i would like it to be eaasy to use, understand and have predictable actions.

it must have - book identification through name and author.
it must be simple to use
it must have CRUD functionality

it should have a login system to allow multiple users
it should have a clean appearence
it should have CI/CD through jenkins

it could have social media integration for posting
it could have links to goodreads for recommendations

it will not have optimisation for mobile
it will not have 2 factor authentification

The App

a one page site for entry of read books
simple colours 
easy identifiable buttons

Version control via GITHUB

Unit testing

Conclusion

I have met the mvp as i have a working app that fulfils the basic functionality for the project.
Timescales have led to Jenkins and unit testing to not be completed.


Future possibilities
- integrate a login page and link login to book entries
- Integrate book recommendations from books read
- Use Jenkins for CI/CD
- learn more about unit testing to be able to unit test the functions
