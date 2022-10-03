# Git & Github Resources

I've used <a href="https://www.coursera.org/learn/introduction-git-github">"Introduction to Git and GitHub Course"</a> from Google on Coursera platform.<br>

And I got <a href="https://www.coursera.org/account/accomplishments/certificate/LGFNC84W2EEL">a certificate</a> of completion


#### I'm regularly using these websites for some syntax help.

1. [GitHub Docs](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github)
2. [git-cheat-sheet-education.pdf](https://github.com/AbdassalamAhmad/DevOps_Learning_Journey/blob/main/Git%20%26%20GitHub/git-cheat-sheet-education.pdf) (important!)

## Commands I've Learnt

**config commands:**
```bash
$ git config --global user.name "user name"
$ git config --global user.email "email@company.com"
$ git config --global core.editor "code --wait" # make vscode default editor for git. (--wait to make the terminal wait untill we finished editing)
$ git config --global core.autocrlf true # to make end of the line the same on windows and macos.
# so that git doesn't make mistakes between end of lines on windwos (CR LF) and on mac (LF).
```
### Creating a Local Repository and Adding it to GitHub using Git.
**git init:** initialize a new repo even on non-empty directory.
```bash
$ git init -b main # initialize a new git repo locally with branch named "main" NOT "master" (because git moved away from master naming terminology).
$ git add . # Adds all files in the local repository and stages them for commit.
$ git stage . # SAME AS `git add .`
$ git commit -m "First Commit" # Commits the tracked changes and prepares them to be pushed to a remote repository.
$ git ls-files # shows the files in staging area.
$ git rm file3.txt # remove file3 from local dir and staging area (just commit and you'll be done.)
$ git rm -r --cached dir # remove dir from staging area (incase of adding it to gitignore after staging the file)


# REMOTE PART.
## Here we should create a repo on github and then we will link it with local git repo then pushing the code.
$ git remote add origin  <REMOTE_URL> # we get REMOTE_URL from github repo.
$ git remote -v # Verifies the new remote URL.
$ git remote set-url origin <new_REMOTE_URL> # If you change repo use this command to update origin link.
```

**history commands:**
```bash
$ git log # Shows all commits. press `space` to go to next page, press `q` to quit.
$ git log --oneline  --reverse # shows all commits with just commit id and commit message. (--reverse) from start to end.

$ git show 6d52 # shows commit details and diff commands.
$ git show HEAD~2 # shows the commit before head with two steps.
```

**unstaging commands:**
```bash
$ git restore --staged . # restore all files in staging area (un-add so changes stay in working dir).
$ git restore file1.txt # (get back to previous version that was stored in staging area).
$ git restore --source=HEAD~1 file1.txt #