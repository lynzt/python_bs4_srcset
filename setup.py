from setuptools import setup, find_packages

print find_packages()
setup(name='python_bs4_srcset',
    version='0.0.1',
    description='return an image_url of an image srcset',
    author='lynzt',
    url='https://github.com/lynzt/python_bs4_srcset',
    packages=['bs4_srcsets'],
    install_requires=['bs4'],
    )
