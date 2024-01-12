# Obsidian Github wiki experiment
This repository was made to explore the possibility to use git hooks to maintain a github wiki using obsidian.
The syntax is _almost_ the same, but differ in some ways, specificlly:

A links in Obsidian: [[fileName|linkTitle]]

A Link in Github wiki: [[linkTitle|fileName]]

This repository has two branches, "obsidian" and "main". The obsidian branch is thought to contain obsidian style markdown.
The git hook in the file "post-commit" is activated after commit to the obsidian branch.
The commited filenames are listed, and filtered for .md extension.
The main branch is checked out.
Changes from the obsidian branch are merged.
The files with .md extension are searched and replaced using regex.
Finally, the changes are committed to the main branch, and the script checks out the obsidian branch again.

look [here](https://forum.obsidian.md/t/github-wiki-kinda-works-to-host-the-wiki/2980) for more background.

> [!WARNING]  
> This was absolutely not tested, backup before using this on your repositories
> This may not even be the best way to solve this problem. 

## How to test:

Fork the repository to your own gh account

clone the fork to your computer

verify that you have both "obsidian" and "main" branches

copy the "post-commit" to .git/hooks

make some changes in the obsidian branch, specifically try adding

```
![[imgage.ext]]
[[filename|title]]
```
in markdown files. These are obsidian style links.

commit the changes in the obsidian branch, switch to main and observe the results.
