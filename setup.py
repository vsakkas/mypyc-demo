from setuptools import setup

from mypyc.build import mypycify

setup(
    name="mypyc-demo",
    packages=["src"],
    ext_modules=mypycify(
        [
            "src/main.py",
            "src/utilities/utils.py",
            "src/utilities/__init__.py",
        ]
    ),
)
