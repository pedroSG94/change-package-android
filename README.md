# change-package-android

Python3 script for change package name in your android project

Tested on Ubuntu 16.04. Python 3.5.2

#Usage

1- Put the script in your app folder under your project

2- Execute the script

```
python3 change_package.py com.example.pedro com.company.project
```

3- Rebuild your project

#Note

Only work with same length package, example:

com.example.pedro (length 3)

com.company.android.project (length 4)

Supported
```
python3 change_package.py com.example.pedro com.company.project
```

Unsupported
```
python3 change_package.py com.example.pedro com.company.android.project
```
