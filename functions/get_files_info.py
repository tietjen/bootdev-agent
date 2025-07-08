import os

def get_files_info(working_directory, directory=None):
    if not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'
    
    dirPath = os.path.join(working_directory, directory)
    
    abs_base = os.path.abspath(working_directory)
    abs_path = os.path.abspath(dirPath)
    
    if not abs_path.startswith(abs_base):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(dirPath):
        return f'Error: "{directory}" is not a directory'
    
    dirEntries = os.listdir(dirPath)
    
    for entry in dirEntries:
        fullPath = os.path.abspath(os.path.join(dirPath, entry))
        fSize = os.path.getsize(fullPath)
        if os.path.isfile(fullPath):
            isFile = "False"
        else:
            isFile = "True"
            
        print(f'- {entry}: file_size={fSize} bytes, is_dir={isFile}')
    
    return