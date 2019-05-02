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
            'stable': Archive('https://github.com/Kitware/CMake/releases/download/v3.14.3/'
                              'cmake-3.14.3.tar.gz',
                              hash='215d0b64e81307182b29b63e562edf30b'
                              '3875b834efdad09b3fcb5a7d2f4b632'),
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
