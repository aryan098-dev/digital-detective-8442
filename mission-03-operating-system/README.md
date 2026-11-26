# Mission 3 — Understand the operating system

## 1. Task / objective
Explore macOS, storage, active processes, paths, permissions, and operating-system responsibilities.

## 2. Work completed
| Information explored | What it tells me | Privacy-safe observation |
|---|---|---|
| Operating system / system details | Identifies the OS environment and build. | macOS 27.2, build 26B123. |
| Current account identity | Identifies who has an active local session. | An active macOS account was in use; no username or identifying output is published. |
| Available and used storage | Shows capacity, used space, free space, and mount location. | 926 GiB volume size; approximately 227 GiB used and 661 GiB available (about 26% used). |
| System activity snapshot | Lists running processes and their PIDs. | `launchd` was PID 1; system services and background daemons were also running. |

A process is a program or system service currently running. The PID column identifies one running process with a process ID. Examples observed here include `launchd` and `logd`; applications such as Safari or VS Code may also appear as processes when open.

### Paths
An absolute path begins at the filesystem root and gives the complete route to a location. Example: `/Users/[redacted]/Documents/digital-detective-8442/mission-03-operating-system`.

A relative path starts from the current directory. From the repository root, an example is `mission-03-operating-system`, and from that folder `../mission-02-terminal` refers to the Terminal mission folder.

Navigating from the assignment folder into a mission subfolder changes the working directory from the repository root to the subfolder.

### Permissions
The detailed listing for the repository showed files with mode `-rw-r--r--`. Its owner has `r` and `w` permissions, so the owner can read and edit the file; the `x` position is `-`, so this ordinary text file is not executable.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows contents to be read. | Opening a README. |
| `w` — Write | Allows a file to be changed. | Editing a README. |
| `x` — Execute | Allows a program/script to run; for directories, allows traversal. | Running a Python script. |

No system permissions or protected files were changed.

### Operating-system responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules, pauses, and ends running programs. | Launching Safari or VS Code. |
| Memory management | Assigns working memory to processes and releases it when no longer needed. | Keeping open documents in RAM. |
| Device management | Coordinates hardware through drivers and system services. | Sending text to the display or data to storage. |
| File management | Organizes files and folders and controls access. | Saving a README inside a mission folder. |
| User interface / shell | Provides graphical or command-line ways for users to interact. | Finder or Terminal. |
| Security and permissions | Controls access and helps protect processes, files, and accounts. | Owner read/write permissions for a text file. |

## 3. Commands / tools used
- `sw_vers`: displayed macOS name, version, and build.
- `df -h ~`: showed storage usage for the active macOS volume.
- `ps -ax | head -n 12`: showed a brief process snapshot and PID column.
- `pwd` and `cd`: navigated and observed paths.
- `ls -l`: displayed permissions and file details.
- Terminal: inspected the system environment.

## 4. My understanding
macOS manages running processes, memory, storage, devices, files, and user permissions while also providing graphical and command-line interfaces. A PID distinguishes a process. Absolute paths fully identify a location, while relative paths depend on the current directory. Permission letters describe the actions allowed for a file or directory.

## 5. Difficulties faced
The raw storage and process listings contained local system details, and the detailed listing contained an account name.

## 6. How I resolved them
I kept only useful privacy-safe observations and replaced identifying path and account details with `[redacted]`. I did not change system permissions or protected files.

## 7. Evidence / files
- Privacy-safe macOS observations in this README.
- Process and storage notes are based on the supplied macOS Terminal output.
- No private screenshots or raw account details are stored.

## 8. Commit details
Commit: `Document operating system and file management`. Pushed to `main`.
