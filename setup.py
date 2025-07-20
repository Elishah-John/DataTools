from setuptools import setup, find_packages

setup(
    name='DataTools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'numpy'
    ],
    author='Elishah John',
    description='Data cleaning and visualization tools for quick analysis.',
)
