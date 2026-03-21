from setuptools import setup, find_packages

setup(
    name='dab_project',
    version='0.0.3',
    description='This contains the src code',
    author="Harish",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'setuptools'
    ]
)