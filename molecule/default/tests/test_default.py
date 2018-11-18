import os

# https://testinfra.readthedocs.io/en/latest/
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

# zpool tool available

# zfs tool available

# zfs kernel module is loaded

# can create pools

# can create datapath

# Can snapshot datapath

# Can clone snapshot
