from .base import *
import os

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}


import dj_database_url
# dj_url = dj_database_url.config()
DATABASES['default']=dj_database_url.config()
# DATABASES['default']['CONN_MAX_AGE']=500


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_static', 'static')#make sure to change the static root later to hagent static root

# This very one is for the media files and how to get hold of them.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'decorona_media', 'media')#make sure to change the media root later to hagent media root.