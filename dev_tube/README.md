<center>
<h1> Welcome to Devtube!</h1>
</center>

<center>
<p> 💻devlandia is a platform for devs and enthusiasts!!   💻</p>
</center>
  
  

<h2>

our platform is incredible and complete.

</h2>

a youtube just for devs!! here you don't procastine since all the content is turnedfor programming
on this site you can learn various programming languages and computer science

</li>

</ul>

<center>
<h1> final project of the harvard cs50 course</h1>
</center>

<center>
<h3> project requirements : </h3>
</center>
<li> Your web application must utilize Django  ✅ </li>
<li>Your web application must be mobile-responsive  ✅ </li>
<li> Your web application must be sufficiently distinct from the other projects in this course  ✅ </li>
<li> requirements.txt ✅ </li>
<li> js on frontend ✅ </li>

<br>

<h1> Distinctiveness and Complexity </h1>
In this project I created a program that uploads videos together with thumbnails, similar to uploading videos from youtube.
Also on this site I created an anonymous video comments system to make the site more dynamic.

I also created a video recommendation algorithm and views and likes system. And also to make the site more intuitive for the user, I made a search system that accesses my video models and shows the search results


Also in this project I integrated some external libraries like django-allauth, django-crispy-forms, django-filter, djangorestframework.

each of these bookstores helped me to make the video platform more scalable and stable and also to use the features they offer, for example django-allauth I used to develop a login and registration system, django-cripy forms I used to help django-allauth to customize the forms in this library. and django rest I used to make the site's api

Also in this project I performed tests following the steps of the last classes of the course, and applied delivery and development techniques such as kanbam and scrum.

I also made my platform scalable using ci/cd

I used the django framework throughout the project and I used javascript libraries in my website's video player.

Note

this project is not a social network or an electronic commerce, this project is an open source study platform

**Note**

this project is not a social network or an electronic commerce, this project is a study platform

<br>
<center>
<h1> files </h1>

 - final project/
	      requirements.txt - python packages
	      manage.py - django **command-line**
	      README.md - documentation
	      db.sqlite3 - database
	      

    - aula- project file
                 settings.py - configuration file,
    						urls.py - project routes,
    						 wsgi.py - Web Server Gateway Interface,
         - Video/
                       admin.py - admin interface,
        				apps.py - app configuration,
        				models.py - communication and creating tables in the database,
        **static** -  static files folder
        
        		 .css / - css files
        				styles.css - some customization
        		.js/ -javascript files
        			videoplayer.js - video player
        
        
             **templates**- html files folder
        			
         -         video/
        				 - base.html
        				 -  upload.html
        				 - videodetail.html
        				 - videos.html
        
             **templatetags** -custom template tags
           			
        
         -     
        				 - customtags.py  - tag
        			
        
        	tests.py - test django app,
        		urls.py -  app routes,
        		views.py - view configuration folder,

     - website/
                           admin.py - admin interface,
            				apps.py - app configuration,
            				models.py - communication and creating tables in the database,
            **static** -  static files folder
    
    		 .css / - css files
            				styles.css - some customization
            		.js/ -javascript files
            			videoplayer.js - video player
            
     **templates**- html files folder
            			
             -         account/ -authedication
            				 - login.html - login user
            				 - signup.html -register user	                          
            				 - logout.html -logout page
            				                                                                                                  
    
    			        website/ -website templates
            				 - base.html - the base template
            				 - index.html -about page	                                                                                                           
    
            				
            
    
            			
            
    tests.py - test django app,
            		urls.py -  app routes,
            		views.py - view configuration folder,

<h1> additional information </h1>


and to make the login and registration system I used the django-allauth app

https://django-allauth.readthedocs.io/en/latest/installation.html

and to make the forms I used crispy forms and django_crispy_bulma which uses famework bulma.io to create the forms

https://bulma.io/
https://django-crispy-forms.readthedocs.io/en/latest/

<br>

<h1> how to use the web app? </h1>

first download the project dependencies , to do this you run the following code in your terminal

**`pip install -r requirements.txt`**

so then do a migrate as a precaution,
with the following code

**`python manage.py makemigrations`**

and then

**`python manage.py migrate`**

and now you can run the app by typing the following command in the terminal

**`python manage.py runserver`**

and a local host with port 8000 will appear, just click and your browser will open the website


