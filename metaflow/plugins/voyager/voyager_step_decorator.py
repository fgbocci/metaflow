from metaflow.decorators import StepDecorator
from metaflow.plugins.voyager.pipeline.step import ETL, Training
from metaflow import current


class ETLStepDecorator(StepDecorator):
    """
    ETL step decorator.

    How to:

    etl_step = {"branch": "", "parameters": {}}
    :branch branch or release of the ETL step to be launched
    :parameters parameters to be passed to the ETL step

    @etl{step=etl_step)
    @step
    def a(self):
        pass

    """

    name = "etl"
    defaults = {"step": {}}

    def task_pre_step(
        self,
        step_name,
        datastore,
        metadata,
        run_id,
        task_id,
        flow,
        graph,
        retry_count,
        max_user_code_retries,
    ):
        """
        Run after the step function has finished successfully in the task
        context.
        """
        step = self.attributes["step"]
        step = ETL(
            project=step["project"],
            branch=step["branch"],
            parameters=step["parameters"],
        )
        current.__dict__ = step.launch()
        print("Inside ETL current: {}".format(vars(current)))


class TrainingStepDecorator(StepDecorator):
    """
    ETL step decorator.

    How to:

    etl_step = {"branch": "", "parameters": {}}
    :branch branch or release of the ETL step to be launched
    :parameters parameters to be passed to the ETL step

    @etl{step=etl_step)
    @step
    def a(self):
        pass

    """

    name = "training"
    defaults = {"step": {}}

    def task_post_step(
        self, step_name, flow, graph, retry_count, max_user_code_retries
    ):
        """
        Run after the step function has finished successfully in the task
        context.
        """
        step = self.attributes["step"]
        step = Training(
            project=step["project"],
            branch=step["branch"],
            parameters=step["parameters"],
            etl_version=vars(current)["etl_version"],
        )
        vars(current)[current.step_name] = step.launch()
