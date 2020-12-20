version = 1
disable_existing_loggers = False

loggers = {
    'sanic.root': {
        'level': 'DEBUG',
        'handlers': ['console', 'root_file'],
        'propagate': True
    },
    'sanic.error': {
        'level': 'ERROR',
        'handlers': ['error_file'],
        'propagate': True
    },
    'sanic.access': {
        'level': 'INFO',
        'handlers': ['access_file'],
        'propagate': True
    }
}

handlers = {
    'console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'generic'
    },
    'root_file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'level': 'INFO',
        'formatter': 'generic',
        'encoding': 'utf-8',
        'filename': './runtime/log/root.log',
        'maxBytes': 2000000,
        'backupCount': 5
    },
    'error_file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'level': 'ERROR',
        'formatter': 'generic',
        'encoding': 'utf-8',
        'filename': './runtime/log/error.log',
        'maxBytes': 2000000,
        'backupCount': 5
    },
    'access_file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'level': 'INFO',
        'formatter': 'access',
        'encoding': 'utf-8',
        'filename': './runtime/log/access.log',
        'maxBytes': 2000000,
        'backupCount': 5
    }
}

formatters = {
    'generic': {
        'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s'
    },
    'access': {
        'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d %(byte)d | %(request)s'
    }
}
