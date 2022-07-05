# Heroku

[Heroku: a tool for deployment](https://www.heroku.com/home):  
    - free!   
    - Support Python, Flask, Postgres databases  

## Set up steps:
1. ` brew tap heroku/brew && brew install heroku`: installs heroku and its CLI (command line interface)
2. `heroku login`
3. gunicorn: This is a Python package that should be included in the requirements.txt file in our Flask app. It is capable fo running Flask apps so they hanlde simultaneous requests.  If it is not in requirements.txt, run: ` (venv) $ pip install gunicorn` then `(venv) $ pip freeze > requirements.txt`
4. create Procfile: `$ touch Procfile` pay attn to upper/lowercasing
5. Inside Procfile, add: `web: gunicorn 'app:create_app()'` Now save file and do a git commit with the file included.
6. Create a heroku app:  
   1. `$ heroku create your-app-name` or `$ heroku create` for a randomly generated name
7. Verify presence of heroku remote branch with command: `$ git remote -v`
8. Push code to heroku remote: `$ git push heroku your-branch-name:main`
9. Create database in heroku: `$ heroku addons:create heroku-postgresql:hobby-dev`
10. Add environmental variables: Settings --> Config Vars -->Click "Reveal Config Vars" --> Find the automatically generated variable named "DATABASE_URL" --> Copy the value of this connection string --> Create a new environment variable named SQLALCHEMY_DATABASE_URI (or whatever name you're using) --> Set the value of this variable to the connection string we copied
11. Set up and initialize database in heroku: `$ heroku run flask db upgrade`
12. Instead of localhost, we can visit https://your-app-name.herokuapp.com/books, where your-app-name is the name of our Heroku app.
13. Heroku logs: This will give HTTP requests/errors/etc...
    1.  Go to More on dashboard
    2.  select View Logs
    3.  Alternately, use `heroku logs` on CLI
14. To re-deploy with new changes: `$ git push heroku your-branch-name:main`

Other heroku commands:  
- `heroku logs --tail`:Starts tailing the Heroku logs in the current terminal window, displaying real-time updates
- `heroku pg:psql`: Runs the psql CLI on the Heroku machine running our app. We can use this to execute psql commands, and check, add, update, or delete the data that our app uses.
