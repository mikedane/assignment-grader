import glob



class File(object):

    @classmethod
    def get_files_in_directory(cls, directory=None, file_extension=None, file_name=None):
        list_of_files = []
        if directory is None:
            if file_extension is None and file_name is None:
                list_of_files = glob.glob('*.*')
            elif file_extension is None and file_name is not None:
                list_of_files = glob.glob(file_name + '.*')
            elif file_extension is not None and file_name is None:
                list_of_files = glob.glob('*.' + file_extension)
            elif file_extension is not None and file_name is not None:
                list_of_files = glob.glob(file_name + '.' + file_extension)
        else:
            if file_extension is None and file_name is None:
                list_of_files = glob.glob(directory + '/*.*')
            elif file_extension is None and file_name is not None:
                list_of_files = glob.glob(directory + '/' + file_name + '.*')
            elif file_extension is not None and file_name is None:
                list_of_files = glob.glob(directory + '/*' + '.' + file_extension)
            elif file_extension is not None and file_name is not None:
                list_of_files = glob.glob(directory + '/' + file_name + '.' + file_extension)
        return list_of_files

    @classmethod
    def remove_path_from_file_name(cls, file_name):
        new_file_name = file_name[file_name.rfind('/') + 1:]
        return new_file_name

    @classmethod
    def remove_path_from_file_names_in_list(cls, list_of_file_names):
        new_list_of_file_names = []
        for file_name in list_of_file_names:
            new_list_of_file_names.append(cls.remove_path_from_file_name(file_name=file_name))
        return new_list_of_file_names

    @classmethod
    def get_path_from_file_name(cls, file_name):
        file_path = file_name[:file_name.rfind('/') + 1]
        return file_path

    @classmethod
    def remove_extension_from_file_name(cls, file_name):
        raw_file_name = file_name[:file_name.rfind('.')]
        return raw_file_name

    @classmethod
    def file_exists_in_directory(cls, directory, file_name):
        file_exists = False
        list_of_files_in_directory = cls.get_files_in_directory(directory=directory)
        if file_name in cls.remove_path_from_file_names_in_list(list_of_file_names=list_of_files_in_directory):
            file_exists = True
        return file_exists

    @classmethod
    def find_existing_file_in_list(cls, directory, list_of_file_names):
        file_name = ""
        i = 0
        while i < len(list_of_file_names) and file_name == "":
            if cls.file_exists_in_directory(directory=directory, file_name=list_of_file_names[i]):
                file_name = list_of_file_names[i]
            i += 1
        return file_name

    @classmethod
    def get_text_from_file(cls, file_path):
        with open(file_path, 'r') as open_file:
            text_from_file = open_file.read()
            open_file.close()
            return text_from_file
