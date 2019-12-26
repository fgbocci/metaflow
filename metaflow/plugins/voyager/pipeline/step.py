import logging

from metaflow.plugins.voyager.pipeline.base import Step

import requests


class ETL(Step):
    def __init__(self, project, branch, parameters):
        super().__init__(project, branch, parameters)

    def execute(self):
        header = {"x-auth-token": self.config["fury_token"]}
        data = {
            "branch": self.branch,
            "version": self.version,
            "parameters": self.parameters,
        }
        r = requests.post(
            self.config[str(self)]["endpoint"].format(self.project, ""),
            json=data,
            headers=header,
        )
        logging.info("Execute response: {}".format(r.json()))


class Training(Step):
    def __init__(self, project, branch, parameters, etl_version):
        super().__init__(project, branch, parameters)
        self.etl_version = etl_version

    def execute(self):
        header = {"x-auth-token": self.config["fury_token"]}
        data = {
            "branch": self.branch,
            "version": self.version,
            "etl_version": self.etl_version,
            "flavor": "cpu-small",
            "instance_amount": 1,
            "parameters": self.parameters,
        }
        requests.post(
            self.config[str(self)]["endpoint"].format(self.project, ""),
            json=data,
            headers=header,
        )
