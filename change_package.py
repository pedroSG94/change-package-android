import os
import sys

old_package = sys.argv[1]
new_package = sys.argv[2]

def show_arguments():
	print("old package: " + old_package)
	print("new package: " + new_package)

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

		#es una carpeta
		if os.path.isdir(path_folder + "/" + f):
			abs_path = os.path.abspath(path_folder + "/" + str(f))
			if(str(f) != "build"):
				list_folder(abs_path)
			for i in range(len(old_package.split("."))):
				if(str(f) == old_package.split(".")[i]):
					os.rename(path_folder + "/" + str(f), path_folder + "/" + new_package.split(".")[i])

		#es un fichero que no es el mismo script
		elif str(f) != "files.py":
			if(str(f).endswith(".java") or str(f).endswith(".xml")):
				replace_text(path_folder + "/" + str(f), old_package, new_package)
			else:
				print("ignore this file")

show_arguments()
list_folder(os.path.abspath("."))
print("finished")
