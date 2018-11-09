from split_settings.tools import optional, include

include(
    'base/security.py',
    optional('local/security.py'),

    'base/paths.py',
    'base/middleware.py',
    'base/apps.py',
    # TODO: add debug toolbar
    # 'base/debug_toolbar.py',
    'base/static.py',
    # TODO: logging
    # 'base/logging.py',

    'base/*.py',

    optional('local/*.py'),
)
