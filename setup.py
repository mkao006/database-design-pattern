import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbdp",
    version="0.0.1",
    author="Michael Kao",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'boto3',
        'pyyaml',
        'keyring',
        'pandas',        
        'sqlalchemy',
        'pyodbc',
        'psycopg2-binary',
        'pandas-gbq',
        'google-cloud-bigquery'
    ]
)
