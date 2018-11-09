DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'atmasters',
        'USER': 'k0t3n',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
        'CONN_MAX_AGE': 60,
    },
}
