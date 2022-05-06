# Git merging

## commands:
```
git branch 
```
`# will show all the branches with an * by the branch you're on`

```
git status 
```
`# will show which branch you're on and the commit status relative to other branches/trees, ie ahead/up to date/behind`

**git branch** will show up in bottom left screen on VSCode, along the bottom bar.  It will have an `*` next to it if there are uncommited changes.  
- Clicking the branch name in VSCode will pop open a menu which allows you to create a new branch or (checkout a branch?).

**creating a new branch:**
```
$ git branch <new-branch-name>
```
Important to think about **which branch you're currently on**.  The new branch will start with the same commit history as your current branch.

**switching branches**:
```
$ git switch <destination-branch-name>
```
 Historically, `$ git checkout <destination-branch-name>` was the way to switch branches. Now **git switch** is prefered`
    - Before switching, you must either:
    - commit any unstaged and/or staged changes. This way, these changes will stay on the current branch before switching.
    - Or, Use Git's stash feature, which will save changes in the **stash** <mark> what is this? </mark>, instead of a commit.

**Delete a branch**:
```
$ git branch -d <branch-name>
```
