# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface to inspect folders, create and manage practice files, understand options and pipes, and explain package managers.

## 2. Work completed
Completed basic Terminal exploration operations, safe file change practice inside `terminal-practice`, flag and pipe comparisons, and Homebrew package manager notes.

## 3. Commands / tools used
* **Terminal (CLI):** Used for executing directory navigation, file creation, copy, and move operations.
* **VS Code:** Used for editing the mission README file.

## 4. My understanding
* **Command Line Interface (CLI):** Allows fast and direct interaction with the operating system using text instructions rather than a graphical interface.
* **Flags & Pipes:** Flags (options) modify how commands behave, while pipes (`|`) let the output of one command flow directly into another.
* **Package Managers:** Tools like Homebrew automate software installation, upgrades, and removal safely.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-02-terminal/README.md`
* `terminal-practice/` folder containing test files

## 8. Commit details
Committed with the message: "Complete Terminal and file management mission"

---

### Task 2.1: Explore basic Terminal operations
| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Displays the full absolute path of the folder you are currently working in. | Printed the complete path starting from the root directory. |
| **Directory listing (`ls`)** | List the files and folders in the current location. | Displayed names of files and subdirectories horizontally/vertically. |
| **Detailed listing (`ls -l`)** | Display the listing in a detailed format. | Showed file permissions, link counts, owners, sizes, and modification dates. |
| **Change directory (`cd ..`)** | Move to the parent folder and identify how your current location changes. | Shifted the working directory level one step up in the directory tree. |
| **Create directory (`mkdir`)** | Create a new practice folder. | Generated a new empty subdirectory successfully. |
| **Create empty file (`touch`)** | Create an empty text file inside the practice folder. | Created a zero-byte text file instantly. |
| **Copy file (`cp`)** | Make a copy of that file with a different name. | Duplicated the original file contents into a new backup filename. |
| **Move / rename file (`mv`)** | Rename or moved the copied file. | Changed the filename or moved it to a new path location. |
| **Display file contents (`cat`)** | Display the contents of the original text file. | Outputted all text lines inside the file directly to the Terminal window. |

### Task 2.2: Practice file changes safely
* **Difference between replacing file contents vs. adding text:** Replacing overwrites all existing data completely (e.g., using `>`), whereas appending adds text to the end of the file without erasing previous lines (e.g., using `>>`).
* **Difference between copying and moving a file:** Copying (`cp`) duplicates the file, leaving the original intact at the source. Moving (`mv`) relocates or renames the original file, removing it from its original location.
* **Information provided by current-directory display (`pwd`):** It provides your exact location path within the computer's file directory tree, preventing you from modifying files in the wrong place.
* **Usefulness of directory listing (`ls`):** It helps you instantly check what files and folders are available before executing commands on them.

### Task 2.3: Understand flags and pipes
* **Flags/Options observation:** Running a normal `ls` shows basic names, whereas `ls -la` displays hidden files, detailed permissions, precise byte sizes, and modification timestamps.
* **Pipes (`|`) observation:** Piping a detailed listing into a line filter (e.g., `ls -la | head -n 3`) sends the output of the left side as input to the right side, restricting the display to only the first 3 lines.

### Task 2.4: Understand package managers
* **Homebrew / Package Managers:** A package manager is a utility that automates installing, configuring, updating, and removing software packages safely. On macOS, Homebrew manages packages efficiently by tracking dependencies without manual web downloads.
