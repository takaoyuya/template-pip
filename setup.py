import setuptools

setuptools.setup(
    name='my-pip',
    version='0.0.1',
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "m-pip=src.main:greet",
        ]
    }
)
