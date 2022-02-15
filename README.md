## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)


## Installing
### Setting up the database
- Project usses an Sqlite file but you can start your database server and create your database.

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/nicksonlangat/laws_africa_leave_project.git) `git clone https://github.com/nicksonlangat/laws_africa_leave_project.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment` and activate it `source name_of_your_virtual_environment/bin/activate`
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## PROJECT MODULES
- The project configs and settings is in the folder `mysite`
- Main app is `core`.

## CONTAINERISATION
- Used Docker 
- You can build the spin up the docker containers by `docker-compose -f docker-compose.yml up --build `
- Visit `localhost` to view the app running inside the container.

## Running tests
- Tests can be run by using  `coverage run --source='.' manage.py test `
- Check coverage report by `coverage report`
![swagger](screenshots/image3.png)

## Github CI for tests
- Tests are also run by a CI workflow upon pushes to the `master`  branch.
