from setuptools import find_packages, setup

setup(
    name='studentbook',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
		'Click==7.0',
		'Flask==1.0.2',
		'Flask-WTF==0.14.2',
		'itsdangerous==1.1.0',
		'Jinja2==2.10',
		'MarkupSafe==1.1.1',
		'Werkzeug==0.14.1',
		'WTForms==2.2.1',

    ],
)