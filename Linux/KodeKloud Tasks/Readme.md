

## **1. Service Error (Postfix a mail service is stopped): 18/8/2022**

```bash
$ systemctl start postfix # 
$ systemctl status postfix # to see what is the error message.
$ # we now know the problem is with the inet_interface parameter.
$ # so we go to '/etc/postfix/main.cf' to fix it.
$ vi /etc/postfix/main.cf
$ # we find this line 'net_interfaces = localhost' and comment it to solve the problem.
$ systemctl start postfix 
$ systemctl status postfix # to make sure the problem is solved.
```

## **2. Install squid package on all servers and make sure it's enabled to start during boot.

```bash
$ ssh app1,app2,app3 # ssh into all 3 apps and enter the password.
$ yum -y install squid # install squid package.
$ systemctl start squid # start the service.
$ systemctl enable squid # enable the service to run after boot.
```