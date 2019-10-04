import os
import sys
import shutil

package_separator = "."
# arguments
initial_folder = sys.argv[1]
new_package = sys.argv[2]


def get_old_package():
    build_file = initial_folder + os.sep + "build.gradle"
    f = open(build_file, "r")
    file_text = f.read()
    for line in file_text.split("\n"):
        if "applicationId" in line.strip():
            return line.strip().split(" ")[1].strip().replace("\"", "")
    return None


def show_arguments(old_package):
    print("old package: " + old_package)
    print("new package: " + new_package)


def check_original_route(old_package):
    print("checking original package...")
    original_route = initial_folder + os.sep + "src" + os.sep + "main" + os.sep + "java" + os.sep + old_package.replace(
        package_separator, os.sep)
    if os.path.isdir(original_route):
        print("original folder exists")
    else:
        print("original folder not found, write a correct original package")
        sys.exit()


def replace_text(path_file, old_text, new_text):
    f = open(path_file, "r")
    try:
        file_text = f.read()
        f.close()
        t = file_text.replace(old_text, new_text)
        f = open(path_file, "w")
        f.write(t)
        f.close()
    except UnicodeDecodeError:  # This file is not text plain
        f.close()


def change_files(path_folder, old_package):
    print("current directory: " + path_folder)

    for f in os.listdir(path_folder):
        print("file " + str(f))
        # is a folder
        if os.path.isdir(path_folder + os.sep + f):
            abs_path = os.path.abspath(path_folder + os.sep + str(f))
            # ignore build folder
            if str(f) is not "build":
                change_files(abs_path, old_package)
        # is a file
        else:
            replace_text(path_folder + os.sep + str(f), old_package, new_package)


def move_code_folder(folder_name, old_package):
    original_route = initial_folder + os.sep + "src" + os.sep + folder_name + os.sep + "java" + os.sep + old_package.replace(
        package_separator, os.sep)
    destiny_route = initial_folder + os.sep + "src" + os.sep + folder_name + os.sep + "java" + os.sep + new_package.replace(
        package_separator, os.sep)
    shutil.move(original_route, initial_folder + os.sep + "my_temporal_folder")
    shutil.rmtree(initial_folder + os.sep + "src" + os.sep + folder_name + os.sep + "java" + os.sep)
    print("new java route: " + destiny_route)
    shutil.move(initial_folder + os.sep + "my_temporal_folder", destiny_route)


def move_folders(old_package):
    path_folder = initial_folder + os.sep + "src"
    for f in os.listdir(path_folder):
        if os.path.isdir(path_folder + os.sep + f):
            move_code_folder(str(f), old_package)


def init_script():
    old_package = get_old_package()
    if old_package is not None:
        show_arguments(old_package)
        check_original_route(old_package)
        change_files(initial_folder, old_package)
        move_folders(old_package)
        print("finished success")
    else:
        print("applicationId not found in app/build.gradle")


init_script()
