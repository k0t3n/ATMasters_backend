INSTALLED_APPS = [
    # Django suit admin
    'src.settings.base.admin.SuitConfig',

    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # Project apps
    'src.apps.withdrawal_point',
    'src.apps.currency',
    'src.apps.bank',
    'src.apps.subway',

    # 3d party apps
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'django_filters',
    'mapwidgets'
]
