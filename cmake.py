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
            'stable': Archive('https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2.tar.gz',
                              hash='e3e0fd3b23b7fb13e1a856581078e0776ffa2df4e9d3164039c36d3315e0c7f0'),
            'unstable': Git('git://cmake.org/cmake.git'),
        }
        self.opts = {
            'bootstrap': '--sphinx-html --sphinx-man'
        }

    def build(self):
        self.cmd('./bootstrap --prefix={prefix} --mandir=share/man '
                 '{bootstrap}')
        self.cmd('make')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('cmake --version').output()
        assert lines[0].find('cmake version') != -1
