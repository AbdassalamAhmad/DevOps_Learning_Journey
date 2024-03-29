# Vagrant Resources

I've used This <a href="https://www.youtube.com/watch?v=a6W1hF9CgDQ&list=PLnFWJCugpwfyInpbM1A435Lrd56jNwZTr">"Youtube Course"</a>.<br>

With the help of that course, I've built three virtual machines (VM) on my lab using [this Vagrantfile](https://github.com/AbdassalamAhmad/DevOps_Learning_Journey/blob/main/Vagrant/Vagrantfile).<br>

So, Now I can configure this lab using Ansible to be able to install docker and kuberentes and other tools with one Ansible Playbook without manually install it on every VM or server.

### Most important commands in Vagrant:
0. To Get help in Vagrant commands.
```shell
$ Vagrant
```

1. Bring up the vagrant instance.
``` shell
$ vagrant up
```

2. SSH into Virtual Machine.
``` shell
$ vagrant ssh
```

3. Get Status of Local Vagrant Machine in the same directory.
``` shell
$ vagrant status
```

4. Get Status of ALL Vagrant Machines on host.
``` shell
$ vagrant global-status
```

5. Get SSH Settings (to be able to use ssh into VM from the terminal).
``` shell
$ vagrant ssh-config
```

6. Restart Virtual Machine to Reload new configurations.
``` shell
$ vagrant reload
```

7. Stop Virtual Machine without saving state.
``` shell
$ vagrant halt
```

8. Stop and Save state of the Virtual Machine.
``` shell
$ vagrant suspend
```

9. Delete the Virtual Machine
``` shell
$ vagrant destroy
```

10. **Alternatively** you can use simple ssh command instead of using **vagrant ssh** ,and get the same results.
```shell
$ ssh vagrant@172.16.1.51 -p 22 # then you put the password which is vagrant.
$ # now you are in the node1 VM
```

#### I'm regularly using these websites for some syntax help.

1. [Vagrant Docs](https://www.vagrantup.com/docs)