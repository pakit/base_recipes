"""
The setup file for packaging pakit
"""
from __future__ import absolute_import, print_function

import os
import shlex
import shutil
import subprocess
from setuptools import setup

MODULE = 'recipes'
ROOT = os.path.abspath(os.path.dirname(__file__))
if os.path.dirname(__file__) == '':
    ROOT = os.getcwd()


def update_package():
    """
    Make a dummy package for tox.
    """
    try:
        os.makedirs(MODULE)
    except OSError:
        pass

    for fname in [mod for mod in os.listdir(ROOT) if mod[-2:] == 'py']:
        shutil.copy(fname, os.path.join(MODULE, fname))
    os.remove(os.path.join(MODULE, 'setup.py'))


def get_version():
    """
    Get a version with commit suffix.
    """
    if os.path.exists(os.path.join(ROOT, '.git')):
        return subprocess.check_output(shlex.split('git rev-parse HEAD'))
    else:
        return 'not_available'


update_package()
MY_NAME = 'Jeremy Pallats / starcraft.man'
MY_EMAIL = 'N/A'
DEPS = ['flake8', 'mock', 'pylint', 'pytest', 'tox']
setup(
    name='pakit_recipes',
    version='0.1.0-' + get_version(),
    description='Base recipes for pakit.',
    long_description='Base recipes for pakit.',
    url='https://github.com/pakit/base_recipes',
    author=MY_NAME,
    author_email=MY_EMAIL,
    maintainer=MY_NAME,
    maintainer_email=MY_EMAIL,
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',
    ],
    keywords='development',
    packages=[MODULE],
    install_requires=DEPS,
    tests_require=DEPS,
)
