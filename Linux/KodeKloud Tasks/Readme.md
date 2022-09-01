

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

## **2. Install squid package on all servers and make sure it's enabled to start during boot.**

```bash
$ ssh app1,app2,app3 # ssh into all 3 apps and enter the password.
$ yum -y install squid # install squid package.
$ systemctl start squid # start the service.
$ systemctl enable squid # enable the service to run after boot.
```

## **3. Add Linux User Without Home Directory.**

```bash
$ ssh app2 # ssh into app2 and enter the password.
$ sudo useradd -M jim # create user named jim with no home directory
```

## **4. Linux banner: (Update the message of the day on all application).**

```bash
$ ssh app1,app2,app3 # ssh into all 3 apps and enter the password.
$ sudo vi /etc/motd # create a new file on each server with the name of message of the day.
$ # paste the contents of the template provided in the task. DONE.
$ # OR you can
$ scp sudo scp -r  /root/nautilus_banner tony@stapp01:/home/tony
$ # and then you can move it to /etc/motd and complete the rest of the steps.
```

## **5. change the default runlevel so that users can boot in GUI.**

```bash
$ systemctl get-default # to know which runtime we're at.
$ systemctl set-default graphical.target # change runtime from multi-user.target to graphical.target
$ systemctl status graphical.target # to see status of this service.
$ systemctl start graphical.target # to start the service if it was dead.
```
## **6.Find all files owned by user rose inside /home/usersdata directory and copy them all while keeping the folder structure to /media directory.**

```bash
$ ssh app2 # ssh into app2 and enter the password.
$ find /home/usersdata/ -type f -user rose -exec cp --parents {} /media \; # use find then exec to execute the command on the result of find command.
$ # then use copy commands with flag --parents to preserve the directories path.
```

## **7. Insatll SElinux:**
```bash
$ ssh app2 # ssh into app2 and enter the password.
$ yum install selinux* # install all required packages.
$ sestatus # check status of SElinux.
$ vi /etc/selinux/config # edit SELINUX=disabled to make sure it is sisabled for now as required.
$ sestatus # make sure it is disabled.
```

## **8. copy file to remote server:**
```bash
$ scp /tmp/nautilus.txt.gpg tony@stapp01:/home/data
$ # enter the password and you're done.
```

## **9. Set up a password-less authentication**
```bash
$ ssh-keygen -t rsa # generate an ssh key 
$ ssh-copy-id  tony@stapp01 # copy the ssh key to all apps.(here i did one only).
```