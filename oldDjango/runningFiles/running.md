# Create Django pip environment
1. Outside of repo folder do the following (typically inside an folder called environments so nothing else goes there)
    a. python -m venv djangoEnv
    b. (djangoEnv is the environment name feel free to change this)
2. Activate Environment (typically from same location you created it)
    a. Mac Users
        1. source djangoEnv/bin/activate
        2. You should  now see djangoEvn in () in your terminal
    b. Windows Users
        1. source djangoEnv/Scripts/activate
        2. You should  now see djangoEvn in () in your terminal
3. Install pip packages
    a. pip install 
        1. django
        2. bcrypt
        3. django-environ
        4. ipython
        5. mysql-connector-python
        6. pillow

# Add base database Schema
1. Open MySQL Workbench
2. Open your Local Instance
3. Click the create new schema icon
4. Name database thehives_health
5. Apply changes

# Alter/Edit settings file, add .env, and add key.py 
1. cd into repo and open the settings file (health/settings.py)
2. You will need to make the following edits to this file (typically I use commenting so it can be changed for deployment eaiser)
    a. Comment out line 32 and uncomment 33 (debug)
    b. Comment out line 35 and uncomment 36 (allowed_hosts)
    c. Copy lines 103-112 and paste below and comment out 103-112
    d. Edit the password field (aprox line 118) to match your workbench password
3. You will need to create a file called .env inside the health folder and add the following
    a. KEY='enter anything here as this is your secret key and will never go to github'
    b. Make sure you keep this .env file ( I sometimes make a secondary folder inside my environments for keys and inside add a folder for the app and place a copy of this .env there so i can always have the proper key (if you change the key current passwords in db will not work))
4. You now need to create a file called key.py inside the healthApp folder (this also does not go to github so save a copy in same folder listed above) in this file you will need to add the following
    a. PROVIDERKEY='addRandomTextHere'
    b. ADMINKEY='addMoreRandomTextHere'
    c. These are used to create different accesses and used for the provider branch mostly

# Run the following commands
- Be sure to be at the base of the heathLog folder
1. python manage.py makemigrations
2. python manage.py migrate
- If you could like to see the Django admin run the following
3. python manage.py createsuperuser
    a. follow prompts in terminal (you will not see anything when typing the password)

# Pending no errors thus far you are ready to start the server
1. python manage.py runserver
2. Go to https://127.0.0.1:8000/ or localhost:8000/ to view the application

# Before creating a user 
1. 1st User is auto superadmin level
2. you will need to create 2 more users with the following names (as it helps with some views)
    1. First Name for one needs to be Example the other one needs to be Diabetic (for seed data to display right please add example then diabetic all after yourself)
    2. This allows for 2 example accounts to be shown/seen with out logging in
3. Once these are created you can use the seedData.md file to add some quick data to the database 


# Possible current view issues
- There are still some CSS issues on desktop mode so you may want to inspect element and change to a mobile view if it looks like a page is not done (that just means it is done on mobile and still needs the desktop views written)

