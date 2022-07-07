""" Formula for building neovim """
from pakit import Git, Recipe


class Neovim(Recipe):
    """
    The mode based terminal editor for programmers.

    By default built with lua & python 2.x interpreters.
    """
    def __init__(self):
        super(Neovim, self).__init__()
        self.src = 'https://github.com/neovim/neovim'
        self.homepage = 'https://neovim.io'
        self.repos = {
            'unstable': Git(self.src),
        }
        self.repos['stable'] = self.repos['unstable']

    def build(self):
        self.cmd('make -j CMAKE_EXTRA_FLAGS="-DCMAKE_BUILD_TYPE=RelWithDebInfo '
                 '-DCMAKE_INSTALL_PREFIX={prefix}"')
        self.cmd('make install')

    def verify(self):
        lines = self.cmd('nvim --version').output()
        assert lines[0].find('NVIM') != -1
        assert lines[1].find('RelWithDebInfo') != -1
