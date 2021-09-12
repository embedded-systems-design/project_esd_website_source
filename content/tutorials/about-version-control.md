---
tags:
- version control
- GitHub
title: About Version Control
---

# Part 1

## What is Version Control

Version control (sometimes called source control) keeps track of changes to files over time. Multiple users can edit the same projects. Some platforms that support version control are GitHub, GitLab, BitBucket, and Google Drive. 

## Git

Git is an open source tool, but platforms like GitHub and GitLab integrate with git by hosting the repositories (project folders). Repositories can also be self-hosted and use git for management through other services. This post is structured GitHub, a popular platform for many developers. Keep in mind that other repository storage platforms have nuanced differences (e.g. GitHub UI drag and dropping existing files will track code changes, whereas GitLab UI drag and dropping existing files will assume the file is overwriting everything--history included).

### Words to Know (in order of importance)
Repository (aka repo) - a project folder that tracks changes in the subdirectories and files, a collection of files
Commit - sometimes considered snapshots of edits made complete with time, a hash reference, message, and the edits themselves
Pull - a command to retrieve the latest edits from the repository
Push - a command to push the latest edits (packaged in a commit) to the repository
README.md - a file that describes how to use the project, FAQ, and/or explains what the repository is about
Branch - a development path, all paths branch from main
Clone - a copy of a repository often including a link to the original repo (remote) and past commits
.gitignore - a file that filters what files end up on GitHub (files like .c, .java, .md, etc.) and what don't (e.g. compiled object files, secret keys, binary files)
Merge Conflict - when edits are made at the same place (and time) and a conflict occurs
Fork - a clone, but set up in a user's profile linking back to the original repo
Rebase - the process of combining ("replaying") commit(s) into a new commit (often used when resolving merge conflicts)
Stage - the action of preparing file(s) to be committed

### Common commands
-   `git status` get an update of what files have been changed or are untracked
-   `git add <filename, ., *>` add changed files to stage a commit
-   `git commit -m “Commit message here”` add a message to a commit
-   `git push` push a staged commit to the central repository
-   `git pull` retrieve the latest changes from the central repository
-   `git reset --hard HEAD` reset all files to the last commit
-   `git checkout branchName` / `git switch branchName` switch to a different development path
-   `git checkout -b newBranchName` switch to a new development path (`git branch newBranchName` + `git checkout newBranchName`) 

## A Normal Git Workflow (GitFlow)

1. Clone or fork a repo `git clone <repo name>`
2. Create a development branch `git branch <new branch name>`
3. Switch to the development branch `git checkout <new branch name>`
4. Edit file(s)
5. Add file(s) to stage them for a commit `git add <fileName>`
6. Write a message to explain the commit (aka commit message) `git commit -m "put a short descriptive message about the changes here"`
7. Push the commit (message + prepared file(s)) to the development branch `git push`
8. Switch to main branch `git checkout main`
9. Pull recent changes to ensure the local branch instance is up to date `git pull`
10. Make a Pull Request to merge the development branch into the main branch `Go to GitHub to make a New Pull Request`
11. Confirm the pull request `Click merge pull request`
12. If multiple users on a single repository, pull from the main branch into the development branch often `git merge main` to reduce merge conflicts
13. Repeat from step 3.

## Pitfalls

StackOverflow is great for fixing git things. However, git is an extremely powerful tool, and it is easy to wipe the entire edit history or cause irreversible change. With great power comes great responsibility. Never automatically follow instructions on fixing things in git without understanding what each command does. Edit history can be rewritten in git, but it may not be the rewrite needed. If comamnds are confusing, spend the time to figure it out, ask another git user, or try to find another way. Just don't do everything the internet says and lose the whole project and be unable to get it back, that defeats the whole point of version control.

Push to the development branch often/commit regularly. Not only to save changes but to ensure if others are on the branch they can pull each other's changes and everyone can reduce their merge conflicts. 

## Resources

[Git Documentation](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

# Part 2

## GitHub and GitFlow Tutorial

### Setting up GitHub

Create an account on GitHub by going to [github.com](github.com) and signing up. Once complete, click the profile circle on the top right. Most navigation items can be found through the pull down menu. Download a Git CLI, preferably (Git for Windows)[https://gitforwindows.org/], however, GitHub provides a CLI that is recently out of beta [GitHub CLI](https://cli.github.com/). 

### Git for Windows

1. Agree to the license
2. Don't change what components are to be installed, click next
3. Choose "override the default branch name for new repositories" and ensure that the initial branch name is "main", click next
4. Use bundled OpenSSH, click next
5. Keep default `git pull` behavior and click next
6. Only use Git Credential Manager Core and click next
7. Do not select experimental options and click install
8. The program is called `Git Bash` and can be accessed from File Explorer in any folder by right clicking and selecting "Git Bash here"

If there are any additional options not specified here do not change the options just click next.

#### Create a personal access token

[Follow these steps](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### Setting up the first repository

Click the plus left of the profile menu and choose "New Repository." When naming a repository the autochecker will reject repository names already in use by the account, special characters and spaces will be automatically turned into "-" and generally should be easy to remember and type. Though a description is optional, it is still recommended to add a short one sentence description or pitch about the project.

Users can have unlimited public and private repositories. Public means visible to all, private means only visible to members of the repository. If there are features of interest that require a GitHub paid plan, consider checking out the [GitHub Education Student Package](https://education.github.com/pack), which is free to all university students to have a Pro plan without needing to pay. As ASU students, additional verification will likely be needed and student validation requests are usually resolved in less than a week. 

Select "Add a README.md" to instantiate (put a file in) the repo(sitory). Instructions to clone, build, and run projects, along with project descriptions, FAQ or other pertinent information can usually be found in the README.md. It is good practice to always have one at the top level of a repo.

Do not select "Add .gitignore" as one is not need for this tutorial part. However, templates for specific languages exists. If another repo is created using a common language such as C or Java, consider including the .gitignore template to ensure object and binary files and folders are not pushed to the repo. Gitignore files remove "bloat" files from being committed as they are often binary files (unreadable by humans) or custom to the user (e.g. include paths such as C:/UserName/Documents/FolderName/ that are not usable by others).

Do not select "Choose a license" but generally open source projects operate on different levels of licenses, which instruct what users of open source work can and can't do with them. MIT Licenses and GNU Public Licenses are the most common licenses, however, both dictate different restrictions to the code. Research what license works best for custom projects that are public (and private) facing.

Select "Create repository" to be taken to the new repo with a README.md file in it. 

Cloning a repo can be done multiple ways, this tutorial will only describe through zip and HTTPS. 

#### Cloning via Zip

Cloning via Zip file is more like a direct download. Though it may be faster, it will not include any record of the repo it came from (no remote set up) nor history of past commits. To reconnect the remote upstream (connect back to the repo it came from) users must do the following

1. Unzip the file
2. Navigate into the unzipped folder
3. `git init` to initialize a new git repository
4. `git remote add origin https://github.com/username/repoName.git` replacing username with the username of the repo owner, and repoName with the name of the repo

#### Cloning via HTTPS

Cloning via HTTPS will include a link back to the repo it came from and allow users to access past commit history. This is the preferred way of cloning repos unless SSH is necessary. GitHub used to require password verification, however, now it requires personal access tokens (PAT) which is more secure. To clone a repo, click the green button labelled "Code" to pull down the clone options. Ensure "HTTPS" is selected and click the clipboard icon to copy the URL. The URL can also be highlighted and copied.

1. Navigate in Windows Explorer to find where to copy the repository to, in this case `C:/UserName/Desktop`.
2. Right click in the folder in Windows Explorer and click "Git Bash here"
3. In the terminal window that has appeared type `git clone ` and paste the copied URL and hit enter. The command should look something like `git clone https://github.com/username/repoName.git`

When first using the command line, terminal, or Git Bash to interact with GitHub, after the clone command is executed it will ask for a username, and then a PAT. If this has already been done, then it will not ask as the values may already be stored in cache through Git clients. Git for Windows and Git CLI will store these after the first use until it expires. Additional setup varies by the program. 

In the Desktop folder there should now be a folder with the repo name. This is a local instance of the cloned repository. 

#### Starting with an empty repo

When creating repo's without a README.md, it is assumed there is an existing repo, or a repo will be created through the command line, terminal, or Git Bash. Follow the appropriate instructions depending on the context. Figure X shows a repo called `tbd` that was not initialized with a README.md and how to start a new repo from a local instance, link an existing repo, or link from another type of version control.

#### Deleting a repo

To delete a repo go to the repo, then settings, then scroll to the bottom of the options page. Deleting a repository requires the title and the account's password to be entered to confirm the decision. Deleted repositories cannot be retrieved after deletion. 

### Pushing the first edits

From the local instance on Desktop, create a new text file and name it "FirstFile.txt" and put "hello world" in the file. Normal git workflow (gitflow) involves making changes, staging the changes by adding the files, writing a descriptive message about the changes, and then pushing the bundled changes and message in a commit. Make sure a Git Bash window is open in this repository folder.

1. To see what files have been changed type `git status` into the Git Bash window.
2. FirstFile.txt is not tracked yet due to it being a new file. To track the file `git add FirstFile.txt`
3. Entering `git status` will now show the file is tracked and staged (or ready) to be committed. 
4. Open FirstFile.txt and add a new line and "another hello world" to it. Save and close the file. For every change that occurs after a file has been added, the file needs to be re-added or a commit will not include those changes. Commits do not need to include all changes. Do not add the file yet.
4. To complete the commit of the creation of a new file and "hello world" (not "another hello world") enter `git commit -m "added new file and hello world message"`. Commit messages should be short but descriptive such that another user or a future user can understand what edits occurred.
5. To send the commit (the changes, the message) to GitHub where the repository is stored, enter `git push`. Commits don't have to be sent and can be sent multiple at a time. However, it is not advised to not push commits once made, especially if there are other users on the repo. 
6. `git status` again to see that there are still changes that have not been committed. Repeat the process to commit the new changes. Run `git status` after to ensure that the working branch is clean or up to date meaning there are no new changes to commit.

### Pulling down changes

GitHub has a decent UI, but it is best used for very quick fixes. Go back to the GitHub page for the repository created. The new file should now be visible. If not, refresh the page. Click "Add file" then "Create new file."

Name the new file `BrowserFile.txt` because this file is being made through GitHub's browser interface. Type "hello browser!" into the "Edit new file" window. Scroll to the bottom of the page to see "Commit new file" and give a short message in the smaller text field or leave it blank. Click "Commit new file." If the field was left blank, "Create BrowserFile.txt" will be the commit message. 

Go back to Git Bash in the repository folder and type `git pull`. This will "pull" the new file down from the repo and the folder will now have the new file BrowserFile.txt This is how changes can be updated in local instances. This only works if recent changes are pushed to the repository on GitHub. Push and pull changes often to reduce merge conflicts, especially when working with multiple users. 

### Handling Merge Conflicts

Merge conflicts happen often when there is more than one editor in a repository editing the same files in the same locations. It can also happen if editing files through the web (e.g. on GitHub's UI) and through a local desktop instance at the same locations. Normally, Git (and therefore GitHub etc.) automatically manage conflicts, however, sometimes it needs human input. 

An example case might be merging a development branch into main. Merges can be done through terminal commands or through pull requests through GitHub's UI. The following example assumes a user is using the command line (or terminal). Proper gitflow is that merge conflicts are handled on the feature branch (branch to be merged into main) and then merged into main after resolving the conflict. The following example has found a merge conflict trying to merge the branch mundo into the main branch. The merge is then aborted, and a new merge is started from main into the mundo branch. Once the conflict is resolved, mundo is finally merged into main.

1. Attempting to merge mundo into main. This assumes that the user has checked out the main branch.
-   (from main) `git merge mundo` (merge mundo into main)

2. A merge conflict has been found! To cancel a merge run `git merge --abort`. Merges can be aborted in the middle of merge conflict resolutions (rebasing).
3. First, checkout the mundo branch `git checkout mundo` then run `git merge main`. The following is what a merge conflict looks like in a file based on the most recent merge command:

```
def hello
<<<<<<< HEAD (aka current change aka changes from mundo)
  puts 'hello mundo'
======= (aka incoming change aka changes from main)
  puts 'hola world'
>>>>>>> main
```

In the above example, the changes in the main branch ('hola world') conflict with the changes from the branch mundo ('hello mundo'). The changes in mundo are considered the "current change" or HEAD (think pointers), while the changes in main are considered the "incoming change" and both are separated by a series of '=' symbols. HEAD will always be preceded by a series of '<' while the conflict itself will be closed by a series of '>' and the branch name (main). Merge conflicts will always appear in the order of current change to incoming change. Sometimes, rather than removing one of the other, the code may need to be a combination of both sources, it is not always the most intuitive, and it is often recommended to use editors that can help manage conflicts, like Visual Studio Code (VSC).

For now, we want to keep the changes in mundo, so we need to remove all indicators of a merge conflict, namely, the lines including '<' and '>'.

```
def hello
  puts 'hello mundo'
```

Once all merge conflicts have been resolved (the lines indicated conflict exists have been removed) follow the process of committing changes from the start (add, add a message, push) and the conflict is complete. Now checkout the main branch, `git merge mundo` into main, and done!


## Resources
https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories

# Part 3 (Setting up for PSoC)

To use GitHub with PSoc code requires a very specific set up, this is mostly due to how PSoC creates and manages files. 

PSoC Creator has a default folder in Documents where project code is stored. Each workspace can host a number of projects. This tutorial commits the workspace, and therefore automatically includes all projects. Some PSoC users organizer their workspaces by keeping one workspace per microcontroller type.

First, create a new workspace in PSoC Creator by selecting "New project" under the "File" tab, and selecting "workspace" when prompted with the radio buttons that appear. Use the default location (C:/Users/UserName/Documents/PSoC Creator/) and specify a name for the workspace

Next, create a new project by using one of the existing template projects. 

PSoC Creator for now.

## Setting up the Repo and including a .gitignore

Open the folder in which the workspace was saved (`C:\\Users\\UserName\\Documents\\PSoC Creator\\WorkspaceName`) in Windows Explorer.

Right click within the folder and select "Git Bash here" to open a git terminal.

To initialize the workspace as a git repo, enter `git init`. Next, download the [.gitignore](https://github.com/HalcyonAura/PSoCTest/blob/TestBranch1/.gitignore) and put the .gitignore file in the same folder. 

On the GitHub UI, create a new repository, but do not initialize it with a README.md, .gitignore, license, or any other option. Just a name, such as PSoC Workspace. Click create repository. 

Follow the instructions that appear to push the local repository to the newly created repository on GitHub. Make sure to include the .gitignore. Instead of adding all the files manually, type `git add .`, this means to add all files in the directory. It is better practice to use purposeful selection of files (e.g. `git add FolderName/*` which adds all files in a folder, or `git add FileName.fileExtension` which adds a single file) to avoid accidentally adding files that are not caught by the .gitignore, or committing secrets (passwords, API tokens, etc.) that should never be publically available. 

## Pulling from the repo

Other users can clone and pull changes, but must rebuild the project in order for it to work on their systems. The .gitignore omits all build files and pertinent workspace information that is custom to each user.

## Editing the .gitignore

There is a very likely chance as the semester proceeds that the .gitignore will need to be modified for files in certain folders that are related to compilation and therefore (currently) not included. The following describes relevant symbols in .gitignores. The .gitignore file downloaded has notes on how to edit the file to include files after being ignored, or to identify specific files to be included.

### Symbols

-   /# comments out the line
-   /* is a wildcard. If placed in front of a folder or name, any number of alphanumerics can precede it. If placed at the end of a folder or name, any number of alphanumerics can follow after it
-   / folder structures end with a forward slash even if on a Windows System
-   ! means to include a file or folder after it has been excluded

### Further Explanation of the .gitignore edits

If edits occur in the Generated_Source/ folder, to include specific files the .gitignore must be edited following the `*Generated_Source/` line with the following: `!*Generated_Source/FolderName/FileToInclude.*` This may not be the only structure. The example listed refers to a custom USB_audio, thus, the added line looks like `!*Generated_Source/PSoC4/USB_audio.*`. This line indicates that all files in Generated Souree in PSoC4 that begin with USB_audio must not be ignored. 

If other optional items such as datasheets are necessary to be commented then remove the preceding `#` from the line to uncomment it. 

Commit the changes to ensure they come into effect. Files that are present before a .gitignore is implemented (and they are marked to be ignored) will still be present in the repository and tracked. It is good practice to implement a .gitignore before development begins. To resolve this enter `git rm -r --cached <To Be Ignored>` where To Be Ignored refers to a file or folder structure (`Folder/` to ignore a directory entirely `Folder/*` to ignore the folder's contents) that needs to be removed. When you commit, the discrepancy should be resolved.
