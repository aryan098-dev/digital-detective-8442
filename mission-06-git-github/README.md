# Mission 6 — Git and GitHub

## 1. Task / objective
Practise the Git workflow, create and publish a branch, open a Pull Request, and explain collaboration concepts.

## 2. Work completed
Created the `update-about` branch, added a **My Learning** section to the root `README.md`, pushed the branch to GitHub, opened a Pull Request into `main`, and merged it successfully.

- Pull Request: [#1 — Add My Learning section](https://github.com/aryan098-dev/digital-detective-8442/pull/1)
- Status: **Merged**
- Merge commit: `8220892a99334ecf07d489557432570035028754`
- Branch used: `update-about`

### Git and GitHub glossary
| Term | Meaning |
|---|---|
| Repository | Project files and their tracked history. |
| Working tree | The current checked-out files where edits are made. |
| Staging area | The selection of changes prepared for the next commit. |
| Commit | A saved snapshot of staged changes with a message. |
| Branch | An independent line of work that can be changed without directly editing another branch. |
| Push | Sends local commits to a remote repository. |
| Pull Request (PR) | A GitHub proposal to review and merge changes from one branch into another. |
| Merge | Combines the changes from the PR branch into its target branch. |
| `main` | The repository's primary branch in this workflow. |

## 3. Commands / tools used
The branch and Pull Request were completed through the GitHub workflow. The corresponding Git operations are:
- `git switch -c update-about` — creates and checks out the work branch.
- `git status` — checks the current branch and working-tree changes.
- `git add README.md` — stages the learning update.
- `git commit -m "Add My Learning section"` — records the staged change as a commit.
- `git push -u origin update-about` — publishes the branch and sets its upstream.
- GitHub Pull Request #1 — proposed merging `update-about` into `main`; the PR was merged.

## 4. My understanding
Staging lets me choose which changes belong in a commit. A commit records a snapshot and message in the repository history. A branch gives a change its own line of work. Pushing publishes that branch to GitHub, and a Pull Request makes the proposed changes available for review before merging them into the target branch. After the merge, the changes are part of `main`.

## 5. Difficulties faced
No major difficulties were reported. The learning update was made on a separate branch and merged through a Pull Request.

## 6. How I resolved them
Used the GitHub branch and Pull Request workflow to publish and merge the change.

## 7. Evidence / files
- Root `README.md` — includes the **My Learning** section.
- Branch: `update-about`.
- [Merged Pull Request #1](https://github.com/aryan098-dev/digital-detective-8442/pull/1).

## 8. Commit details
The learning-update commit message was `Add My Learning section`. Pull Request #1 was merged into `main`; this mission report is recorded in a follow-up commit on `main`.
