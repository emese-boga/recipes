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

# Installing dependencies for local virtual environment

## Prerequisites

Please make sure you have `poetry` installed. You can find the installation guide [here](https://python-poetry.org/docs/).

Once installed add it to your **PATH**.

Now poetry should be installed in a platform-specific directory:
- **$HOME/.local/bin** on Unix
- **%APPDATA%\Python\Scripts** on Windows
- **~/Library/Application Support/pypoetry** on MacOS

This is the directory you should add to your **PATH**.
Check by running:
```console
poetry --version
``` 
To have the latest version:
```console
poetry self update
``` 

## Creating virtual environment

Open project in VSCode.

Install dependencies:
```console
poetry install
```

Press `CTRL+Shift+P` and search for `Python: Select Interpreter`. 
Select it and then choose option with **Poetry** on the right side.


# Running the application

In the main directory of the project execute:
```bash
docker compose up --build 
```

In another terminal execute:
```bash
docker exec -it recipes-recipes-api-1 python ./src/manage.py migrate
```

If using the environment from above access the following page:
http://localhost:8002


To try out the APIs access:
http://localhost:8002/api/docs
