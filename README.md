# Project requirements

Python 3.9.6
Node.js 17.3.0

# Project setup

1. After activating your virtual environment, navigate to the root directory to install requirements.
    - If using virtual environment:
      `python -m venv venv`
    - `venv\Scripts\activate`
2. Next install requirements:
    - `pip install -r requirements.txt`
3. Navigate to the frontend directory and setup:
    - navigate: `cd frontend`
    - install: `npm install`
    - serve: `vue serve`
4. Setup django backend:
    - open new terminal at project root
    - make static folder: `mkdir static`
    - collectstatic: `python manage.py collectstatic`
    - run: `python manage.py runserver`

# Tests

-   Unit tests have been created for the two backend endpoints: `/api/num_to_english` and `/`

    -   `python manage.py test`

# Endpoint num_to_english

-   Endpoint only accepts numerical characters within range -10^21 to 10^21

###### Valid input response example:

```
{
    "status": "ok",
    "num_in_english": "twelve"
}
```

###### Invalid input response example:

```
{
    "status": "error",
    "num_in_english": "Please enter a valid whole number. Example: '123'"
}
```

###### Out of range input response example:

```
{
    "status": "ok",
    "num_in_english": "Input out of range. Please use whole numbers between -10^21 to 10^21"
}


```
