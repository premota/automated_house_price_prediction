from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    Read a requirements.txt file and return a list of requirements.

    Parameters:
    - file_path (str): The path to the requirements.txt file.

    Returns:
    - List[str]: A list of strings representing the requirements.
    """

    requirements = []
    editable = "-e ."
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readline()
            requirements = [req.replace("\n", "") for req in requirements]

            # to make sure '-e .' in requirement.txt is removed from list if present
            if editable in requirements:
                requirements.remove(editable)
    #exception block
    except FileNotFoundError:
        print(f'file not found: {file_path}')
    except Exception as e:
        print(f"An error occurred: {e}")

    return requirements




setup(
name = "automated_house_price_prediction",
version = "0.0.1",
author = "asemota",
author_email = "premota101@gmail.com",
packages= find_packages(),
install_requires = get_requirements('requirements.txt')

)