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
            'class': 'women.log_handlers.InfoHandler',
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'critical'
        },
        'error': {
            'level': 'ERROR',
            'filters': ['error_only'],
            'class': 'women.log_handlers.InfoHandler',
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'error'
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warning_only'],
            'class': 'women.log_handlers.InfoHandler',
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'formatter': 'verbose',
            'log_type': 'warning'
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'women.log_handlers.InfoHandler',
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'log_type': 'info'
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['debug_only'],
            'class': 'women.log_handlers.InfoHandler',
            'filename': os.path.join(BASE_DIR, 'logs/'), # Или любой путь куда юзер, запускающий сервер имеет доступ
            'log_type': 'debug'
        },
        'notify': {
            'level': 'WARNING',
            'class': 'women.log_handlers.NotifyHandler' # Путь к классу
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'console',
        }
    },
    'filters': {
        'error_only': {
            '()': 'women.filters.ErrorOnlyFilter' # Путь к классу
        },
        'warning_only': {
            '()': 'women.filters.WarningOnlyFilter' # Путь к классу
        },
        'info_only': {
            '()': 'women.filters.InfoOnlyFilter' # Путь к классу
        },
        'debug_only': {
            '()': 'women.filters.DebugOnlyFilter' # Путь к классу
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