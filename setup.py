from setuptools import find_packages, setup

import dao

long_description = open("README.md", encoding="utf8").read()
requirements = [line.strip() for line in open("requirements.txt", encoding="utf8").readlines()]

setup(
    name='dao',
    version=str(dao.__version__),
    description='道可道，非常道',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='dao',
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    url='https://github.com/dao-lang/dao-python',
    author='killf',
    entry_points={
        'console_scripts': ['dao=dao.main:main'],
        'gui_scripts': []
    }
)
