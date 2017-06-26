import os

def fileids_under_dir(dirname=None, file_extension=''):
    files_name_list = [line.strip().split(file_extension)[0] for line in os.listdir(dirname) if line.endswith(file_extension)]
    return files_name_list

def fileids_under_dir_v2(dirname=None, file_extension='', excluding=''):
    files_name_list = [line.strip().split(file_extension)[0] for line in os.listdir(dirname) if line.endswith(file_extension) and excluding not in line]
    return files_name_list
          
def files_under_dir(dirname=None, file_extension=''):
    files_name_list = [line.strip() for line in os.listdir(dirname) if line.endswith(file_extension)]
    return files_name_list

def dirs_under_top_dir(dirname=None,dir_check=False):
    if dir_check:
        files_name_list = [line.strip() for line in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,line))]
    else:
        files_name_list = [line.strip() for line in os.listdir(dirname)]
    return files_name_list


def abs_files_under_dir(dirname=None, file_extension=''):
    files_abs_name_list = [os.path.join(dirname,line.strip()) for line in os.listdir(dirname) if line.endswith(file_extension)]
    return files_abs_name_list

def abs_files_under_dir_v2(dirname=None, file_extension='', excluding=''):
    files_abs_name_list = [os.path.join(dirname,line.strip()) for line in os.listdir(dirname) if line.endswith(file_extension) and excluding not in line]
    return files_abs_name_list

def matching_abs_files(dirname_s=None, file_extension_s='', dirname_t=None, file_extension_t=''):
    fileids = fileids_under_dir(dirname=dirname_s, file_extension=file_extension_s)
    files1 = [os.path.join(dirname_s, line+file_extension_s) for line in fileids]
    files2 = [os.path.join(dirname_t, line+file_extension_t) for line in fileids]
    return files1, files2

def matching_abs_existing_files(dirname_s=None, file_extension_s='', dirname_t=None, file_extension_t=''):
    fileids = [fileids_under_dir()] 
