from setuptools import setup, find_packages

setup(
    name='hat',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA recursion and sorting function',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/VanesseB/hat.git',
    author='Vanesse Mngomezulu',
    author_email='vanessesetsoalo@gmail.com'
)
