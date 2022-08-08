# Commands I've Learnt:
## **1. User Accounts:**
1. **whoami**: to know which user your logged in.

2. **id** : to know the userid and group id.

3. **su**: change user logged in to other user.
```shell
$ su user2 # change loggedin usesr from old user to user2
```

4. **ssh**: use secure shell to log into other system with different user
```shell
$ ssh user3@192.168.1.3 # the host is the ip
```

5. **sudo** use sudo command to gain root user privileges.

## **2. Download Files:**
1. **curl**: download a file.
```shell
$ curl http://www.some-site.com/some-file.txt -O # Downloads some-file.txt in the working directory
```

2. **wget**: download a file.
```shell
$ wget http://www.some-site.com/some-file.txt -O new-file.txt # download some-file.txt and rename it to new0file.txt
```

## **3. Check OS Version:**
```shell
$ ls /etc/*release* 
$ cat /etc/*release* # view more details about the os version.
```

## **4. Package Managers:**
- **yum**: "Yellowdog Updater, Modified" is a powerful package manager used to download and install softwares and its dependencies and it is used mostly on RHEL family OS’s.

```shell
$ yum install ansible # install ansible :)
$ yum remove ansible # remove ansible.
```

- **apt**: "Advanced package tool" ia another powerful package manager that downloads and installs softwares used mostly on debian like ubuntu.
```shell
$ apt install ansible # install ansible.
$ apt remove ansible # remove ansible.
$ apt update # Refreshes repository index.
$ apt upgrade # Upgrades all upgradable packages.
$ apt show [package] # Shows package details.
```
## **5. Services:**
- **systemctl or service**: both commands are used to control the system and service manager with different syntax.

```shell
$ systemctl start httpd # Start service httpd.
$ systemctl stop httpd # Stop service httpd.
$ systemctl status httpd # Check HTTPD service Status.
$ systemctl enable httpd # Configure HTTPD to start at startup
$ systemctl disable httpd # Configure HTTPD to not start at startup
``` 

**Note:** If you want to configure your own app to make it a service and be able to start automatically at startup you can do these seteps:
```shell
$ cd /etc/systemd/system
$ touch app.system
$ nano app.system
[Unit]
Description=My python web application

[Service]
ExecStart= /usr/bin/python3 /opt/code/app.py #The main command to run
ExecStartPre=/opt/code/configure_db.sh # command before start
ExecStartPost=/opt/code/email_status.sh # command after starting.
Restart=always # if something crashes the app, restart.

[Install]
WantedBy=multi-user.target # to run this service after multi user target.

$ systemctl daemon-reload # Refresh the system files to get the new system file.
$ systemctl start app
$ systemctl enable app # to start at startup.
```

## **6. VI Editor:**
- **Insert Mode**: Press 'i'.
- **Command Mode**: Press 'esc'.
- **Delete a Line**: Press 'dd'.
- **Copy then Paste**: Press 'yy' then 'p'.
- **Find**: Press '/' then what you want to find.
- **Save with Naming**: Press ':w name'
- **Quit**: Press ':q'
- **Save and Quit**: Press ':wq'

## **7. SSH:**
- To SSH from windows to ubuntu you need to make sure that sshd service is installed and running.
```shell
$ systemctl status sshd
$ systemctl start sshd # if it's not started
```

- Then you must know the ip of your VM and the username.
```shell
$ ip addr
OR
$ ifconfig # look at the ouput near 'enp0s3' 'inet'
$ whoami # to know the name of the user.
```
**Note:** if the ip address wasn't 192.168.*.\* then you need to configure the vm network by selecting bridge adapter from VM Network settings.

- Now you can ssh from your windows terminal.
```shell
$ ssh user@192.168.1.17 # Then provide the password and you're in.
```







![image](https://user-images.githubusercontent.com/83673888/183394278-35b619af-5206-4bb7-9253-581e4f78e464.png)


