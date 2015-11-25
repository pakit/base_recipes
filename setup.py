"""
The setup file for packaging pakit
"""
from __future__ import absolute_import, print_function

import os
import shlex
import shutil
import subprocess
from setuptools import setup
# from setuptools import setup, find_packages, Command
# from setuptools.command.test import test as TestCommand

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
TEST_DEPS = ['flake8', 'mock', 'pylint', 'pytest', 'tox']
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

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',
    ],

    # What does your project relate to?
    keywords='development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['venv', 'test*']),
    packages=[MODULE],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=TEST_DEPS,

    tests_require=TEST_DEPS,

    # # List additional groups of dependencies here (e.g. development
    # # dependencies). You can install these using the following syntax,
    # # for example:
    # # $ pip install -e .[dev,test]
    # extras_require={
        # 'dev': ['pyandoc'],
        # 'test': TEST_DEPS,
    # },

    # # If there are data files included in your packages that need to be
    # # installed, specify them here.  If using Python 2.6 or less, then these
    # # have to be included in MANIFEST.in as well.
    # package_data={
        # '': MODULES,
    # },

    # # Although 'package_data' is the preferred approach, in some case you may
    # # need to place data files outside of your packages. See:
    # # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
        # 'console_scripts': [
            # 'pakit = pakit.main:main',
        # ],
    # },

    # cmdclass={
        # 'clean': CleanCommand,
        # 'deps': InstallDeps,
        # 'release': ReleaseCommand,
        # 'test': PyTest,
    # }
)
