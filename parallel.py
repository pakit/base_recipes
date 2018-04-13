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
            'unstable': Archive('https://ftp.gnu.org/gnu/parallel/'
                                'parallel-20180322.tar.bz2',
                                hash='6389ad5318247ea28a8e9ddc9e69bc2713ae5c'
                                '19e3783edda81da54ff6356497')
        }
        self.repos['stable'] = self.repos['unstable']

    def build(self):
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('parallel --version').output()
        assert lines[0].find('GNU parallel') != -1
