import os
import sys

old_package = sys.argv[1]
new_package = sys.argv[2]

def show_arguments():
	print("Old package: " + old_package)
	print("New package: " + new_package)

def replace_text(path_file, old_text, new_text):
	f = open(path_file, "r")
	file_text = f.read()
	f.close()
	t = file_text.replace(old_text, new_text)
	f = open(path_file, "w")
	f.write(t)
	f.close()

def list_folder(path_folder):
	print("current directory: " + path_folder)
	
	for f in os.listdir(path_folder):
		print("file " + str(f))

		#is a folder
		if os.path.isdir(path_folder + "/" + f):
			abs_path = os.path.abspath(path_folder + os.sep + str(f))
			if(str(f) != "build"):
				list_folder(abs_path)
			for i in range(len(old_package.split("."))):
				if(str(f) == old_package.split(".")[i]):
					os.rename(path_folder + os.sep + str(f), path_folder + os.sep + new_package.split(".")[i])

		#is a file
		else:
			#only change java and xml files
			if(str(f).endswith(".java") or str(f).endswith(".xml")):
				replace_text(path_folder + os.sep + str(f), old_package, new_package)
			else:
				print("ignore this file")

show_arguments()
list_folder(os.path.abspath("."))
print("finished")
