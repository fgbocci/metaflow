import time

from metaflow.plugins.voyager import pipeline
from metaflow.plugins.voyager.core import config, FETCH_STATUS_DELAY
from metaflow.plugins.voyager.core.errors import UnimplementedMethodError
from metaflow.plugins.voyager.pipeline import StepStatus

import requests


class Step:

    config = config()

    def __init__(self, project, branch, parameters):
        self.project = project
        self.branch = branch
        self.parameters = parameters
        self.version = pipeline.assemble_version()

    def __repr__(self):
        return self.__class__.__name__.lower()

    def launch(self):
        # self.execute()
        #  self.fetch_status()
        print("Mocked execution")

    def fetch_status(self):
        while True:
            status = StepStatus(self._get_status())
            if StepStatus.is_error(status):
                raise Exception("Step error")
            elif status == StepStatus.FINISHED:
                return
            else:
                time.sleep(FETCH_STATUS_DELAY)

    def _get_status(self):
        header = {"x-auth-token": self.config["fury_token"]}
        r = requests.get(
            self.config[str(self)]["endpoint"].format(self.project, self.version),
            headers=header,
        ).json()
        return r.get("status")

    def execute(self):
        raise UnimplementedMethodError()
