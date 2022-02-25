# Project 4 - Full Stack 

![GitHub contributors](https://img.shields.io/github/contributors/nikhilkalhan92/Project-4---Full-Stack)
![GitHub last commit](https://img.shields.io/github/last-commit/nikhilkalhan92/Project-4---Full-Stack)
![GitHub language count](https://img.shields.io/github/languages/count/nikhilkalhan92/Project-4---Full-Stack)
![GitHub top language](https://img.shields.io/github/languages/top/nikhilkalhan92/Project-4---Full-Stack)

Welcome to my fourth project. This project is a blog website, using 2 different programs called Bootstrap and Django. I have also used 3 different languages: HTML5/CSS3, Javascript and Python. 

This project will show the use of CRUD functionality (Create, Read, Update, Delete). A user can post comments on all topics, As an admin I can update/delete and create new posts via the admin site. 

[Here is a link to the final project](http://project-4-full-stack.herokuapp.com/)


![amiresponsive](media/responsiove.png)


# 1 - UX

I am a big fan of the website "Reddit", I have always used the website to browse different topics, and of course getting involved. 

This project will showcase simplicity and ease to sign up to a blog, start a discussion and discuss topics with others.

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user profile and create/update/delete a blog in a simple and effective process.

### User Goals:
First Time Visitor Goals
-   As a first-time visitor, I want to sign up to the website 
-   As a first-time visitor, I want to view all current blog discussions.

Returning Visitor Goals
-   As a Returning Visitor, I want to log back into the terminal.
-   As a Returning Visitor, I want to like and comment discussions

Frequent User Goals
-   As a Frequent User, I want to check to see if there are more debates being added by various users and to get involved with the community.

### User Expectations:
The system should have a simple user interface, with the navigation to each section clear and concise.

-   The blog posts are clear to read.
-   The user interface is easy to navigate.
-   The website is responsive on all devices.
-   To have the ability to sign up via social media/online

### User Stories
Throughout the project I used the GitHub projects board to log all user stories as my project management tool. This helped me keep focus on the specific tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed. As you see below - you can see the story planned out with screenshots showing my progression.

You will see below my user stories being updated in chronological order.

#### 1

Installing Django 

![pic1](media/pic1.png) 

#### 2

![pic2](media/pic2.png)

#### 3

Linking my blog to Cloudinary after signing up,creating ana ccount and copying the key into settings.py 

![pic3](media/pic3.png)

Also setting up a new heroku app, and linking it to my SQL 

![heroku](media/heroku.png)


#### 4

Install Summernote which is a JavaScript library that helps you create WYSIWYG editors online.

![pic4](media/pic4.png)

#### 5

Install Summernote which is a JavaScript library that helps you create WYSIWYG editors online.

![pic5](media/pic5.png)

#### 6

![pic6](media/pic6.png)

#### 7

Installed gunicorn which is: This object is used to pass request data to your application, and to receive response data

![pic7](media/pic7.png)

#### 8

Created the Superuser for my django - which gives me permission to create, read, update and delete data in the Django admin
![pic8](media/pic8.png)

#### 9

![pic9](media/pic9.png)

#### 10

On Django admin - Sety up so I can manage drafts/delete posts and create new ones.

![pic10](media/pic10.png)

#### 11

![pic11](media/pic11.png)

#### 12

Created my first view on the website 

![pic12](media/pic12.png)

#### 13

![pic13](media/pic13.png)

#### 14

![pic14](media/pic14.png)

#### 15

![pic15](media/pic15.png)

#### 16

Give my website the option to allow users to sign up to my blog.

![pic16](media/pic16.png)

#### 17

![pic17](media/pic17.png)

#### 18

Allows user to comment on set post.

![pic18](media/pic18.png)

#### 19

![pic19](media/pic19.png)

#### 20

Allow user to like/unlike the post.

![pic20](media/pic20.png)

#### 21

![pic21](media/pic21.png)

# 2 Structure

It is really important to include responsive design in this project as many users are using different devices (mobile, tablet, laptop/PC). This gives the user the best experience on their device.

- Responsive on all device sizes
- Easy navigation through labelled buttons
- Footer at the bottom of the index page that links to the social media website.
- All elements will be consistent including font size, font family, colour scheme.


# 3 Skeleton 

I used Balsamiq to create my wireframes as this gives the template of the UI. This also shows where all elements will be placed within the screen.

There are 3 versions of each wireframe as one shows the design on a web browser and the other show on a Ipad and Iphone

#### Website Wireframe

![website1](media/website1.png)

![website2](media/website2.png)

![iphone](media/iphone.png)

![ipad1](media/ipad1.png)

![ipad2](media/ipad2.png)

### Surface

Colours used for my blog -

![C1](media/23bbbb.png)

![C2](media/33fff6.png)

![C3](media/979a9a.png)

![C4](media/17202a.png)

![C5](media/445261.png)

![C6](media/e84610.png)


# 4 Features


## All Pages Features 

- The navigation bar is placed at the top of all pages. The user will know if they are logged in or not. Examples below.

![loggedout](media/loggedout.png)

- You will see the social media icons at the end of the footer per page.

![socialmedia](media/socialmedia.png)

## Register Page

- A simple signup form that requires the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.

![signuppage](media/signuppage.png)

- Once signed up, you'll be logged in with a quick pop message confirming succesful registeration and you'll be able to use the platform

![usersuccessfulogin](media/usersucessful.png)

- If the user enters a password that is not secure, the user will be prompted by a message.

![userpagenotsuccessful](media/userpagenotwork.png)

- If the user enters both passwords that do not match, the user is prompted by a message.

![incorrectpw](media/incorrectpw.png)
![commonpassword](media/commonpasswordnotwork.png)

- Once the user has successfully signed up, this will automatically log in and direct the user to the homepage 

![signin](media/signin.png)

## Log Out Page

When clicking logout from the navigation bar - the webpage will give you the option to log out
![logout?](media/doyouwanttosignout.png)

Signed Out Successful
![signoutsuccesful](media/signedoutsuccesful.png)


# 5 Technologies used

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.


### Responsive Tools

HTML Validator Results

I used to check for any errors within my HTML pages. The only errors i had was because of the 'Jinja Template" method used. my mentor said to screenshot them and explain why no changes were made.

https://validator.w3.org/

### Base.HTML

![base](media/base.png)

### Index.html

![index1](media/index.png)
![index2](media/Index.html2.png)


### Post_detail.html

![postdetail](media/postdetailhtml.png)

#### CSS3 - 
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.

I had no errors in my css

![CSS errors](media/CSSerrors.png) 


#### Python
I used [pep8online](http://pep8online.com/) to check errors on my Views/Forms/Models

Models.py - I had 3 errors which i solved quite quickly

![models](media/modelspyerror.png)
![models2](media/modelspy.png)

Formspy - no errors
![forms](media/forms.png)

Views.py - I had 3 errors which I solved quite quickly
![view](media/views.png)
![views2](media/viewspynice.png)



## Manual Testing
I have tested my site on Safari and google chrome on multiple devices.

These include:
-   iPhone X
-   iPhone XS Max
-   iPad Pro
-   MacBook Pro

### Responsiveness	

I tested my website using Google Chrome Developer Tools Lighthouse feature, and received the results below:
![test](media/testing1.png)

Please find below my testing process for all pages via mobile and web:

### All Pages

Home page - When clicking the "home" button in the navigation bar, the browser redirects me to the home page. 

Blog Page - When clicking the "menu" button in the navigation bar, the browser redirects me to the menu page.

Text - Checked that all fonts and colours used are consistent.

Login / Logout page - When clicking the "login" or "logout button in the navigation bar, the browser redirects me to the login or logout page

Register page - When clicking the "register" button in the navigation bar, the browser redirects me to the register page.

 ### Home Page
 
 Media - All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices.

 Responsiveness - Check every element on the page for consistent scalability in mobile, tablet and desktop view.

![response](media/lighthousehomepage.png)

Accessibility - Checked the accessibility of the page using lighthouse

 ### Blog Page

 Media - All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices.

 Responsiveness - Check every element on the page for consistent scalability in mobile, tablet and desktop view.

 Home - Clicked the home button and you will be back on the homepage

Accessibility - Checked the accessibility of the page using lighthouse

 ![blog](media/lighthouseblog.png)

 ### Lighthouse Blog Page results

 ![lightout](media/lightouthouse.png)

 ### Media	
 
 All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices.

### Sign Up Page

 Responsiveness - Check every element on the page for consistent scalability in mobile, tablet and desktop view.

 Once you reigstered your details, you will be logged in and it will take you to the homepage and you can comment

 Accessibility - Checked the accessibility of the page using lighthouse
 ![sign](media/loginlighthouse.png)


### Signed Out

Responsiveness - Check every element on the page for consistent scalability in mobile, tablet and desktop view.

when you sign out, a message will appear confirming this.

 ### Footer

Facebook - When clicking the Facebook icon, a new tab opens and redirects to the Facebook website.	

Twitter	  - When clicking the Twitter icon, a new tab opens and redirects to the Twitter website.	

Instagram - When clicking the Instagram icon, a new tab opens and redirects to the Instagram website.

Youtube   - When clicking the youtube icon, a new tab opens and redirects you to the Youtube website.

# 6. Development Cycle

I used GitHub pages to deploy my final project. To do this I had to:
1. Login or Sign Up to [GitHub] - https://github.com/nikhilkalhan92/Project-4---Full-Stack
2. Create a new repository named "Project-4---Full-Stack"
3. Once created, click on "Settings" on the navigation bar under the repository title.
4. Choose which folder to deploy from, I used "/root".
5. Click "Save", then wait for it to be deployed. 
6. The URL will be displayed above the "source" section in GitHub Pages.

**HOW TO FORK A REPOSITORY**

### If you need to make a copy of a repository:

1. Login or Sign Up to GitHub.
2. On GitHub, go to nikhilkalhan92/Project-4---Full-Stack.
3. In the top right corner, click "Fork".

### For the final deployment to Heroku, I had to:
1. Uncomment the PostgreSQL databse from my settings.py file.
2. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

### Project Checklist
Install Django and the supporting libraries
1. Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
2. Install support libraries including psycopg2, this is used to connect the PostgreSQL database
3. Install Cloudinary libraries, this is a host provider service that stores images
4. Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

### Create a new, blank Django Project
1. Create a new project
2. Create the app
3. Migrate all new changes to the database
4. Run the server to test

### Setup project to use Cloudinary and PostgreSQL
1. Create new Heroku app
2. Sign into Heroku
3. Select New
4. Select create new app
5. Enter a relevant app name
6. Select appropriate region
7. Select the create app button

### Attach PostgreSQL database
1. In Heroku go to resources
2. Search for Postgres in the add-ons box
3. Select Heroku Postgres
4. Submit order form

### Prepare the environment and settings.py file
1. Create env.py file
2. Add DATABASE_URL with the Postgres URL from Heroku
3. Add SECRET_KEY with a randomly generated key
4. Add SECRET_KEY and generated key to the config vars in Heroku
5. Add if statement to settings.py to prevent the production server from erroring
6. Replace insecure key with the environment variable for the SECRET_KEY
7. Add Heroku database as the back end
8. Migrate changes to new database

### Get static media files stored on Cloudinary
1. Create a Cloudinary account
2. From the dashboard, copy the API Environment variable
3. In the settings.py file create a new environment variable for CLOUDINARY_URL
4. Add the CLOUDINARY_URL variable to Heroku
5. Add a temporary config var for DISABLE_COLLECTSTATIC
6. In settings.py add Cloudinary as an installed app
7. Add static and media file variables
8. Add templates directory
9. Change DIR's key to point to TEMPALTES_DIR
10. Add Heroku hostname to allowed hosts
11. Create directories for media, static and templates in the project workspace
12. Create a Procfile

### Django Admin

If you need to sign in into the admin django

URL is = https://project-4-full-stack.herokuapp.com/admin

username is nikhilkalhan92 and password is nikhilkalhan1

# 7 Final Product


Homepage
![homepage](media/homepage.png)

Signout
![signout](media/signout.png)

Blog 1
![blog](media/blog1.png)

Blog 2
![blog](media/blog2.png)

Blog 3
![blog3](media/blog3.png)

Blog 4
![blog4](media/blog4.png)

Blog 5
![blog5](media/blog5.png)

Blog 6
![blog6](media/blog7.png)

Register Page
![register](media/register.png)

SignIn
![signin](media/signin.png)

Browsing the website without being a member
![member](media/notsignedinbrowing.png)


Django admin
![djang1](media/djangoadmin.png)
![django2](media/djangoadmin2.png)
![django3](media/djangoadmin3.png)


# 8 Acknowledgments 

My Mentor Marcel thank you for the advice/meetings and answering my endless questions.

Shout out to my friend Jayden Maddison.





