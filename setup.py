
import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


with open(
        os.path.join(
            os.path.dirname(__file__),
            'androidbazaar', '__init__.py')) as v_file:
    VERSION = re.compile(
        r".*__version__ = '(.*?)'",
        re.S).match(v_file.read()).group(1)

testpkgs = [
]

install_requires = [
    "opencv-python"
]

setup(
    name='mood_detection',
    version=VERSION,
    description='',
    author='Amin Etesamian',
    author_email='',
    url='https://github.com/eteamin/mood_detection',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
)