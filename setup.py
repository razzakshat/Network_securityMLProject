from setuptools import find_packages,setup
from typing import List

requirement_lst:List[str] = []

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """

    try:
        with open('requirement.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement =line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_lst


print(get_requirements())

setup (
    name="NetworkSecurity",
    version="0.0.1",
    author="Akshat Raj",
    author_email="akshatraj0721@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)





    