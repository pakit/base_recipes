""" Formula for building libzlib """
import os

from pakit import Git, Recipe


class Libz(Recipe):
    """
    The zlib compression library.
    """
    def __init__(self):
        super(Libz, self).__init__()
        self.src = 'https://github.com/madler/zlib'
        self.homepage = self.src
        self.repos = {
            'stable': Git(self.src, tag='v1.2.8'),
            'unstable': Git(self.src),
        }

    def build(self):
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make')
        self.cmd('make install')

    def verify(self):
        libpath = os.path.join(self.opts['link'], 'lib', 'libz.a')
        assert os.path.exists(libpath)
