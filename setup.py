from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """this function takes requirements.txt file path and returns the list of requirements

    Args:
        file_path (str): file path for requirements

    Returns:
        List[str]: List of Libraries to Install
    """    
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_read:
        requirements = file_read.readlines()
        requirements = [req.rstrip("\n") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlops-demo",
    version="0.0.1",
    description="A Short and Concise Demo of MLops flow",
    author="ravi",
    author_email="ravi.0531.rp@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
