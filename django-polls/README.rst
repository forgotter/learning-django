=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

P.S. This project was made by following instructions provided in
official django tutorial.

Requirement
-----------
Django 2.14


Quick start (To see the project in your browser)
-----------
1. Clone this repo to your PC
2. Launch a terminal/cmd and cd to the mysite folder
3. Start the server by executing
   python manage.py runserver 8000
4. Launch any browser and enter 
   localhost:8080/polls
   in the URL field and hit enter
   
   
Quick start (To use the polls apps in your project)
-----------

1. Use the tar file provided in dist folder and install it with
   pip. The django version used was 2.14

2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

3. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

4. Run `python manage.py migrate` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
