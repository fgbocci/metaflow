from metaflow import FlowSpec, step, etl, training


class HelloVoyager(FlowSpec):
    """
    A flow where Metaflow prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """

    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        print("HelloFlow is starting.")
        self.next(self.run_etl)

    @etl(
        step={
            "project": "fda-voyager",
            "branch": "dummy",
            "parameters": {"FOO": "BAR"},
        },
    )
    @step
    def run_etl(self):
        self.next(self.run_fake_training)

    @step
    def run_fake_training(self):
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print("HelloFlow is all done.")


if __name__ == "__main__":
    HelloVoyager()
