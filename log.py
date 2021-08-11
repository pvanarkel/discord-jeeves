LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO', 
            'class': 'logging.StreamHandler',
            'formatter': 'standard', 
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level' : 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': 'jeeves.log',
            'maxBytes': 4096,
            'backupCount': 7
        }
    }, 
    'loggers': {
        '': { # root logger                  
            'handlers': ['console','file'],    
            'level': 'DEBUG',    
            'propagate': False 
        }
    }
}
