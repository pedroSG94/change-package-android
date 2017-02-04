# change-package-android

Python3 script for change package name to your Android projects or modules

Tested on Ubuntu 16.04. Python 3.5.2

Should work on Mac and Windows (not tested)

#Usage

1- Put the script in your app  or module folder in your project

2- Execute the script

Normal execute:

```
python3 change_package.py com.example.pedro com.company.project
```

If you use proguard:

```
python3 change_package.py com.example.pedro com.company.project myproguardname.pro
```

3- Rebuild your project

#Note

Projects with NDK not supported (script work but you need change NDK youself).

