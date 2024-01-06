from setuptools import setup, find_packages

setup(
    name='hunterapi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Eugeniy Kolodko',
    author_email='evgeniykolodko@gmail.com',
    description='Python client for Hunter.io API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)