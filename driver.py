from testr.testr import *
from testr.screen import *


def driver():
    testr_configuration = TestrConfiguration()
    testr_configuration.get_user_input()

    for subDirectories, directories, files in os.walk(testr_configuration.working_directory):
        for directory in directories:
            testr = Testr(testr_configuration, testr_configuration.working_directory + '/' + directory.title())
            if len(testr.comment_files) > 0:
                if testr.path_to_source_file != "":
                    if testr.path_to_test_file != "":
                    	if not testr.compiled_successfully:
                            Screen.PrintInColor.yellow(message="WARNING -> Compiler error(s) on file(s) in '" + File.remove_path_from_file_name(testr.working_directory) + "'")
                    	if WordDocument.assemble_feedback_document_txt(testr=testr, directory_of_template=testr_configuration.working_directory + '/Feedback.docx'):
                            Screen.PrintInColor.green(message="SUCCESS -> successfully tested '" + File.remove_path_from_file_name(testr.working_directory) + "'\n")
                    	else:
                            Screen.PrintInColor.red(message="ERROR -> Problem creating feedback document in '" + File.remove_path_from_file_name(testr.working_directory) + "'\n")
                    else:
                        Screen.PrintInColor.red(message="ERROR -> Could not find test file in '" + File.remove_path_from_file_name(testr.working_directory) + "'\n")
                else:
                    Screen.PrintInColor.red(message="ERROR -> Could not find source file in '" + File.remove_path_from_file_name(testr.working_directory) + "'\n")
            else:
                Screen.PrintInColor.red(message="ERROR -> No comment file in '" + File.remove_path_from_file_name(testr.working_directory) + "'\n")

driver()
