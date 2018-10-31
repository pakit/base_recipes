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
                                'parallel-20181022.tar.bz2',
                                hash='2e84dee3556cbb8f6a3794f5b21549faffb132'
                                'db3fc68e2e95922963adcbdbec')

        }
        self.repos['stable'] = self.repos['unstable']

    def build(self):
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('parallel --version').output()
        assert lines[0].find('GNU parallel') != -1
