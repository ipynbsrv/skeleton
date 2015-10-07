import os
from setuptools import setup, find_packages

setup(
    name="coco-skeleton",
    description="Project skeleton for coco Python packages.",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['coco'],
    install_requires=[],
)
