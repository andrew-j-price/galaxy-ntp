import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ntp_is_installed(host):
    ntp = host.package("ntp")
    assert ntp.is_installed


def test_ntp_file(host):
    f = host.file("/etc/ntp.conf")
    assert f.exists
    assert f.is_file
    assert f.contains("0.us.pool.ntp.org")


# def return_daemon(distro):
#    if distro == "debian":
#        return("ntp")
#    elif distro == "centos":
#        return("ntpd")
#
#
# def test_ntp_service(Service, SystemInfo):
#    ntp_daemon = return_daemon(SystemInfo.distribution)
#    s = Service(str(ntp_daemon))
#    assert s.is_running
#    assert s.is_enabled
