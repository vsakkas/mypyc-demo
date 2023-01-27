# MyPyC Demo
Short demo to showcase how to use mypyc.

## Steps

Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install the needed dependencies:
```bash
pip install -r requirements.txt
```

Build a wheel file for the package:
```bash
python3 setup.py bdist_wheel
```

Install the wheel:
```bash
pip install dist/mypyc_demo-0.0.0-cp37-cp37m-linux_x86_64.whl
```

**NOTE:** The exact name of the wheel file will differ, depending on your platform and Python version.

You can now run the package:
```bash
python3 -m src.main

Please, type a message (or integer): _
```

When running the compiled version, you will notice that the Fibonacci calculation is now much faster compared to using the regular Python version.

**NOTE:** This was tested on Linux using Python 3.7.5. It should also work on other platforms and Python versions as well.
