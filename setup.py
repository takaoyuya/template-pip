import setuptools

setuptools.setup(
    name='template-pip',    # package name
    version='0.0.1',        # package version
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "template-pip=src.main:greet",  # command name
        ]
    }
)
