import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()

from rango.models import Category, Page

def populate():
    # 각 카테고리별로 추가할 페이지 데이터를 정의
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/'}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org'}
    ]

    # 카테고리와 해당 페이지 데이터를 저장하는 딕셔너리 생성
    cats = {
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages}
    }

    # 딕셔너리를 순회하며 카테고리와 페이지를 데이터베이스에 추가
    for cat, cat_data in cats.items():
        c = add_cat(cat)  # 카테고리 추가
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])  # 페이지 추가

    # 결과 출력
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# 스크립트 실행
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()