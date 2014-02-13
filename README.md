===============================================
Dojo Dev Camp - Django/Angular Project Template
===============================================

A project template for AngularJS, Django 1.6 and Heroku.

Cloning the Repository to GitHub
--------------------------------
- Create an empty repository at GitHub (let's call it test)
- Open up your terminal
- Run the following commands

```
cd /tmp # make sure this is a directory that exists
git clone --bare git@github.com:DojoDevCamp/django_angular_pt.git
cd django_angular_pt.git
git push --mirror git@github.com:test.git # this will be different for you
cd ..
rm -rf django_angular_pt.git
```

Deploying to Heroku
-------------------
- Create a new heroku account at heroku.com
- Open up your terminal
- Run the following commands

```
cd /path/that/will/hold/repository
git clone git@github.com:test.git # using the same name as above for an example
cd test
heroku create # this will create a new heroku app and attach it as a remote repository
```

- Copy the heroku app domain to the ALLOWED_HOSTS array in project/settings/test.py

```
git push heroku master
heroku open # run this once the previous command finishes, it may take a minute
```