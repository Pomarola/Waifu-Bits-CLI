from setuptools import setup, find_packages

setup(
    name="waifu-bits",
    version="1.0",
    packages=find_packages(),  # finds the WaifuBits package and submodules
    install_requires=[
        "urwid",
        "python-dotenv",
    ],
    include_package_data=True,  # this line
    package_data={
        "WaifuBits": [".env"],  # and this line
    },
    entry_points={
        "console_scripts": [
            "waifu-bits=WaifuBits.main:main"  # assuming main() is inside WaifuBits/main.py
        ]
    },
)