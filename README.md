# Syncing Obsidian & GitHub Wiki

This repository was made to explore the possibility to use git hooks to maintain a [GitHub Wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis) using the amazing note-taking, markdown-editing, and second-brain-making app [Obsidian](https://obsidian.md/). 

This repository has a GitHub Wiki, accessible [here](https://github.com/BjornFJohansson/obsidian_git_experiment/wiki), or by clicking the **Wiki** link at the top of the page.

BTW, Obsidian can be confusing, but it's worth it! Here's a link to learn more about using it :) ([YouTube](https://youtu.be/QXIa0NAycGo?si=q2-NtNW7xvjYKZSy)).

## Key Differences Between Obsidian and GitHub Wiki
While both Obsidian and GitHub Wiki claim to use Markdown, the syntax is not quite the same,  differing in small but important ways, namely:
### WikiLinks
- Obsidian: `[[page|custom display text]]`
- GitHub Wiki: `[[custom display text|page]]`

In the WikiLinks format, Obsidian and GH Wiki use the opposite order.
This is important in Obsidian for how the GUI autocomplete these links
### Image Links
- Obsidian: `![[borb.png]]`
- GitHub Wiki: `[[borb.png]]`
### Header Links
- Obsidian: `[[#Some Header|custom display text]]`
- GitHub Wiki: `[custom display text](#some-header)`

## How The Script Works
This is a Python script called "post-commit" which must be placed in the .git/hooks folder. The script now uses a modular approach with separate transformation functions for better maintainability.

When committing, the post-commit Git hook is activated. Specifically, this script will only have an effect if the change is committed while in the "obsidian" branch.

Your GH Wiki will have three branches, "master", "ob_to_gh" and "obsidian" (after you create the latter two). The "master" branch is the only one that is visible online on GitHub Wiki.

On your computer, you should **always** have the "obsidian" branch checked out.

This script does this:

1. The committed filenames are listed by Git.
2. Filenames are filtered for .md extension and other extensions.
3. Check out the "ob_to_gh" branch.
4. Check out all the changed paths listed in 1. from "obsidian" branch
5. The checked-out .md files are processed using the `transformations.py` module to modify wiki and image links with improved regex patterns.
6. The resulting changes are committed to "ob_to_gh".
7. Branch "master" is checked out.
8. "master" is merged with "ob_to_gh" using "--strategy-option theirs"
9. Changes in "master" are pushed to remote to make them visible.
10. Finally, the script checks out the obsidian branch again.

Note: "master" is being used for the main branch name as that's seemingly what GitHub Wiki uses by default for some reason.

Look [here](https://forum.obsidian.md/t/github-wiki-kinda-works-to-host-the-wiki/2980) for more background.

> [!WARNING]
> While I use this everyday to maintain [this](https://github.com/MetabolicEngineeringGroupCBMA/MetabolicEngineeringGroupCBMA.github.io/wiki) wiki, this was not tested on other use cases.
> ***Back up*** before using this on your repositories. Even better, run through the test below to make sure it works on your system first! This may not even be the best way to solve this problem.
> 
~ [BjornFJohansson](https://github.com/BjornFJohansson)

## How You Can Test It
1. Fork this repository.
2. Clone the forked repo.
3. Create the wiki on the forked repo using the **Wiki** tab.
4. Clone the created **GH Wiki**, typically in the format (*username*/*repository*.wiki.git). The clone link can also be found on the Wiki page under the sidebar on the right:

```
(bjorn311) bjorn@bjorn-ThinkPad-T450s:~/Desktop/Untitled Folder 2$ git clone https://github.com/BjornFJohansson/obsidian_git_experiment.wiki.git
Cloning into 'obsidian_git_experiment.wiki'...
remote: Enumerating objects: 178, done.
remote: Counting objects: 100% (178/178), done.
remote: Compressing objects: 100% (65/65), done.
remote: Total 178 (delta 114), reused 165 (delta 104), pack-reused 0
Receiving objects: 100% (178/178), 363.54 KiB | 1.37 MiB/s, done.
Resolving deltas: 100% (114/114), done.
(bjorn311) bjorn@bjorn-ThinkPad-T450s:~/Desktop/Untitled Folder 2$ cd obsidian_git_experiment.wiki/
(bjorn311) ✔ ~/Desktop/Untitled Folder 2/obsidian_git_experiment.wiki [master|✔]
07:29 $ git fetch --all
(bjorn311) ✔ ~/Desktop/Untitled Folder 2/obsidian_git_experiment.wiki [master|✔]
07:29 $ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/origin/obsidian
(bjorn311) ✔ ~/Desktop/Untitled Folder 2/obsidian_git_experiment.wiki [master|✔]
07:29 $
```
Commands used: *git clone* (wiki) >> *git fetch --all* >> *git branch -a*

1. Copy the "post-commit" file and "transformations.py" module from the forked GH repo to the **.git/hooks** directory in the **GH Wiki** repo.
2. Create the branches "ob_to_gh" and "obsidian".
3. Switch to the "obsidian" branch. Add the following **Obsidian**-style links to a .md file.
```
Page: [[filename|title]]

Image: ![[image.ext]]

Header: [[#Some Header|custom display text]]
```

6. Stage and commit the changes in the "obsidian" branch and switch to "master" to observe the results. Check that the file(s) you created on the "obsidian" branch show up and make sure the contents have been transformed. If you copied the block above, it should now look something like this:
```
Page: [[title|filename]]

Image: [[image.ext]]

Header: [custom display text](#some-header)
```

7. Done!

## How You Can Use It
Before you do anything, ***back up*** your Obsidian folder. Just create a copy of the Obsidian vault folder if you need to.
1. Create a GitHub Wiki for your GitHub repo using the **Wiki** tab.
2. Clone the created wiki, typically in the format (*username*/*repository*.wiki.git). The clone link can also be found on the Wiki page under the sidebar on the right.
3. Download and move the **.gitignore** file to the new folder.
4. Download and move the **post-commit** and **transformations.py** script files into the .git/hooks/ directory. You may need to reveal hidden items in whichever file browser or interface you're using.
5. Rename the "main" branch to "master" if it isn't already.
6. Create two branches: "ob_to_gh" and "obsidian".
7. Switch to the "obsidian" branch.
8. Open **Obsidian** and *open the cloned folder* as a vault. Do not create a new vault.
9.  Do whatever you'd like to in Obsidian. Make new notes, add some links, etc.
10. Stage and commit the changes (while still in the "obsidian" branch). The script should automatically ultimately merge the changes into "master" and push it to the wiki. It will return to "obsidian" after.
11. View your changes on GitHub Wiki.
12. Celebrate! 🎉