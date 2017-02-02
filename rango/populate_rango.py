import os
os.environment.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import django
django.setup()
from rango.models import Category, Page

def poputlate():
    python_pages = [{"title": "Official Python Tutorial", "url":"http://docs.python.org/2/tutorial/"},
                    {"title":"How to Think like a Computer Scientist",
                    "url":"http://www.greenteapress.com/thinkpython/"},
                    {"title": "Learn Python in 10 Minutes",
                    "url":"http://korokithakis.net/tutorials/python/"}]