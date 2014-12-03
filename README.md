temperature_server
==================

This Django App connects to a MySQL DB where temperature data is stored, it queries this data and displays it in form of a dashboard:

![Temperature Dashboard](http://i59.tinypic.com/9rhnye.png)

You will need a MySQL DB, the schema can be created locally with a migration:

```
python manage.py makemigrations
python manage.py migrate
```

If you are also interested about populating the Temperature DB with real data, checkout the project RPi Temperature Logger project on my repo.
