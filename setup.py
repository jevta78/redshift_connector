from setuptools import find_packages, setup

setup(
    name='redshift_connector',
    packages=find_packages(include=['redshift_connector']),
    version='0.1.0',
    description='Connector to redshift db',
    author='Nikola Jevtic',
    license='MIT',
    install_requires=['psycopg2'],
    test_suite='tests',
)