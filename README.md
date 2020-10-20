# Inventory

Trying to create a web app in flask

# Db changes

To migrate changes made in ```/api/models.py```, run the following commands:

```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

The command ```$ python manage.py db init``` is needed only the first time.
