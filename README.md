# Baseapp

Baseapp is an application django for 

### Prerequisites

* **django**

```
pip3 install Django
```
or
```
pip install Django
```

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
The goal is to create a website and the ability to learn and easily modify it

## Installation

```
git clone https://github.com/Nelestya/tools.git
```

## Authors
* **Dlugosz Tristan** - *Initial work* - [tools](https://github.com/Nelestya/tools)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Nelestya/baseapp/blob/master/LICENSE) file for details
