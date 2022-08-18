# Commands I've Learnt:
## **1. User Accounts:**
1. **whoami**: to know which user your logged in.

2. **id** : to know the userid and group id.

3. **su**: change user logged in to other user.
```bash
$ su user2 # change loggedin usesr from old user to user2
```

4. **ssh**: use secure shell to log into other system with different user
```bash
$ ssh user3@192.168.1.3 # the host is the ip
```

5. **sudo** use sudo command to gain root user privileges.

## **2. Download Files:**
1. **curl**: download a file.
```bash
$ curl http://www.some-site.com/some-file.txt -O # Downloads some-file.txt in the working directory
```

2. **wget**: download a file.
```bash
$ wget http://www.some-site.com/some-file.txt -O new-file.txt # download some-file.txt and rename it to new-file.txt
```

## **3. Check OS Version:**
```bash
$ ls /etc/*release* 
$ cat /etc/*release* # view more details about the os version.
```

## **4. Package Managers:**
- **yum**: "Yellowdog Updater, Modified" is a powerful package manager used to download and install softwares and its dependencies and it is used mostly on RHEL family OS’s.

```bash
$ yum install ansible # install ansible :)
$ yum remove ansible # remove ansible.
```

- **apt**: "Advanced package tool" ia another powerful package manager that downloads and installs softwares used mostly on debian like ubuntu.
```bash
$ apt install ansible # install ansible.
$ apt remove ansible # remove ansible.
$ apt update # Refreshes repository index.
$ apt upgrade # Upgrades all upgradable packages.
$ apt show [package] # Shows package details.
```
## **5. Services:**
- **systemctl or service**: both commands are used to control the system and service manager with different syntax.

```bash
$ systemctl start httpd # Start service httpd.
$ systemctl stop httpd # Stop service httpd.
$ systemctl status httpd # Check HTTPD service Status.
$ systemctl enable httpd # Configure HTTPD to start at startup
$ systemctl disable httpd # Configure HTTPD to not start at startup
$ systemctl restart httpd # Restart a service after changing a configuration file.
``` 

**Note:** If you want to configure your own app to make it a service and be able to start automatically at startup you can do these seteps:
```bash
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
- **Delete a letter &&& Line**: Press 'x' &&& 'dd'.
- **Copy then Paste**: Press 'yy' then 'p'.
- **Find**: Press '/' then what you want to find.
- **Save with Naming**: Press ':w name'
- **Quit and override**: Press ':q!'
- **Save and Quit**: Press ':wq'

## **7. SSH:**
- To SSH from windows to ubuntu you need to make sure that sshd service is installed and running.
```bash
$ systemctl status sshd
$ systemctl start sshd # if it's not started
```

- Then you must know the ip of your VM and the username.
```bash
$ ip addr
OR
$ ifconfig # look at the ouput near 'enp0s3' 'inet'
$ whoami # to know the name of the user.
```
**Note:** if the ip address wasn't 192.168.*.\* then you need to configure the vm network by selecting bridge adapter from VM Network settings.

- Now you can ssh from your windows terminal.
```bash
$ ssh user@192.168.1.17 # Then provide the password and you're in.
```
## **8. Snapshots in VirtualBox**
- We can use snapshots to restore the vm to a good state that we know it was good before testing a new software. We can do that by clicking snapshots button on the required vm.

![image](https://user-images.githubusercontent.com/83673888/183394660-e9912b99-e04d-4f58-91af-10bdd99cd768.png)


## **9. DNS:**
* Hosts File
    - Domain Name System is a system to replace IPs with names that are easy to remember.
    - you can try using DNS on your local network, say you have another device with this ip 192.168.1.11 , and you want to name it db to reach for it faster, You can do that by modifying the "/etc/hosts" file on your system like this.<br>
    192.168.1.11 db
    - Now you can ping "db" instead of 192.168.1.11
* Record Types
    - A : storing IPv4 to host names. Like : web-server 192.168.1.1
    - AAAA : Storing IPv6 to host names. Like : web-server 2001:0db8:85a3:0000:0000:8a2e:0370:7334
    - CNAME : Storing names to names. Like : food.web-server eat.web-server

* You can use "nslookup" OR "dig" commands to query a hostname from a DNS server.
```bash
$ nslookup www.google.com 
$ # Outputs the IP address of www.google.com
$ dig www.google.com
$ # Outputs more detailed info about www.google.com
```

## **10. Routing and Switching:**
- You can find all useful commands and best practices in [KodeKloud Labs](https://kodekloud.com/topic/labs-switching-and-routing-2/).


## **12. JSON:**

```json
{
    "car":{
        "price":"20",
        "wheels":[
            {"state":"good",
            "position":"rear"},
            {"state":"bad",
            "position":"front"}
        ]
    },
    "bus":{
        "color":"red"
    }
}
```
- **How to Query from a Dictionary:**<br>
By using \$ sign we can query the car price like this: $.car.price **# "20"**
- **How to Query from a List:**<br>
By using square bracketes like this: $.car.wheels[0].position **# "rear"**
- **Criteria:**<br>
    - $[?(@>40)] # check if each item in the array > 40
    - $.car.wheels[?(@.position=="front")].state **# "good"**

## **13. KodeKloud Tasks:**
1. create a user with a non-interactive bash 
```bash
$ adduser username  -s /sbin/nologin 
```