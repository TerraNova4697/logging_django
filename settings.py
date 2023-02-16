import os


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} - {asctime} - {module} - {process:d} - {thread:d} - {message}',
            'style': '{',
        },
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'critical': {
            'level': 'CRITICAL',
            'class': 'project.log_handlers.InfoHandler', # Путь к классу InfoHandler
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'critical'
        },
        'error': {
            'level': 'ERROR',
            'filters': ['error_only'],
            'class': 'project.log_handlers.InfoHandler', # Путь к классу InfoHandler
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'error'
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warning_only'],
            'class': 'project.log_handlers.InfoHandler', # Путь к классу InfoHandler
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'warning'
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'project.log_handlers.InfoHandler', # Путь к классу InfoHandler
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'log_type': 'info'
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['debug_only'],
            'class': 'project.log_handlers.InfoHandler', # Путь к классу InfoHandler
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'log_type': 'debug'
        },
        'notify': {
            'level': 'WARNING',
            'class': 'project.log_handlers.NotifyHandler' # Путь к классу NotifyHandler
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'console',
        }
    },
    'filters': {
        'error_only': {
            '()': 'project.filters.ErrorOnlyFilter' # Путь к классу ErrorOnlyFilter
        },
        'warning_only': {
            '()': 'project.filters.WarningOnlyFilter' # Путь к классу WarningOnlyFilter
        },
        'info_only': {
            '()': 'project.filters.InfoOnlyFilter' # Путь к классу InfoOnlyFilter
        },
        'debug_only': {
            '()': 'project.filters.DebugOnlyFilter' # Путь к классу DebugOnlyFilter
        }
    },

    'loggers': {
        '': {
            'handlers': ['critical', 'error', 'warning', 'info', 'debug', 'notify', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}