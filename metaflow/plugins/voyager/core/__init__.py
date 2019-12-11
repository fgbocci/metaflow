import os

from metaflow.plugins.voyager.core.config import CONFIG, _git_token, _fury_token


def config():
    if os.getenv("SCOPE"):
        return CONFIG["PROD"]
    return CONFIG["DEV"]


FURY_TOKEN = _fury_token()

GIT_TOKEN = _git_token()

FETCH_STATUS_DELAY = 10
