<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#technologies-used">Technologies Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#about-the-application">About the Application</a>
      <ul>
        <li><a href="#database">Database</a></li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#scope">Scope</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Home Page Screen Shot][home-page]]

This project was built to demonstrate software development and DevOps concepts and principles such as AGILE project management, CI/CD automation, and cloud computing.

The application itself is a simple Flask web app that can be used to update a database with full CRUD functionality. The concept is this;

Your band is releasing albums and you want to add your albums to your website, under each album you want a list of songs, with the ability to add songs to multiple albums for remasters, hits albums and so on. 

Enter, Band-Flask-Pro! With full many-to-many database table functionality, you can add your music to your albums and have them listed all on the home page of the website. 

* First, you add your album on the /addalbum page, which populates an entry in the Albums table of the database
* Second, you add your song on the /addsong page, which populates an entry in the Songs table of the database
* Third, you add your song to the album you want it on on the /addsongtoalbum page, which populates an entry in the Listings table of the database, linking the song to an album
* Repeat for your full discography and it will be displayed automatically, ordered by release year on the home page

Make a mistake?

* You can edit any song you enter by navigating to the /editsong page, pick the song you want to change, and enter a new name and song length
* You can delete any album you enter on the /deletealbum page, pick the album you want gone and it will disappear from the database

Throughout the project, git was used as version control, with GitHub hosting the repository. I used a feature branch system, where I would develop parts of the app and merge them into the dev branch when they were ready. Once the dev build was considered stable, I created a pull request and merged it into the main branch.

<p align="right">(<a href="#top">back to top</a>)</p>



### Technologies Used

[![Jira Screen Shot][jira]]

* [Jira](https://www.atlassian.com/software/jira) - Project Tracking
* [jenkins](https://www.jenkins.io/) - CI/CD Automation
* [Docker](https://www.docker.com/) - Application Containerisation
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Application Framework
* [MySQL](https://hub.docker.com/_/mysql) - Database Container
* [Azure](https://azure.microsoft.com/en-gb/) - Application and Automation Hosting

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ABOUT THE APPLICATION -->
## About the Application

[Video Demo](https://drive.google.com/file/d/1n3q5wzMRAMxZePHNzalccCKUby0U8TNb/view?usp=sharing) - A video with commentary on the App and Jenkins pipeline

[![Pipeline Screen Shot][pipeline]]

This application is a monolithic Flask application made interactable through HTML templates, running off Docker swarm containing a MySQL container and several images of the front end application.

When a change is made and pushed to GitHub, it will send a trigger to Jenkins using webhooks, which will then start a job which runs through a series of scripts which test the application, build the image, push the image to Dockerhub, and deploy the application on the Docker manager node in a container using the dockerhub image.

### Database

[![Database Screen Shot][database]]

The database schema is written using SQLAlchemy as a many-to-many relationship using a link table, it is built into a MySQL docker container, but a SQLite database was used during development.

### Testing

[![Test Stage Screen Shot][test-stage]]
[![Cobertura Screen Shot][cobertura]]

Tests were written using pytest and run automatically using Jenkins. When Jenkins gets to the Test stage, it will generate a report and show it in a readable format using the Cobertura plugin. The tests run through all the python files in the application folder and currently have 100% coverage across all 4 files, including the __init__, forms, models, and routes files.

### Scope

This project was subject to limitations which restricted what could be achieved, using the MoSCoW prioritisation I considered the following points:

Must Have:

* Full CRUD functionality
* App containerisation
* Separate database
* Multiple database tables
* Unit tests
* CI/CD automation using a pipeline
* Docker swarm management

Should Have:

* App security
    * Without authorisation, anyone can have full access to the edit and delete functionality. If bad actors were to decide to sabotage the data, they would be able to do so easily.
* CRUD failsafes
    * Currently, when deleting an album from the database using the web app, the links in the listings table are left in place. This could have unintended bugs when repopulating the database and keep unnecessary data stored.

Could Have:

* Integration testing
    * Due to the timeframe and scope of the app, I deemed unit tests to suffice for the project. Integration testing would have been good to have for ensuring the integrity of the app, but were deemed low priority for the time being.
* Multiple swarm nodes
    * Due to the limitations of Azure, with public IPs and amount of virtual machines available, I was unable to set up worker nodes for this project. The machines that were running were a Jenkins/development machine, and a Docker manager node. With more resources available, I would add several worker nodes to host more instances of the app.
* NGINX load balancing
    * As mentioned above, Azure presented infrastructure limitations. With no worker node, load balancing was less of a priority due to fewer instances of the app running. Alongside this, having a machine dedicated to running nginx was not feasible. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Paris Lyons - parislyons@hotmail.co.uk

Project Link: [https://github.com/parislyons/Band-Flask-Pro](https://github.com/parislyons/Band-Flask-Pro)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/parislyons
[home-page]: documentation/HomePage.png
[jira]: documentation/Jira.png
[pipeline]: documentation/Pipeline.png
[database]: documentation/ERD.png
[test-stage]: documentation/TestStage.png
[cobertura]: documentation/Jenkins.png