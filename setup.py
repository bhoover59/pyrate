from setuptools import setup
from ipinfo.version import SDK_VERSION

long_description = """
Plotting functions for HONO rxn rates from output of Bode Hoover's MATLAB scripts for F0AM v4.2.2
"""

setup(
    name="pyrate",
    version=SDK_VERSION,
    description="Plotting functions for HONO rxn rates",
    long_description=long_description,
    url="https://github.com/pyrate",
    author="Bode Hoover",
    author_email="bodehoov@iu.edu",
    license="Apache License 2.0",
    packages=["ipinfo", "ipinfo.cache"],
    install_requires=["requests", "cachetools", "aiohttp<=4"],
    include_package_data=True,
    zip_safe=False,
)
