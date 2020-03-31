import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_logrotate_package_installed(host):
    assert host.package("logrotate").is_installed


def test_logrotate_binary_exists(host):
    assert host.file('/usr/sbin/logrotate').exists


def test_logrotate_binary_file(host):
    assert host.file('/usr/sbin/logrotate').is_file


def test_logrotate_binary_which(host):
    assert host.check_output('which logrotate') == '/usr/sbin/logrotate'
