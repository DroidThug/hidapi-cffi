from setuptools import setup

setup(
    name='hidapi-usb',
    version="0.3.1",
    description=("CFFI wrapper for hidapi with changes by flok"),
    author="Florian K",
    url="https://github.com/flok/hidapi-cffi.git",
    author_email="37000563+flok@users.noreply.github.com",
    license='BSD',
    py_modules=['hidapi'],
    install_requires=['cffi']
)
