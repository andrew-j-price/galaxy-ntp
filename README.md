# galaxy-ntp
NTP Ansible Galaxy role tested via Molecule

### Commands
```
# virtualenv init
virtualenv -p /usr/local/bin/python2.7 ~/venv-molecule
source ~/venv-molecule/bin/activate
pip install -r test_requirements.txt

# Ansible Galaxy init
ansible-galaxy init galaxy-ntp -f

# Molecule init
molecule init --driver docker --verifier testinfra
```

### Resources
  - http://giovannitorres.me/testing-ansible-roles-with-molecule-testinfra-and-vagrant.html
