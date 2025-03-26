# Obsidian Github wiki experiment

This repository was made to explore the possibility to use git hooks to maintain a GitHub wiki using obsidian.

Public Github repositories with come with a 
[wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis).

This repository has a github wiki [here](https://github.com/BjornFJohansson/obsidian_git_experiment/wiki).
Or click the wiki link at the top of the page.

[Obsidian.md ](https://obsidian.md) is a great tool to maintain a local markdown wiki for 
notes ([YouTube](https://youtu.be/QXIa0NAycGo?si=q2-NtNW7xvjYKZSy)).


While both Obsidian and Github wiki claims to use markdown, the syntax is not quite the same, but differ in 
small but important ways, specifically:

### wiki links

- Obsidian: `[[page|custom display text]]`
- Github wiki: `[[custom display text|page]]`

In the wiki link format with alternative display text, Obsidian and GH wiki use the opposite order. 
This is important in Obsidian for how the GUI autocomplete these links.

Another important difference are image links:

### image links
- Obsidian: `![[borb.png]]`
- Github wiki: `[[borb.png]]`

### How this works

The GH wiki has three branches, "master", "ob_to_gh" and "obsidian".
The master branch is the only one that is visible online on Github.

On you local computer, you should always have the "obsidian" branch checked out.

When committing to "obsidian" branch, a post-commit hook is activated.
This is a Python script called "post-commit" in the .git/hooks folder.

In this script: 

1. The committed filenames are listed by Git.

2. Filenames are filtered for .md extension and other extensions.

3. Check out the "ob_to_gh" branch.

4. Check out all the changed paths listed in 1. from "obsidian branch"

5. The checked-out -md files are processed to modify wiki and image links using regex.

6. The resulting changes are committed to "ob_to_gh".

7. Branch "master" is checked out.

8. "master" is merged with "ob_to_gh" using "--strategy-option theirs"

9. Changes in "master" are pushed to remote to make them visible.

10. Finally, the script checks out the obsidian branch again.


look [here](https://forum.obsidian.md/t/github-wiki-kinda-works-to-host-the-wiki/2980) for more background.

> [!WARNING]
> While I use this everyday to maintain [This](https://github.com/MetabolicEngineeringGroupCBMA/MetabolicEngineeringGroupCBMA.github.io/wiki) wiki
> This was not tested on other use cases, backup before using this on your repositories
> This may not even be the best way to solve this problem.

## How to test:

1. Fork this repository to your own gh account.
2. Clone the GH wiki repo:

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

2. copy the "post-commit" file from the GH wiki repo to .git/hooks

3. Make some changes in the obsidian branch, specifically try adding

```
![[imgage.ext]]
[[filename|title]]
```
in markdown files. These are obsidian style links.

Commit the changes in the obsidian branch, switch to main and observe the results.
