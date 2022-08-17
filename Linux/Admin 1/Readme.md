# Commands I've Learnt:
I will write the new commands for me because most of these commands I've studied from another sources.
## Day 1:

- **ls**: List files and dir.
```bash
$ ls -R # list all files and Dirs and thier sub-directories RECURSIVELY.
```

- **head & tail**: Print the first and last lines of a file.
```bash
$ head -3 file1.txt # print the first 3 lines.
$ tail -2 file1.txt # print the last two lines.
```

- **cp**: Copy files and dir.
```bash
$ cp -i file1.txt dir1/file1.txt # asks before overwrite the file.
```

## Day 2:
### **Users and Groups:**
### 1. Users:
- The **/etc/passwd** file includes these fields: <br>
Login name | Encrypted password | User Id (uid) | Group Id (gid) | Comment about the user | Home Directory | Login bash.

- The **/etc/shadow** file: Have all passwords encrypted -probably- with SHA 256 

- **useradd**: Add new users.
```bash
$ useradd username # add new user named username
$ useradd -u 1003 -g 1003 -c “this is a comment from this testuser” -md /home/testuser -s /bin/bash testuser # here we specify some details about the user.
```

- **userdel**: Delete a user account
```bash
$ userdel -rf testuser # delete testuser account and home directory and mail spool with force of removing files.
```

- **usermod**: Change all properties of a user like adding user to group, **BUT for changing password**, it's not good.
```bash
$ usermod -l test11@user testuser # this will change the username from testuser to test11@user.
$ usermod -L testuser # this will lock the account of testuser (can't login).
$ usermod -a -G newgroup testuser # this will add testuser to newgroup.
```

- **passwd**: Change a password for a user.
```bash
$ passwd testuser # it made you enter a new password
$ sudo passwd -d testuser # delete password of testuser account
```

- **chage**: Change password expiry information.
```bash
$ chage -m 20 testuser # Change the min number of days between password changes to 20 days.
$ chage -M 20 testuser # Change the max number of days between password changes to 20 days.
```
### 2. Groups:

- **groupadd**: Create new group
```bash
$ groupadd newgroup # adds nwegroup group :)
```

- **groupmod**: Modify group properties like name and ID.
```bash
$ groupmod -n new_group old_group # Renames the old_group TO new_group.
```

- **chown**: change group and/or user ownership of a file or directory.
```bash
$ chown :newgroup file1 # Change owenership of file1 from its old group TO newgroup.
$ chown -R user2:newgroup dir1 # Change dir1 owenership from its old group TO newgroup and from old user TO user2.
```

- **groupmems**: See which users are a member of a certin group.
```bash
$ groupmems -g group1 -l # List all users within group1.
```

