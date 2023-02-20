from paramiko import SSHClient, AutoAddPolicy

hosts = ['13.127.160.219', 
         '13.127.160.220',
         '13.127.160.221']

for host in hosts:
    client = SSHClient()
    client.load_host_keys('~/.ssh/known_hosts')
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, username='ubuntu')

    stdin, stdout, stderr = client.exec_command('uname -a')

    if stdout.channel.recv_exit_status() == 0:
        print(f'STDOUT: {stdout.read().decode("utf8")}')
    else:
        print(f'STDERR: {stderr.read().decode("utf8")}')

    stdin.close()
    stdout.close()
    stderr.close()
    client.close()
