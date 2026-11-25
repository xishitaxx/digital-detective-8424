# Mission 3 - Understand the operating system

## 1. Task / objective
Explore the operating system environment, active account, storage space, running processes, paths, file permissions, and core OS responsibilities.

## 2. Work completed
Checked system details, active user identity, disk usage, and running processes in Terminal, practiced navigating paths, inspected file permissions, and completed the OS responsibilities table.

## 3. Commands / tools used
* **Terminal / shell:** Used to inspect OS info, user account, storage, processes, paths, and file permissions.
* **Activity Monitor / Task Manager or `ps`:** Used to view running processes and their Process IDs (PIDs).
* **VS Code:** Used to write and format the Mission 3 README.

## 4. My understanding
* **System & Storage Info:** Checking OS details, active account, and storage helps you understand the environment you are working in and ensure enough free disk space is available.
* **Processes & PIDs:** A process is a running program, and its Process ID (PID) uniquely identifies it so the OS can track and manage it.
* **Paths & Permissions:** An absolute path starts from the root directory, while a relative path is measured from your current directory. Permissions (`r`, `w`, `x`) control whether the owner, group, or others can read, write, or execute files/directories.
* **OS Responsibilities:** The operating system coordinates hardware and software by managing processes, memory, devices, files, user interfaces, and security.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-03-operating-system/README.md`

## 8. Commit details
Committed with the message: "Document operating system and file management"

---

### Task 3.1: Explore your operating system
| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Shows the OS name, version, kernel, or architecture your machine runs on. | Observed OS and kernel details in Terminal (`[redacted]` device/host info). |
| **Current account identity** | Shows which user account is currently running commands in the session. | Active account confirmed as `[redacted]`. |
| **Available and used storage** | Shows total, used, and free space across filesystems or drives. | Checked used and available capacity; sufficient free space is available. |
| **System activity snapshot** | Shows a brief view of active processes and system resource usage. | Observed running tasks and CPU/memory activity with personal details redacted. |

### Task 3.2: Understand processes
* **What is a process?** A process is a program currently loaded into memory and running on the computer.
* **What does the PID column represent?** PID stands for Process Identifier—a unique number assigned by the OS to identify each running process.
* **Two examples of running processes:** A web browser (such as Chrome or Safari) and a text editor or terminal process.

### Task 3.3: Understand paths and permissions
* **Absolute vs. relative path:** An **absolute path** gives the full location from the root of the filesystem (for example, `/Users/[redacted]/digital-detective-XXXX/mission-03-operating-system`), while a **relative path** starts from your current working directory (for example, `mission-03-operating-system` from the project root, or `..` to move up one level).
* **File permissions observation:** Checked a detailed listing for a file in the practice area and reviewed the owner permission bits (`r` for read, `w` for write, `x` for execute) to see what the owner is allowed to do without changing any system permissions.

### Task 3.4: Explain operating-system responsibilities
| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Creates, schedules, and manages running programs so they share CPU time fairly. | Running a browser and a text editor at the same time. |
| **Memory management** | Allocates RAM to running programs and frees memory when programs close. | Giving memory to an app when opened and reclaiming it when quit. |
| **Device management** | Coordinates communication between the OS/apps and connected hardware via drivers. | Sending output to a display, keyboard, or printer. |
| **File management** | Organizes files and folders and tracks where data is stored on storage devices. | Creating, saving, renaming, and deleting files in folders. |
| **User interface / shell** | Provides the visual desktop or command-line shell for users to give instructions. | Typing commands in Terminal or clicking icons on the desktop. |
| **Security and permissions** | Enforces user accounts and access rules so unauthorized users cannot alter protected data. | Restricting write access to files owned by another user or system area. |
