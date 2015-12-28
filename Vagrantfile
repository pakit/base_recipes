# -*- mode: ruby -*-
# vi: set ft=ruby :

# Recommended pugins:
#   vagrant plugin install vagrant-cachier
# Caches package installation to a folder under ~/.vagrant.d
#
#   vagrant plugin install vagrant-faster
# Sets cpu/memory to a good value above default, speeds up VM.

$root = <<EOF
sudo apt-get update -y
sudo apt-get install -y build-essential automake autopoint autoconf pkg-config cmake\
 git mercurial vim rar p7zip-full python-dev python-pip  pandoc sphinx-common\
 libyaml-dev libpcre3-dev zlib1g-dev liblzma-dev
EOF

$user = <<EOF
# Purely optional & slow, sets up a dev environment
if [ ! -e ~/.my_scripts ]; then
    git clone --depth 1 https://github.com/starcraftman/.my_scripts/ ~/.my_scripts
    rm ~/.bashrc
    python .my_scripts/SysInstall.py home_save home
    sed --in-place -e "s/Plug 'Valloric.*//" ~/.vimrc
    echo "vim +Bootstrap +qa >/dev/null 2>&1"
    vim +Bootstrap +qa >/dev/null 2>&1
    echo "vim +PlugInstall +qa >/dev/null 2>&1"
    vim +PlugInstall +qa >/dev/null 2>&1
fi

# Setup pakit
rm -rf ~/pakit
git clone https://github.com/starcraftman/pakit.git ~/pakit
if  ! grep 'pakit/bin'  ~/.lbashrc; then
    echo 'Adding pakit to local bashrc.'
    echo 'export PATH=$HOME/pakit/bin:$PATH' >> ~/.lbashrc
    echo 'export PYTHONPATH=$HOME/pakit:$PYTHONPATH' >> ~/.lbashrc
fi
pip install --upgrade argparse pyyaml coverage flake8 mock pytest tox
python ~/pakit/setup.py release

# Further setup
ln -fs /vagrant ~/recipes
git clone https://github.com/pakit/pakit_tests.git ~/pakit_tests
if  ! grep 'pakit_tests'  ~/.lbashrc; then
    echo 'Adding pakit_tests to local bashrc.'
    echo 'export PATH=$HOME/pakit_tests:$PATH' >> ~/.lbashrc
fi

source ~/.lbashrc
EOF

Vagrant.require_version ">= 1.5.0"

VAGRANTFILE_API_VERSION = 2
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "boxcutter-VAGRANTSLASH-ubuntu1510"

  config.vm.provider :virtualbox do |v|
    # You may want to modify these if you don't use vagrant-faster
    #v.cpus = 4
    #v.memory = 4096
    v.customize ["modifyvm", :id, '--chipset', 'ich9'] # solves kernel panic issue on some host machines
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  if Vagrant.has_plugin?("vagrant-cachier")
    # Configure cached packages to be shared between instances of the same base box.
    # More info on http://fgrehm.viewdocs.io/vagrant-cachier/usage
    config.cache.scope = :box
  end

  config.vm.provision :shell, :inline => $root
  config.vm.provision :shell, :inline => $user, privileged: false
end
