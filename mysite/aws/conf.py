import datetime

AWS_ACCESS_KEY_ID = "AKIAIDXU33RWKGU7ZFAQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

WS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True


DEFAULT_FILE_STORAGE = 'mysite.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'mysite.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'hashedvalue-assets'
S3DIRECT_REGION = 'us-east-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
