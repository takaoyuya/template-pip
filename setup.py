import setuptools

setuptools.setup(
    name='template-pip',
    version='0.0.1',
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "template-pip=src.main:greet",
        ]
    }
)
