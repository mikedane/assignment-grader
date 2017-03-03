from .screen import Screen


class UserInput(object):

    @classmethod
    def prompt_home(cls):
        Screen.reset_screen()
        home_selection = \
            input("Welcome to Testr!\n"
                  "Testr is a useful tool which can parse through a directory of assignments and test\n"
                  "each one. Select one of the options below to proceed.\n\n"
                  "Testr Options:\n"
                  "1. Test an assignment submission\n"
                  "2. Test a lab submission\n"
                  "3. Exit Testr\n\n")
        return home_selection

    @classmethod
    def prompt_working_directory(cls):
        Screen.reset_screen()
        working_directory = input(
            "Enter the path to the working directory, this is the location of the folder that contains all of the\n"
            "assignment submissions (ex. /grading/AS06/)\n\n"
            "Working Directory : ")

        return working_directory

    @classmethod
    def prompt_source_file_name(cls):
        Screen.reset_screen()
        source_file_name = input(
            "Enter the name of the source file.py, which is the file.py that is being graded, and the one that will be\n"
            "placed in the feedback word document (ex. HelloWorld.java)\n\n"
            "Source file.py : ")
        return source_file_name

    @classmethod
    def prompt_alternate_source_file_names(cls):
        Screen.reset_screen()
        alternate_source_file_names = input(
            "Sometimes students submit files with incorrect or inconsistant names. Here we'll account for any\n"
            "alternate source file.py names that students may have submitted. For example if the file.py is supposed\n"
            "to be named 'HelloWorld.java', and a student submitted 'myHelloWorld.java' or 'HelloWorldV2.java'\n"
            "we want the script to know to check for files with those names.\n\n"
            "Enter any alternate source file.py names in a space separated list: ex. item1 item2 item3\n\n"
            "Alternate Source file.py Names : ")
        return [source_file_name for source_file_name in alternate_source_file_names.split()]

    @classmethod
    def prompt_test_file_name(cls):
        Screen.reset_screen()
        test_file_name = input(
            "Enter the name of the testing file.py, which is the file.py that is being used to test the source file.py.\n"
            "In many cases a testing file.py will not be used, if this is the case leave the field blank.\n"
            "(ex. TestHelloWorld.java)\n\n"
            "Testing file.py : ")
        return test_file_name

    @classmethod
    def prompt_test_cases(cls):
        Screen.reset_screen()
        test_cases = input(
            "Enter the names of the test case files,these files will contain sets of input used for testing.\n"
            "In many cases there are several of these files. Please enter them in the order they are to be tested\n"
            "in a space separated list: ex. tc1.txt tc2.txt tc3.txt\n\n"
            "Test Case Files : ")
        return [test_case for test_case in test_cases.split()]

    @classmethod
    def prompt_test_input_from_cli(cls):
        Screen.reset_screen()
        get_test_input_from_cli = \
            input("There are two different ways a java source file.py can recieve input, the input can come from command\n"
                  "line arguments (ex. java HelloWorld arg1 arg2) or it can come from internal prompts (think Scanner\n"
                  "class). Here we'll decide which method the script should use.\n\n"
                  "Should input be fed as command line arguments? (y/n) : ")
        return get_test_input_from_cli