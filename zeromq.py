""" Formula for building zeromq """
from pakit import Archive, Recipe


class Zeromq(Recipe):
    """
    Library for standard inter language connections.
    """
    def __init__(self):
        super(Zeromq, self).__init__()
        self.src = 'https://github.com/zeromq/libzmq'
        self.homepage = 'http://zeromq.org'
        archive = Archive('https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz',
                          hash='27d1e82a099228ee85a7ddb2260f40830212402c605a4a10b5e5498a7e0e9d03')
        self.repos = {
            'stable': archive,
            'unstable': archive,
        }

    def build(self):
        self.cmd('./autogen.sh')
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make -j 4 all')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('curve_keygen').output()
        assert lines[0].find('CurveZMQ keypair') != -1
