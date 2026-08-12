## Modules

is simple .py extension file with functions, classes and property which can be imported on other python files and can invoke
Flat structure
Example: math, os, sys


calculator.py
def sum(a, b):
  return (a+b)

main.py
import calculator

print(calculator.sum(10,20))

## Packages
is combination of multiple modules inside some specific directories and have __init__.py file inside which contains all logic that need to be run during import of the package.

my_project/
│
└── my_package/                <-- The Package
    ├── __init__.py            <-- Initialization file
    ├── math_utils.py          <-- Module A
    └── string_utils.py        <-- Module B

You can access modules inside a package using the import statement in several ways:
Dot syntax:
  import my_package.math_utils
From syntax (cleaner): 
  from my_package import math_utils
Direct function import: 
  from my_package.math_utils import add_numbers

## name == main

we use __name___ == "__main__" in order to group all codes that should be executed only when that particular python files gets executed directly. 
If you import a python which has __name__ == __main__ condition and try to invoke, code under that condition won't be executed since that python file was imported and called , not executed directly

## Virtual Envs & pip 
pip install <package-name>==<version>
pip list --> to get all installed packages

To update
pip install -U <package-name>

To uninstall
pip uninstall <package-name>

to show dependencies of any package
pip show <package-name>

Venv --> to create isolation for applications, so that multiple application can run with different versions of dependencies in parallel

python -m venv .venv --> Inside directory where we need to create

To activate 
source .venv/Scripts/activate

to deactivate the environment
deactivate

