from .shell import *
from .file import File


class Java(object):

    @classmethod
    def compile(cls, file_path):
        shell_command = ['javac', '-classpath', File().get_path_from_file_name(file_name=file_path), file_path]
        return Shell.execute_shell_command(shell_command=shell_command, use_shell=False)

    @classmethod
    def run(cls, run_file_path, get_input_from_command_line=False, input_file_path=None):
        run_file_directory_path = File.get_path_from_file_name(run_file_path)
        run_file_name = File.remove_extension_from_file_name(File.remove_path_from_file_name(run_file_path))
        if input_file_path is None:
            shell_command = ['exec java -classpath ' + run_file_directory_path + ' ' + run_file_name]
            run_result = Shell.execute_shell_command(shell_command=shell_command, use_shell=True)
        else:
            if get_input_from_command_line:
                shell_command = 'exec java -classpath ' + run_file_directory_path + '/ ' + run_file_name + ' ' + File().get_text_from_file(input_file_path)
                run_result = Shell.execute_shell_command(shell_command, True)
            else:
                shell_command = 'exec java -classpath ' + run_file_directory_path + '/ ' + run_file_name + ' < ' + input_file_path + ' > ' + run_file_directory_path + '/out.txt'
                run_result = Shell.execute_shell_command(shell_command, True)
                run_result.output = File().get_text_from_file(run_file_directory_path + 'out.txt')
        return run_result