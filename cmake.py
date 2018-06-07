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
            'stable': Archive('http://www.cmake.org/files/v3.11/'
                              'cmake-3.11.3.tar.gz',
                              hash='287135b6beb7ffc1ccd02707271080bbf14c21'
                              'd80c067ae2c0040e5f3508c39a'),
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
