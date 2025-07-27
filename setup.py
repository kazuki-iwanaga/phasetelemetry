from setuptools import find_packages, setup

setup(
    name='phasetelemetry',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "typing==3.10.0.0; python_version=='2.7'",
        "six==1.16.0",
    ],
    license='Apache-2.0',
)
