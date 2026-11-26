# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practise safe Terminal navigation and file operations in the repository, compare directory-listing options, understand pipes, and learn what a package manager does.

## 2. Work completed
Created a `terminal-practice` area and practised creating a text file, adding two lines, displaying it, making a backup, and renaming the backup. The practice files below contain the two-line example. Inspected the repository with normal, detailed, hidden-file, and human-readable listings. Checked Homebrew and viewed the beginning of its package list.

| Operation | Command | What it does / observation |
|---|---|---|
| Current directory | `pwd` | Prints the working directory path. Avoid publishing the username portion of a home-directory path. |
| List files | `ls` | Shows visible entries in the current directory. |
| Detailed listing | `ls -l` | Shows permissions, owner/group, size, date, and name; redact the account name before sharing output. |
| Include hidden entries | `ls -la` | Includes dotfiles such as `.git`. |
| Human-readable sizes | `ls -lh` | Formats sizes with units such as B, KiB, or MiB. |
| Move to parent | `cd ..` | Changes the working directory to its parent. |
| Create directory | `mkdir terminal-practice` | Makes a practice directory. |
| Create/replace first line | `echo "Line one" > terminal-practice/practice.txt` | Creates the file or replaces its contents. |
| Append second line | `echo "Line two" >> terminal-practice/practice.txt` | Adds a line at the end without replacing the first. |
| Display contents | `cat terminal-practice/practice.txt` | Prints the file contents in Terminal. |
| Copy | `cp terminal-practice/practice.txt terminal-practice/practice-backup.txt` | Creates a separate copy. |
| Rename | `mv terminal-practice/practice-backup.txt terminal-practice/practice-renamed.txt` | Moves/renames the backup entry. |
| Pipe example | `ls -lah | head` | Sends listing output to `head`, which displays only the first lines. |

Replacing with `>` overwrites the previous contents, while `>>` appends. Copying leaves the original in place; moving/renaming changes the source entry's location or name. `pwd` shows where commands act, and `ls` helps inspect that location before working.

A flag changes command behavior: `-l` requests a detailed listing, `-a` includes hidden entries, and `-h` makes sizes easier to read. In a pipe, the command on the left produces text output and the command on the right consumes it. Homebrew is a package manager; it helps install, update, and manage software and dependencies consistently. No packages were installed or removed for this task.

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -la`, `ls -lh`: inspected the working directory and its entries.
- `cd ..`, `mkdir`, `echo`, `cat`, `cp`, `mv`: practised safe navigation and file operations.
- `ls -lah | head`: demonstrated piping a listing into a command that limits displayed lines.
- `brew --version`, `brew list | head`: checked Homebrew 7.0.11 and viewed a short package-list sample.

## 4. My understanding
The Terminal runs commands in the current directory, so checking the location and listing files helps avoid changing the wrong place. Redirection with `>` replaces file contents, whereas `>>` preserves existing lines and adds more. A pipe connects the output of one command to the input of another. Package managers keep software and its dependencies organized; I did not install or uninstall anything.

## 5. Difficulties faced
Detailed listings displayed the local account name. That value is private and is not included in this repository.

## 6. How I resolved them
Kept the observation general and omitted raw listing output containing the account name. File practice was confined to `terminal-practice` in the assignment repository.

## 7. Evidence / files
- `terminal-practice/practice.txt` — two-line practice text.
- `terminal-practice/practice-renamed.txt` — renamed backup copy.
- This README — command reference and observations. Raw Terminal output is not included because listings exposed an account name.

## 8. Commit details
Commit: `Complete Terminal and file management mission`. Pushed to `main`.
