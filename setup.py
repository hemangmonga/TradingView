from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='TradingView',
    version='0.0.15',
    description='Unofficial API to fetch live and historical data from TradingView.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hemang Monga',
    packages=find_packages(),
    install_requires=[],
)
