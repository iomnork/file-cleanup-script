# File Cleanup Script

This is a simple Python automation tool designed to clean up directories by sorting files into organized folders based on file type, extension, or date.

## 🛠️ Features

- Automatically scans a folder and organizes files
- Sorts by:
  - File type (e.g., Images, Documents, Archives)
  - Extension (e.g., `.jpg`, `.pdf`, `.zip`)
  - Or creation/modification date
- Safe to run repeatedly

## 🚀 Getting Started

1. Clone this repo  
```bash
git clone https://github.com/yourusername/file-cleanup-script.git
```

2. Run the script
```bash
python cleanup.py
```
3. Customize the target folder

Open the cleanup.py file and change the target_directory variable to the path you want to clean up.

## 💡 Example Use Cases
Clean your Downloads folder every week

Sort screenshots, PDFs, and images from your Desktop

Organize project folders by file type

## ✅ To Do
 - [ ] Add config file support
 - [ ] Add log output
 - [ ] Add dry-run preview mode
 - [ ] Add support for auto-scheduling (e.g. Task Scheduler or cron)
 - [ ] Add recursive subfolder support

## 🧠 Why I Built This
This is one of my first real-world Python automation projects. It’s a tool I’ll actually use — and a way for me to practice writing cleaner, more modular code. More features will come as I grow.

## 📄 License
This project is licensed under the MIT License.

## 🙌 Contributions
Got suggestions? Feel free to fork this repo, submit a pull request, or open an issue.
