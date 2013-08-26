from django.conf import settings


def pytest_configure(config):
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'NAME': ':memory:',
                'ENGINE': 'django.db.backends.sqlite3',
                'TEST_NAME': ':memory:',
            },
        },
        DATABASE_NAME=':memory:',
        TEST_DATABASE_NAME=':memory:',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.sites',
            'related_choice_field',
            'demo.polls',
        ],
        ROOT_URLCONF='demo.polls.urls',
        DEBUG=False,
        SITE_ID=1,
        TEMPLATE_DEBUG=True,
        # TEMPLATE_DIRS=[os.path.join(where_am_i, 'tests', 'contrib', 'django', 'templates')],
        ALLOWED_HOSTS=['*'],
    )
