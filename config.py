import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'u\xde^K\xa5\x8a\xed\x18\x7f\xde\xce@\xc9\xca-+'

    MONGODB_SETTINGS = {"db": "UTA_Enrollment"}
