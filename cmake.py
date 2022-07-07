""" Formula for building cmake """
from pakit import Archive, Git, Recipe


class Cmake(Recipe):
    """
    A cross-platform build tool for C++
    """
    def __init__(self):
        super(Cmake, self).__init__()
        self.homepage = 'www.cmake.org'
        self.repos = {
            'stable': Archive('https://github.com/Kitware/CMake/releases/download/v3.23.2/cmake-3.23.2.tar.gz',
                              hash='f316b40053466f9a416adf981efda41b160ca859e97f6a484b447ea299ff26aa'),
            'unstable': Git('git://cmake.org/cmake.git'),
        }
        self.opts = {
            'bootstrap': '--sphinx-html --sphinx-man'
        }

    def build(self):
        self.cmd('./bootstrap --prefix={prefix} --mandir=share/man '
                 '{bootstrap}')
        self.cmd('make -j')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('cmake --version').output()
        assert lines[0].find('cmake version') != -1
