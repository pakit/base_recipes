""" Formula for building git """
from pakit import Archive, Recipe
from pakit import Git as GitRepo


class Git(Recipe):
    """
    The git distributed version control system
    """
    def __init__(self):
        super(Git, self).__init__()
        self.homepage = 'https://git-scm.com'
        self.repos = {
            'stable': Archive('https://www.kernel.org/pub/software/scm/git/'
                              'git-2.9.4.tar.xz',
                              hash='6c7e18ce9eb6fffe75704b3fde286c32210e831'
                              '75e03b75cb08952d5fb319018'),
            'unstable': GitRepo('https://github.com/git/git'),
        }

    def build(self):
        self.cmd('make configure')
        self.cmd('./configure --prefix={prefix}')
        self.cmd('make')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('git --version').output()
        assert lines[0].find('git version') != -1
