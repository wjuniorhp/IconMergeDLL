# IconMergeDLL

A Python script that compiles `.ico` files into a single .dll file using Resource Hacker.

## Prerequisites

- Install [Resource Hacker](http://www.angusj.com/resourcehacker/).
- Create a template `.dll` file (or get iit from this repo's files).

## Configuration

1. Edit the paths in the script:
    - `RESOURCE_HACKER_PATH`: Path to the Resource Hacker executable.
    - `TEMPLATE_DLL_FILE`: Path to the template `.dll` file.
    - `OUTPUT_FOLDER`: Folder containing subfolders with the icon files.

2. Place Your Icons:
    - Place your `.ico` files into subfolders inside the OUTPUT_FOLDER.

3. Run the Script:
    - Execute the Python script. It will process each subfolder within the `OUTPUT_FOLDER`, creating `.dll` files that contain the icons from each subfolder.

## How It Works

The script performs the following steps for each subfolder within the `OUTPUT_FOLDER`:

1. Creates a `.rc` file listing all `.ico` files in the subfolder.
2. Copies the template `.dll` file to create a new `.dll` file.
3. Compiles the `.rc` file into a `.res` file using Resource Hacker.
4. Compiles the `.res` file into the new `.dll` file using Resource Hacker.
5. Deletes the intermediate `.rc` and `.res` files.

## Usage

```python
# Paths to Resource Hacker executable and template .dll file
RESOURCE_HACKER_PATH = r"Path\to\ResourceHacker.exe"
TEMPLATE_DLL_FILE = r"Path\to\template.dll"
OUTPUT_FOLDER = r"Path\to\output\folder"

# Create and compile .rc files to .dll
if __name__ == "__main__":
    for folder in os.listdir(OUTPUT_FOLDER):
        folder_path = os.path.join(OUTPUT_FOLDER, folder)
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder}")
            create_rc_and_dll(folder_path)
```

## Example

1. Directory Structure:
    ```
    OUTPUT_FOLDER
    │
    ├── Folder1
    │   ├── icon1.ico
    │   └── icon2.ico
    │
    ├── Folder2
    │   ├── iconA.ico
    │   └── iconB.ico
    │
    └── .template.dll
    ```

2. Run the Script:
    - The script will generate `Folder1.dll` and `Folder2.dll` containing the icons from `Folder1` and `Folder2`, respectively.
