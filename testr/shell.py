import subprocess


class ShellOutput(object):
    def __init__(self, output, execution_was_successful):
        self._output = output
        self._execution_was_successful = execution_was_successful

    # O U T P U T
    @property
    def output(self):
        """I'm the 'output' property."""
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    @output.deleter
    def output(self):
        del self._output

    # E X E C U T I O N _ W A S _ S U C C E S S F U L
    @property
    def execution_was_successful(self):
        """I'm the 'execution_was_successful' property."""
        return self._execution_was_successful

    @execution_was_successful.setter
    def execution_was_successful(self, value):
        self._execution_was_successful = value

    @execution_was_successful.deleter
    def execution_was_successful(self):
        del self._execution_was_successful


class Shell(object):

    @classmethod
    def execute_shell_command(cls, shell_command, use_shell):
        try:
            result = subprocess.check_output(shell_command, stderr=subprocess.STDOUT, shell=use_shell, timeout=5, universal_newlines=True)
            return ShellOutput(result, True)
        except subprocess.CalledProcessError as exc:
            return ShellOutput(exc.output, False)
        except subprocess.TimeoutExpired as toExcept:
            return ShellOutput('ERROR -> Execution Timeout: ' + str(shell_command), False)
