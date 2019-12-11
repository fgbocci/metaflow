import uuid
from datetime import datetime
from enum import Enum


def assemble_version():
    return datetime.now().strftime("%Y.%m.%d") + "-" + str(uuid.uuid4())[:5]


class StepStatus(Enum):
    STARTING = "starting"
    PENDING = "pending"
    WAITING_ETL = "waiting_etl"
    BUILDING = "building"
    RUNNING = "running"
    TRAINING = "training"
    FINISHED = "finished"
    ERROR = "error"
    DELAYED = "delayed"
    CANCELLING = "cancelling"
    ABORTED = "aborted"
    UNDEFINED = "undefined"

    @classmethod
    def is_error(cls, step_status):
        return step_status in [cls.ERROR, cls.ABORTED, cls.CANCELLING]

    @classmethod
    def is_done(cls, step_status):
        return step_status in [cls.ERROR, cls.ABORTED, cls.CANCELLING, cls.FINISHED]

    @classmethod
    def get_voyager_status(cls, step_status):
        if step_status in [cls.STARTING, cls.PENDING, cls.WAITING_ETL, cls.BUILDING]:
            return StepStatus.PENDING
        elif step_status in [cls.RUNNING, cls.TRAINING]:
            return StepStatus.RUNNING
        elif StepStatus.is_error(step_status):
            return StepStatus.ERROR
        elif step_status == StepStatus.FINISHED:
            return StepStatus.FINISHED

    @classmethod
    def list_done_status(cls):
        return [e.value for e in StepStatus if StepStatus.is_done(e)]
