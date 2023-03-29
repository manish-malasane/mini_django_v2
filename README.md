## Project Structure - `(before django-admin startapp <app_name>)`

- minidjango_v3 (django project root directory)
  - manage.py  (entry point for django-project)
  - minidjango_v3 (django project settings package)
    - __init__.py (this is an empty python file which tells python it is a python package)
    - wsgi.py    (project instantiation)
    - settings.py (project configuration)
    - urls.py   (urls configuration)
    - asgi.py  (project instantiation)
  - requirements.txt (dependencies)
  - README.md (Documentation)
  - venv  (isolation)


####  In Brief
```
- minidjango_v3 :-> DJANGO PROJECT ROOT DIRECTORY

  - manage.py :-> It is a command line application. It is a shortcut to use django-admin command line utility tool. It 
    is used to run management commands related to our project. by using this we run our development server and many more.
  
  - minidjango_v3 :-> DJANGO PROJECT SETTINGS DIRECTORY
    - __init__.py :-> This is empty python file which tells python it is a package.
    
    - wsgi.py :-> It is a simple web-server gateway interface. We required this for deployment of application on the server
      which follows wsgi specifications. 
    
    - settings.py :-> It is a master configuration file of our django project. Here all configurations are available 
      which are related to our project.
    
    - urls.py :-> Here we do url mapping of our views which we written in minidjango_v3/app/views.py. This file is 
      responsible for mapping the routs and paths in our project. 
    
    - asgi.py :-> It is a simple asynchronous-server gateway interface. We required this for deployment of application on 
      the server which follows asgi specifications.
```


## Project structure `(after django-admin startapp <app_name>)`

- minidjango_v3 (django-project root directory)
  - manage.py   (entry -point of django project command line utility)
  - app         (django-application)
    - __init__.py (this file tells python it is a pacakge)
    - migrations  (to keep track of db changes)
      - __init__.py (this file tells python it is a package)
    - admin.py   (built in django-admin GUI)
    - apps.py   (application configurations itself)
    - models.py  (to define db)
    - tests.py  (to define unit tests)
    - views.py  (actual business logic goes here.)
  - minidjango_v3 (django-project settings directory)
    - __init__.py (this file tells python it is a python package)
    - wsgi.py   (project instantiation)
    - settings.py  (project configuration)
    - urls.py  (urls configuration)
    - asgi.py (project instantiation)
  - requirements.txt (dependencies)
  - README.md (Documentation)
  - venv (isolation)

### In Brief
```
- minidjango_v3 :-> DJANGO PROJECT ROOT DIRECTORY

  - manage.py :-> This is a command line application. It is a shortcut to use django-admin command line utility.It is
    used to run management commands in our project. by using this we run our development server and many more. 
    
  - app :-> DJANGO APPLICATION
  
    - __init__.py :-> This empty file tells python it is a python pacakge.
    
    - migrations :-> Here django stores some files to keep track of changes we made in the models.py for keeping the 
      models.py and database synchronised.
      
      - __init__.py :-> This empty file tells python it is a python package.
      
    - admin.py :-> This is a configuration file for a built-in django-admin application
    
    - apps.py  :-> This a configuration file for application itself.
    
    - models.py :-> We use this file for writing the models in ORM way. It is basically a DDL. In this django models 
      are automatically converted into database tables. 
      
    - tests.py :-> We use this file for writing unit tests
    
    - views.py :-> Here we write actual business logic. From here our request/ response cycle of our web-application is 
       handled.
       
  - minidjango_v3 :-> DJANGO PROJECT SETTINGS DIRECTORY
  
    - __init__.py :-> This empty file tells python it is a python package.
    
    - wsgi.py :-> It is a simple web-server gateway interface. We required this for deployment of application on the 
      server which follows wsgi specifications.
      
    - settings.py :-> It is a master configuration file of our django project. Here all the configurations are available
      which are related to our project.
      
    - urls.py :-> Here we do mapping of views which we written under minidjango_v2/app/views.py. This file is responsible
      for mapping the routes and paths in our project.
      
    - asgi.py :->  It is a simple asynchronous-server gateway interface. We required this for deployment of application on the 
      server which follows wsgi specifications.
```