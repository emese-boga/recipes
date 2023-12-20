[![Coverage](https://img.shields.io/codecov/c/github/emese-boga/recipes)](https://app.codecov.io/gh/emese-boga/recipes)

# Recipes


A simple website for uploading recipes


# Environment

```bash
PORT=8002
DB_ROOT_PASSWORD=FrzBFZ&YpYLMV4R&
DB_USER=recipe_manager
DB_PASS=dydJUaETVRvrDFwc
DB_NAME=db_recipes
DB_PORT=4880
DB_HOST=recipes_host
SECRET_KEY=3we83YzHaGQyCPWoQhfw7qndhndrJIoI
```

## Creating virtual environment

Create a virtual environment by running:
```console
python3 -m venv .venv
``` 
Activate your virtual environment:
```console
source .venv/bin/activate
``` 

Install the dependencies by running
```console
pip install -r requirements.txt
``` 


# Running the application

In the main directory of the project execute:
```bash
docker compose up --build 
```

In another terminal execute migrations:
```bash
docker exec -it recipes-recipes-api-1 python ./src/manage.py migrate
```

Create a Django super user:
```bash
docker exec -it recipes-recipes-api-1 python ./src/manage.py createsuperuser
```

If using the environment from above access the following page:
http://localhost:8002


The admin page:
http://localhost:8002/admin
