from setuptools import setup

setup(
    name='zeitdoro',
    version='0.1',
    py_modules=['zeitdoro'],
    install_requires=[
        'Click',
        'Flask',
        'Requests'
    ],
    entry_points='''
        [console_scripts]
        zeitdoro=cli:cli
    ''',
)
