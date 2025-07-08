# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

# Define testcases
# format:
#   <message prefix before testcase>,
#   <basedir for testcases>
#   <subdir case to append to basedir>
testcases = [
    ["Result for current directory:", "calculator", "."],
    ["Result for 'pkg' directory:", "calculator", "pkg"],
    ["Result for '/bin' directory:", "calculator", "/bin"],
    ["Result for '../' directory:", "calculator", "../"]
    ]

for case in testcases:
    message, baseDir, subDir = case
    print(message)
    result = get_files_info(baseDir, subDir)
    if result != None:
        print(result)
