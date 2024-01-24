# Obsidian Github wiki experiment

This repository was made to explore the possibility to use git hooks to maintain a GitHub wiki using obsidian.

Public repositories with come with a [wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis).

This repository has a github wiki [here](https://github.com/BjornFJohansson/obsidian_git_experiment/wiki).
Or click the wiki link at the top of the page.

[Obsidian.md ](https://obsidian.md) is a great tool to maintain a local markdown wiki for notes ([YouTube](https://youtu.be/QXIa0NAycGo?si=q2-NtNW7xvjYKZSy)).


While both Obsidian and Github wiki claims to use markdown, the problem is that the syntax is _almost_ the same, but differ in small but important ways, specifically:

### wiki links

- Obsidian: `[[page|custom display text]]`
- Github wiki: `[[custom display text|page]]`

In the wiki link format with alternative display text, Obsidian and GH wiki use the opposite order. This is important in Obsidian for how the GUI autocomplete these links.

Another important difference are image links:

### image links
- Obsidian: `![[borb.png]]`
- Github wiki: `[[borb.png]]`

The GH wiki has two branches, "master" and "obsidian".
On you local computer, you should have the obsidian branch checked out.
When committing to this branch, a post-commit hook is activated.
The commited filenames are listed, and filtered for .md extension.
This is a python script that checks out the "master" branch.
The "obsidian" branch is merged.
The committed files are processed to modify wiki and image links using regex.
The resulting changes are committed.
Finally, the script checks out the obsidian branch again.

look [here](https://forum.obsidian.md/t/github-wiki-kinda-works-to-host-the-wiki/2980) for more background.

> [!WARNING]
> This was absolutely not tested, backup before using this on your repositories
> This may not even be the best way to solve this problem.

## How to test:

Fork this repository to your own gh account.
Clone the GH wiki repo:

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

copy the "post-commit" file from the GH wiki repo to .git/hooks

Make some changes in the obsidian branch, specifically try adding

```
![[imgage.ext]]
[[filename|title]]
```
in markdown files. These are obsidian style links.

Commit the changes in the obsidian branch, switch to main and observe the results.
