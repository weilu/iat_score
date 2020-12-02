from setuptools import setup

setup(
    name='iat-score',
    version='0.1.0',
    author='Wei Lu',
    author_email='luwei.here@gmail.com',
    packages=['iat-score', 'iat-score.test'],
    # scripts=['bin/script1','bin/script2'],
    # url='http://pypi.python.org/pypi/PackageName/',
    license='MIT',
    description='Compute IAT score & provide human readable feedback based on the score',
    long_description=open('README.md').read(),
    install_requires=[ "pandas >= 1.1.4", "pytest" ],
)