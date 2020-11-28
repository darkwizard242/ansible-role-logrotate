import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'logrotate'
PACKAGE_BINARY = '/usr/sbin/logrotate'


def test_logrotate_package_installed(host):
    """
    Tests if logrotate package is installed.
    """
    assert host.package("logrotate").is_installed


def test_logrotate_binary_exists(host):
    """
    Tests if logrotate binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_logrotate_binary_file(host):
    """
    Tests if logrotate binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_logrotate_binary_which(host):
    """
    Tests the output to confirm logrotate's binary location.
    """
    assert host.check_output('which logrotate') == PACKAGE_BINARY
