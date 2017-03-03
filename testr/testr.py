from .file import File
from .java import Java
from .word_document import WordDocument
from .user_input import UserInput


class TestrConfiguration(object):

    def __init__(self):
        self._home_selection = 0
        self._working_directory = ""
        self._source_file_name = ""
        self._alternate_source_file_names = []
        self._test_file_name = ""
        self._use_source_file_as_test_file = False
        self._test_cases = []
        self._test_input_from_cli = False

    def get_user_input(self):
#         self.home_selection = 1
#         self.working_directory = "/Users/Mike/Google_Drive/School/GTA/cs1_grading/AS07"
#         self.source_file_name = "DurationAO.java"
#         self.alternate_source_file_names = ["DurationA0.java", "Duration.java"]
#         self.test_file_name = "DurationIllustrator.java"
#         if self.test_file_name.strip() == "":
#             self.use_source_file_as_test_file = True
#         self.test_cases = []
#         self.test_input_from_cli = False

        self.home_selection = UserInput.prompt_home()
        self.working_directory = UserInput.prompt_working_directory()
        self.source_file_name = UserInput.prompt_source_file_name()
        self.alternate_source_file_names = UserInput.prompt_alternate_source_file_names()
        self.test_file_name = UserInput.prompt_test_file_name()
        if self.test_file_name.strip() == "":
            self.use_source_file_as_test_file = True
        self.test_cases = UserInput.prompt_test_cases()
        self.test_input_from_cli = False
        if UserInput.prompt_test_input_from_cli().lower()[:1] == "y":
            self.test_input_from_cli = True

    # H O M E _ S E L E C T I O N
    @property
    def home_selection(self):
        """I'm the 'home_selection' property."""
        return self._home_selection

    @home_selection.setter
    def home_selection(self, value):
        self._home_selection = value

    @home_selection.deleter
    def working_directory(self):
        del self._home_selection

    # W O R K I N G _ D I R E C T O R Y
    @property
    def working_directory(self):
        """I'm the 'working_directory' property."""
        return self._working_directory

    @working_directory.setter
    def working_directory(self, value):
        self._working_directory = value

    @working_directory.deleter
    def working_directory(self):
        del self._working_directorys

    # S O U R C E _ F I L E _ N A M E
    @property
    def source_file_name(self):
        """I'm the 'source_file_name' property."""
        return self._source_file_name

    @source_file_name.setter
    def source_file_name(self, value):
        self._source_file_name = value

    @source_file_name.deleter
    def source_file_name(self):
        del self._source_file_name

    # A L T E R N A T E _ S O U R C E _ F I L E _ N A M E S
    @property
    def alternate_source_file_names(self):
        """I'm the 'alternate_source_file_names' property."""
        return self._alternate_source_file_names

    @alternate_source_file_names.setter
    def alternate_source_file_names(self, value):
        self._alternate_source_file_names = value

    @alternate_source_file_names.deleter
    def alternate_source_file_names(self):
        del self._alternate_source_file_names

    # T E S T _ F I L E _ N A M E
    @property
    def test_file_name(self):
        """I'm the 'test_file_name' property."""
        return self._test_file_name

    @test_file_name.setter
    def test_file_name(self, value):
        self._test_file_name = value

    @test_file_name.deleter
    def test_file_name(self):
        del self._test_file_name

    # U S E _ S O U R C E _ F I L E
    @property
    def use_source_file_as_test_file(self):
        """I'm the 'use_source_file_as_test_file' property."""
        return self._use_source_file_as_test_file

    @use_source_file_as_test_file.setter
    def use_source_file_as_test_file(self, value):
        self._use_source_file_as_test_file = value

    @use_source_file_as_test_file.deleter
    def use_source_file_as_test_file(self):
        del self._use_source_file_as_test_file

    # T E S T _ C A S E S
    @property
    def test_cases(self):
        """I'm the 'test_cases' property."""
        return self._test_cases

    @test_cases.setter
    def test_cases(self, value):
        self._test_cases = value

    @test_cases.deleter
    def test_cases(self):
        del self._test_cases

    # T E S T _ I N P U T _ F R O M _ C L I
    @property
    def test_input_from_cli(self):
        """I'm the 'test_input_from_cli' property."""
        return self._test_input_from_cli

    @test_input_from_cli.setter
    def test_input_from_cli(self, value):
        self._test_input_from_cli = value

    @test_input_from_cli.deleter
    def test_input_from_cli(self):
        del self._test_input_from_cli


class Testr(object):

    def __init__(self, testr_configuration, working_directory):
        self._testr_configuration = testr_configuration
        self._working_directory = working_directory
        self._comment_files = self._find_comment_files()
        self._path_to_source_file = self._find_path_to_source_file()
        self._path_to_test_file = self._find_path_to_test_file()
        self._compiled_successfully = False;
        self._run_successfully = False;
        self._list_of_compile_shell_outputs = []
        self._list_of_run_shell_outputs = []
        self._run_test()

    def _find_comment_files(self):
        return File.get_files_in_directory(directory=self.working_directory, file_extension='txt', file_name='201*')

    def _find_path_to_source_file(self):
        path_to_source_file = ""
        if File.file_exists_in_directory(directory=self.working_directory, file_name=self.testr_configuration.source_file_name):
            path_to_source_file = self.working_directory + '/' + self.testr_configuration.source_file_name
        elif File.find_existing_file_in_list(directory=self.working_directory, list_of_file_names=self.testr_configuration.alternate_source_file_names) != "":
            path_to_source_file = self.working_directory + '/' + File.find_existing_file_in_list(directory=self.working_directory, list_of_file_names=self.testr_configuration.alternate_source_file_names)
        return path_to_source_file

    def _find_path_to_test_file(self):
        path_to_test_file = self.path_to_source_file
        if self.testr_configuration.test_file_name != "" and not self.testr_configuration.use_source_file_as_test_file:
            if File.file_exists_in_directory(directory=self.working_directory, file_name=self.testr_configuration.test_file_name):
                path_to_test_file = self.working_directory + '/' + self.testr_configuration.test_file_name
        return path_to_test_file

    def _run_test(self):
        self.list_of_compile_shell_outputs += self._compile_files()
        for shell_output in self.list_of_compile_shell_outputs:
            if shell_output.execution_was_successful:
                self.compiled_successfully = True

        if self.compiled_successfully:
            self.list_of_run_shell_outputs += self._run_files()
            for shell_output in self.list_of_run_shell_outputs:
                if shell_output.execution_was_successful:
                    self.run_successfully = True

    def _compile_files(self):
        compile_output = []
        compile_output.append(Java.compile(file_path=self.path_to_source_file))
        if compile_output[0].execution_was_successful:
            if not self.testr_configuration.use_source_file_as_test_file:
                compile_output.append(Java.compile(self.path_to_test_file))
        return compile_output

    def _run_files(self):
        run_results = []
        if self.testr_configuration.use_source_file_as_test_file:
            self.path_to_test_file = self.path_to_source_file
        if len(self.testr_configuration.test_cases) > 0:
            for test_case in self.testr_configuration.test_cases:
                run_results.append(Java.run(run_file_path=self.path_to_test_file, get_input_from_command_line=self.testr_configuration.test_input_from_cli, input_file_path=self.testr_configuration.working_directory + '/' + test_case))
                # if self.testr_configuration.use_source_file_as_test_file:
                run_results[-1].output = WordDocument.interleave_io(run_results[-1].output, ':>', File.get_text_from_file(self.testr_configuration.working_directory + '/' + test_case))
        else:
            run_results.append(Java.run(run_file_path=self.path_to_test_file))
        return run_results

    # T E S T R _ C O N F I G U R A T I O N
    @property
    def testr_configuration(self):
        """I'm the 'testr_configuration' property."""
        return self._testr_configuration

    @testr_configuration.setter
    def testr_configuration(self, value):
        self._testr_configuration = value

    @testr_configuration.deleter
    def testr_configuration(self):
        del self._testr_configuration

    # W O R K I N G _ D I R E C T O R Y
    @property
    def working_directory(self):
        """I'm the 'working_directory' property."""
        return self._working_directory

    @working_directory.setter
    def working_directory(self, value):
        self._working_directory = value

    @working_directory.deleter
    def working_directory(self):
        del self._working_directory

    # C O M M E N T _ F I L E S
    @property
    def comment_files(self):
        """I'm the 'comment_files' property."""
        return self._comment_files

    @comment_files.setter
    def comment_files(self, value):
        self._comment_files = value

    @comment_files.deleter
    def comment_files(self):
        del self._comment_files

    # P A T H _ T O _ S O U R C E _ F I L E
    @property
    def path_to_source_file(self):
        """I'm the 'path_to_source_file' property."""
        return self._path_to_source_file

    @path_to_source_file.setter
    def path_to_source_file(self, value):
        self._path_to_source_file = value

    @path_to_source_file.deleter
    def path_to_source_file (self):
        del self._path_to_source_file

    # P A T H _ T O _ T E S T _ F I L E
    @property
    def path_to_test_file(self):
        """I'm the 'path_to_test_file' property."""
        return self._path_to_test_file

    @path_to_test_file.setter
    def path_to_test_file(self, value):
        self._path_to_test_file = value

    @path_to_test_file.deleter
    def path_to_test_file (self):
        del self._path_to_test_file

    # C O M P I L E D _ S U C C E S S F U L L Y
    @property
    def compiled_successfully(self):
        """I'm the 'compiled_successfully' property."""
        return self._compiled_successfully

    @compiled_successfully.setter
    def compiled_successfully(self, value):
        self._compiled_successfully = value

    @compiled_successfully.deleter
    def compiled_successfully (self):
        del self._compiled_successfully

    # R U N _ S U C C E S S F U L L Y
    @property
    def run_successfully(self):
        """I'm the 'run_successfully' property."""
        return self._run_successfully

    @run_successfully.setter
    def run_successfully(self, value):
        self._run_successfully = value

    @run_successfully.deleter
    def run_successfully (self):
        del self._run_successfully

    # L I S T _ O F _ C O M P I L E _ S H E L L _ O U T P U T S
    @property
    def list_of_compile_shell_outputs(self):
        """I'm the 'list_of_compile_shell_outputs' property."""
        return self._list_of_compile_shell_outputs

    @list_of_compile_shell_outputs.setter
    def list_of_compile_shell_outputs(self, value):
        self._list_of_compile_shell_outputs = value

    @list_of_compile_shell_outputs.deleter
    def list_of_compile_shell_outputs (self):
        del self._list_of_compile_shell_outputs

    # L I S T _ O F _ R U N _ S H E L L _ O U T P U T S
    @property
    def list_of_run_shell_outputs(self):
        """I'm the 'list_of_run_shell_outputs' property."""
        return self._list_of_run_shell_outputs

    @list_of_run_shell_outputs.setter
    def list_of_run_shell_outputs(self, value):
        self._list_of_run_shell_outputs = value

    @list_of_run_shell_outputs.deleter
    def list_of_run_shell_outputs (self):
        del self._list_of_run_shell_outputs
