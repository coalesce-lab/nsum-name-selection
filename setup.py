from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'nsumselect',
    version = '1.0.0',
    author = 'Adria Fenoy',
    author_email = 'fenoy.adria@gmail.com',
    maintainer = 'Michał Bojanowski',
    maintainer_email = 'michal2992@gmail.com',
    license = 'GPL 2',
    description = 'Automated sub-population selection for Network Scale-Up Method',
    url = 'https://github.com/coalesce-lab/nsum-name-selection',
    py_modules = ['main', 'src'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    package_data={
        'sample': ['data']
        },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'nsumselect=main'
            ]
        }
)
