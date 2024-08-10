from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-E .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sunesh',
author_email='suneshagarwal995@gmail.com',
packages=find_packages(),
install_requiers=get_requirements('requirements.txt')

)