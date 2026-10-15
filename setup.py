'''
The setup.py file is used for packaging and distributing Python projects. It contains metadata about the project, such as its name, version, author, and dependencies. This file is essential for creating a distributable package that can be installed using tools like pip.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            ##Read line from the file
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
            print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Bipin Yadav",
    author_email="yadavbipin79817@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)