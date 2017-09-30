import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ntp_package(Package):
    assert Package("ntp").is_installed


def test_ntp_file(File):
    f = File("/etc/ntp.conf")
    assert f.exists
    assert f.is_file


def test_ntp_file_content(File):
    f = File("/etc/ntp.conf")
    assert f.contains("0.us.pool.ntp.org")


def test_ntp_service(Service, SystemInfo):
    if SystemInfo.distribution == "debian":
        ntp_daemon = "ntp"
    elif SystemInfo.distribution == "centos":
        ntp_daemon = "ntpd"

    s = Service(ntp_daemon)
    assert s.is_running
    assert s.is_enabled
