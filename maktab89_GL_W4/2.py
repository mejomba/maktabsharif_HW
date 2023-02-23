import os


class OsUtils:

    @staticmethod
    def generate_file(file_name):
        if os.path.exists(file_name):
            print(f'file {file_name} already exist.')
        else:
            os.system(f'touch {file_name}')

    @staticmethod
    def generate_directory(path, directory_name):
        if path:
            path = path.strip('/')
            os.system(f'mkdir {path}/{directory_name}')
        else:
            os.system(f'mkdir {directory_name}')

    @staticmethod
    def file_directory_list(directory_name):
        # os.system(f'ls {directory_name}')
        out = os.popen(f'ls {directory_name}').read()
        print(out)

    @staticmethod
    def edit_name(old_file_path_name, new_file_path_name):
        os.rename(old_file_path_name, new_file_path_name)

    @staticmethod
    def move_file(source, destination):
        os.system(f'mv {source} {destination}')

    @staticmethod
    def copy_file(source, destination):
        os.system(f'cp {source} {destination}')

    @staticmethod
    def delete_file(file_name):
        os.system(f'rm {file_name}')

    @staticmethod
    def delete_directory(directory_name):
        os.system(f'rm -r {directory_name}')
        # os.removedirs(directory_name)


# OsUtils.generate_file('salam.py')
# OsUtils.delete_file('salam.py')
# OsUtils.copy_file('test2.py', 'quize/')
# OsUtils.generate_directory('', 'jafar')
OsUtils.file_directory_list('')
# OsUtils.edit_name('salam.py', '01_simple_get_post.py')
# OsUtils.delete_directory('../jafar')



# print(os.path.exists())