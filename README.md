# BETCHART
#### Video Demo: <https://youtu.be/Jjj_YZbKluw>
#### Description:
hello .
 this project is a mini card game build by python/javascripts/html/css in Django Framework, who allows you to bet on the color of upcoming candles of a live chart. it has 5 apps that i'm gonna explain them each.
1.home: which defined the landing page of website in it's files .
2.users: users app has some models that created for webapp to create accounts and uses django authentication system .
 signing in and registering a user are all defined in views.py file. and forms.py contains the forms that user is able to fill and sign up. i also used a python package named Django-Verify-Email who sends email to new users so they can verify themselvs and activate their account.
3.contact: it allows the users to communicate with the admin through a form called contact-form , the form's data will be saved on database under the model named contact and admin can access them in django administration panel.
4.transactions: it has the game's logic and many other details in it . how a user can deposit money , whithdraw, and track his/her transactions. it also has a management folder that contains runapscheduler.py that is somehow the core of this game . there are some jobs in this file that needs to be execute repeatly. like getting live price of any cryptocurrency (in our case bitcoin) from an exchange api and with mathematics it will realize the color of the current candle (in candle_color function) and it goes on forever.. python package APScheduler is used for this file 
there is also a bunch of functions and class based views in views.py file to execute the user needs and calculate their account ballance and more.. in models.py file you can see the many models that creating this game together . used Foriegn key for relation models. and post_connect (signals) for creating and updating models that are depends on other querysets.
forms.py has some forms designed for user to be able to deposit/withdraw and bet.
5.api: uses django rest framework , to send live json data to it's own api so in the frontend of webapp (in games.html) javascript codes can use ajax and rendering live data to the page so it wont reload every time but have the correct live data using ajax request..

In frontend of the webApp i used Bootstrap classes and jquery libraries to achieve what i wanted to this webApp to be look like
also used stackoverflow website a lot for my questions and issues