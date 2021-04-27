# REST API for Shop

REST API for Shop is a service where you can add, delete, filter and get data about the goods of diferent categories.

## Getting Started

You may clone the repository and run it on your local machine.


### Installing

Make sure you have initialised a virtual env for the project the way you usually do it. After that you can safely install all the necessary dependencies via

```
pip install -r requirements.txt
```

### How to use
To start the app you need to make migrations via
```
python manage.py migrate
```

Finally, you can run the service via
```
python manage.py runserver
```

Then it will be callable on http://0.0.0.0:80/api/

### Avaliable API endpoints:
```
api/v1/goods/ - get all goods from the DB
api/v1/goods/<pk> - get the good with particular primary key 
api/v1/categories/ - get all categories from the DB
api/v1/categories/<pk> - get the category with particular primary key 
api/v1/goods/slug/<slug> - get the good with particular slug
api/v1/categories/slug/<slug> - get the category with particular slug
```
## Filtering endpoints

To filter the DB queryset you may use params which are passed in the URL after the request starting with '?' 
Example:
```
127.0.0.1:8000/api/v1/goods?price_min=1000&price_max=2000
```

Filtering params: 

* search - searching by name of the goods or name and slug of the categories (e.g. /api/v1/goods?search=tv)
* price filtering - filtering goods listing by price (e.g. /api/v1/goods?price_min=1000&price_max=2000)
* categories - you may set up the category to filter goods (e.g. /api/v1/goods?categories=2)
* is_published - a flag (default=False) to filter by(e.g. /api/v1/goods?is_published=True)
* is_deleted - a flag (default=False) to filter by(e.g. /api/v1/goods?is_deleted=True)

### Testing 

Tests check the main functionality of the app, you can run them via

```
python manage.py test
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.1/) - The web framework

## Authors

* **Nika Dmitrievskaya** - *Initial work* - [ndmitrievskaya](https://github.com/ndmitrievskaya)
