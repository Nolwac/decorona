from .base import *
import os
DEBUG = False
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

CORS_ORIGIN_WHITELIST = (
 'http://localhost:8080',
)

import dj_database_url
# dj_url = dj_database_url.config()
DATABASES['default']=dj_database_url.config()
# DATABASES['default']['CONN_MAX_AGE']=500
