from setuptools import setup

setup(
    name='helios',
    version='0.1.2',
    py_modules=['helios'],
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'helios=helios:main',
        ],
    },
)
