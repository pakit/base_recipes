""" Formula for building libzlib """
import os

from pakit import Archive, Recipe


class Libpcre(Recipe):
    """
    The pcre regular expression library.
    """
    def __init__(self):
        super(Libpcre, self).__init__()
        self.homepage = 'http://www.pcre.org/'
        self.repos = {
            'stable': Archive('ftp://ftp.csx.cam.ac.uk/pub/software/'
                              'programming/pcre/pcre-8.38.tar.gz',
                              hash='9883e419c336c63b0cb5202b09537c140966d5'
                              '85e4d0da66147dc513da13e629')
        }
        self.opts = {
            'configure': '--enable-unicode-properties --enable-pcre16 '
                         '--enable-pcre32'
        }

    def build(self):
        self.cmd('./configure  --prefix={prefix} {configure}')
        self.cmd('make')
        self.cmd('make install')

    def verify(self):
        libpath = os.path.join(self.opts['link'], 'lib', 'libpcre.a')
        assert os.path.exists(libpath)
