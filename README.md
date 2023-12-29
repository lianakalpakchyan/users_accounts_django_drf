# Django and DRF users' accounts

This application has a Django web interface and DRF API to show registered users' accounts by the table. Where it is also possible to check every account individually.
## Installation


```bash
git clone https://github.com/lianakalpakchyan/users_accounts_django_drf.git
python3 -m venv venv
source venv/bin/activate
cd website
pip install -r requirements/requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage
Create a superuser who can sign up another users and create accounts for them.
To check the accounts' table direct to http://127.0.0.1:8000/accounts/.

For API usage direct to:
1. http://127.0.0.1:8000/swagger/
2. http://127.0.0.1:8000/redoc/


## Running Tests
The following tests can be run From BlogsWebsiteBackend folder.

```bash
python manage.py test accounts.tests.test_models
python manage.py test accounts.tests.test_api_views
python manage.py test accounts.tests.test_views_urls
```


## Logging

All the logs are saved in information.log file. However, so far no need for logs.

## Status
Always can be improved :)
