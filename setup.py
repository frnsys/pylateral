from setuptools import setup, find_packages

setup(
    name='lateral',
    version='0.0.2',
    description='python interface to Lateral\'s APIs',
    url='https://github.com/ftzeng/lateral',
    author='Francis Tseng',
    author_email='f@frnsys.com',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)