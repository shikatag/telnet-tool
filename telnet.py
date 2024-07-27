import telnetlib
import getpass

print("Telnet Connection Tool By ShikataGaNai")

host = input("Remote Host: ")

user = input("Username: ")

password = getpass.getpass()

tn = telnetlib.Telnet()

tn.open(host)

tn.read_until(b"login: ")

tn.write(user.encode("ascii")+b"\n")

tn.read_until(b"Password: ")

tn.write(password.encode("ascii")+b"\n")

tn.write(b"exit\n")

print(tn.read_all())

tn.close()

