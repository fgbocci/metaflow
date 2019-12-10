from metaflow.decorators import StepDecorator


class VoyagerStepDecorator(StepDecorator):
    """
    Base class for all step decorators.

    Example:

    @my_decorator
    @step
    def a(self):
        pass

    @my_decorator
    @step
    def b(self):
        pass

    To make the above work, define a subclass

    class MyDecorator(StepDecorator):
        name = "my_decorator"

    and include it in plugins.STEP_DECORATORS. Now both a() and b()
    get an instance of MyDecorator, so you can keep step-specific
    state easily.
    """

    name = "voyager"

    def task_pre_step(self,
                      step_name,
                      datastore,
                      metadata,
                      run_id,
                      task_id,
                      flow,
                      graph,
                      retry_count,
                      max_user_code_retries):
        """
        Run before the step function in the task context.
        """
        print("LA CONCHA DE TU MADRE ALL BOYS")

    def task_decorate(self,
                      step_func,
                      flow,
                      graph,
                      retry_count,
                      max_user_code_retries):
        print(self)
        return step_func
