""" Formula for building parallel """
from pakit import Archive, Recipe


class Parallel(Recipe):
    """
    GNU parallel executes shell jobs in parallel
    """
    def __init__(self):
        super(Parallel, self).__init__()
        self.homepage = 'http://www.gnu.org/software/parallel'
        self.repos = {
            'unstable': Archive('http://ftp.gnu.org/gnu/parallel/'
                              'parallel-20170422.tar.bz2',
                              hash='7a2438a92692c662dae3d4e80f1190af4cfe52'
                              '7cd3fb1a0d14e07f5c110ed329')
        }
        self.repos['stable'] = self.repos['unstable']

    def build(self):
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('parallel --version').output()
        assert lines[0].find('GNU parallel') != -1
