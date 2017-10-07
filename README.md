# Baseapp

Baseapp is an application django for 

## Getting Started
add your file settings project the application baseapp
and add urls.py in your project

```
urlpatterns = [
    url(r'^', include('baseapp.urls')),
    ]
```

and use this command

```
python3 manage.py makemigrations
python3 manage.py migrate
``` 

## Motivation
Objective is automatisation for many application in django or other project in python

## Installation

```
git clone https://github.com/Nelestya/tools.git
```

## Authors
* **Dlugosz Tristan** - *Initial work* - [tools](https://github.com/Nelestya/tools)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Nelestya/tools/blob/master/LICENSE) file for details
