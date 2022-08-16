# Commands I've Learnt:
I will write the new commands for me because most of these commands I've studied from another sources.
## Day 1:

- **ls**: list files and dir.
```shell
$ ls -R # list all files and Dirs and thier sub-directories RECURSIVELY.
```

- **head & tail**: print the first and last lines of a file.
```shell
$ head -3 file1.txt # print the first 3 lines.
$ tail -2 file1.txt # print the last two lines.
```

- **cp**: copy files and dir.
```shell
$ cp -i file1.txt dir1/file1.txt # asks before overwrite the file.
```

## Day 2:
### Users and Groups
- The **/etc/passwd** file includes these fields: <br>
Login name | Encrypted password | User Id (uid) | Group Id (gid) | Comment about the user | Home Directory | Login Shell.

- The **/etc/shadow** file: Have all passwords encrypted -probably- with SHA 256 

- **useradd**: add new users.
```shell
$ useradd username # add new user named username
$ useradd -u 1003 -g 1003 -c “this is a comment from this testuser” -md /home/testuser -s /bin/bash testuser # here we specify some details about the user.
```

- **passwd**: to change a password for a user.
```shell
$ passwd testuser # it made you enter a new password
```

- **usermod**: change all properties of a user **except for password**, it's not good.
```shell
$ usermod -l test11@user testuser # this will change the username from testuser to test11@user.
$ usermod -L testuser # this will lock the account of testuser (can't login).
```


