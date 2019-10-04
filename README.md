# change-package-android

Python3 script for change package name to your Android projects or modules

Tested on Ubuntu 16.04. Python 3.5.2

Should work on Mac and Windows (not tested)

#Usage

1 - Execute script:
  arguments:
    1 - module path
    2 - new package name

```
python3 change_package.py modulepath newpackagename

//Example
python3 change_package.py /home/pedro/myproject/app com.pedro.example
```

2 - Rebuild your project

#Note

Projects with NDK not supported (script work but you need change NDK files yourself).

