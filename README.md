Path of Budgets
a path of exile market tool

User Experience (UX)
User stories
First Time Visitor Goals
As a First Time Visitor, I want to be able to easily navigate throughout the site to find it's tools and what utility these provide.
Returning Visitor Goals
As a Returning Visitor, i Want to be able qucikly use the website with minimal effort

As a frequent user i want to feel like its a practical tool that saves me time to use

as a frequent user i want to become used to it's utility and feel safe that all my information is safe

Design
Colour Scheme
a dark mode colour scheme to align with the source material
Typography
used roboto for simple, familiar and contemporary feel.
Imagery
the imagery is supposed to evoke feelings of playing tha game and being another tool in your toolbelt.

Features
Responsive on all device sizes

lightweight

GDPR compliant

Fast

simple

Technologies Used
heroku (https://www.heroku.com/)
Flask (https://flask.palletsprojects.com/en/2.0.x/)
pymongo (https://pymongo.readthedocs.io/en/stable/)
mongoDB (https://www.mongodb.com/)
poe prices (https://www.poeprices.info/)
Languages Used 
HTML5
javascript
CSS3
PYTHON
Frameworks, Libraries & Programs Used
Bootstrap 4.4.1:
Bootstrap was used to assist with the responsiveness and styling of the website.
jQuery:
jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
Git
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
GitHub:
GitHub is used to store the projects code after being pushed from Git.
Photoshop:
Photoshop was used to create the logo and editing photos for the website.
GitPod:
Gitpod was used to write the code and test the site, as well as the main compiler used.
fullstack WebDev Template by code institute:
the template was used to set up the project.
testing

testing was done incrementally throughout the project running every single function manually and executing from file 

Deployment
heroku
The project was deployed to heroku using the following steps...

To log into the Heroku toolbelt CLI:

Log in to your Heroku account and go to Account Settings in the menu under your avatar.
Scroll down to the API Key and click Reveal
Copy the key
In Gitpod, from the terminal, run heroku_config
Paste in your API key when asked

then go onto https://dashboard.heroku.com/apps and create a new app
select the application and select deploy
select the github deployment method and find your github repo for your project
connect to your desired repo
enable automatic deploys
at this point heroku should deploy your addlication automatically 

utilizing the code institute template 
Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

Log in to GitHub and locate the GitHub Repository
At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
You should now have a copy of the original repository in your GitHub account.
Making a Local Clone
Log in to GitHub and locate the GitHub Repository
Under the repository name, click "Clone or download".
To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
Open Git Bash
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 3.
$ git clone https://github.com/HugoZedendahl/Cluster_Page
Press Enter. Your local clone will be created.
$ git clone https://github.com/HugoZedendahl/Cluster_Page
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Click Here to retrieve pictures for some of the buttons and more detailed explanations of the above process.

Credits
Code
Bootstrap4: Bootstrap Library used throughout the project to make site responsive using the Bootstrap Grid System as well as styling through the inbuilt styling tools that Bootstrap 4 incorporates.
Content
All content was written by the Hugo Zedendahl with exception to the emailJS related code wich was given on their website https://www.emailjs.com/.
Media
logo Images were created by Alvin Zedendahl on comission by Hugo Zedendahl
Acknowledgements
while the regex will prevent some malicios information from being submitted this is no replacement for proper encryption and security measures. one clear weakness is that since the data is stored clientside there is a possibility that a user with malintent would be able to edit the localstorage and run malicious data on the launch function. what i would have done is to encrypt the data before storing it in the localstorage and doing all the regex checks outside of the end users access.

there will be missing bug commits since this is a remake of the original repo to provide better documentation on the commits. i am not sure how to go back and redo/edit commit history so i thought this would be the best solution. link to the original repo can be found here https://github.com/HugoZedendahl/Cluster_Page

My Mentor for continuous helpful feedback.

My brother for intense QA testing and answering questions about javascript.

Tutor support at Code Institute for their support.