from setuptools import setup

setup(
    name='hidapi-usb',
    version="0.2.4",
    description=("CFFI wrapper for hidapi with changes by flok"),
    author="Florian K",
    url="https://github.com/flok/hidapi-cffi.git",
    author_email="37000563+flok@users.noreply.github.com",
    license='BSD',
    py_modules=['hidapi'],
    setup_requires=['cffi >= 1.14.4']
)
