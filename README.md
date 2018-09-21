# PStest

Quick start
-----------

1. Clone repository:

```
  git clone https://github.com/trottomv/pstest.git
```

2. Execute follow command from shell: 

```
  $ pip install virtualenv
  $ virtualenv venv
  $ . venv/bin/activate
  $ pip install -r requirements.txt
  $ touch db.sqlite3
  $ python manage.py migrate
  $ python manage.py runserver 8000
```

3. Api instruction:

- On your browser hit 
`localhost:8000/api/hw` for api Hello World
`localhost:8000/api/allproducts` for json api products

4. Change api value for Paypal:

- In `core/settings.py` search the follow lines and change value with your paypal api settings:

```
  PAYPAL_API_USERNAME = "CHANGEME"
  PAYPAL_API_PASSWORD = "CHANGEME"
  PAYPAL_API_SIGNATURE = "CHANGEME"
```
