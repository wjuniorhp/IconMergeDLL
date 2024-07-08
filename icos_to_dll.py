import os
import subprocess
import shutil

# Paths to Resource Hacker executable and template .dll filefile
RESOURCE_HACKER_PATH = r"Path\to\ResourceHacker.exe"
TEMPLATE_DLL_FILE = r"Path\to\template.dll"
OUTPUT_FOLDER = r"Path\to\output\folder"

def create_rc_file(icon_folder, rc_file):
    """
    Create a resource (.rc) file based on the icon files in the specified folder.

    Parameters:
    icon_folder (str): The path to the folder containing the icon files.
    rc_file (str): The path to the output resource file (.rc).

    Returns:
    None
    """
    icon_files = [f for f in os.listdir(icon_folder) if f.endswith('.ico')]
    with open(rc_file, 'w') as rc:
        for i, icon_file in enumerate(icon_files):
            icon_path = os.path.join(icon_folder, icon_file)
            rc.write(f'ICON_{i+1} ICON "{icon_path}"\n')

def compile_rc_to_res(resource_hacker_path, rc_file, res_file):
    """
    Compiles a resource (.rc) file into a .res file using Resource Hacker.

    Args:
        resource_hacker_path (str): The path to the Resource Hacker executable.
        rc_file (str): The path to the input resource file (.rc).
        res_file (str): The path to the output resource file (.res).

    Returns:
        None
    """
    cmd = [
        resource_hacker_path,
        '-open', rc_file,
        '-save', res_file,
        '-action', 'compile'
    ]
    subprocess.run(cmd, check=True)

def compile_res_to_dll(resource_hacker_path, res_file, output_dll):
    """
    Compiles a .res file into a .dll file using Resource Hacker.

    Args:
        resource_hacker_path (str): The path to the Resource Hacker executable.
        res_file (str): The path to the input resource file (.res).
        output_dll (str): The path to the output DLL file.

    Raises:
        subprocess.CalledProcessError: If the subprocess call returns a non-zero exit code.

    Returns:
        None
    """
    cmd = [
        resource_hacker_path,
        '-open', output_dll,
        '-save', output_dll,
        '-resource', res_file,
        '-action', 'addoverwrite'
    ]
    subprocess.run(cmd, check=True)

def copy_template(destination_dll):
    """
    Copies a template .dll file to the specified destination.

    Args:
        destination_dll (str): The path to copy the template .dll file to.

    Returns:
        None
    """
    shutil.copyfile(TEMPLATE_DLL_FILE, destination_dll)

def compile_dll(icon_folder):
    """
    Create the .rc file and compile it into a .dll file.

    Args:
        icon_folder (str): The path to the folder containing the icon files.

    Returns:
        None

    Raises:
        FileNotFoundError: If the folder or the template .dll file does not exist.
        subprocess.CalledProcessError: If the subprocess call returns a non-zero exit code.

    This function creates a .rc file based on the icon files in the specified folder.
    It then copies the template .dll file and compiles the .rc file into a .res file.
    Finally, it compiles the .res file into a .dll file.

    The .rc and .res files are deleted after the compilation process.

    Example usage:
    ```
    compile_dll("my_folder")
    ```
    """
    # Create the .rc file
    rc_file = os.path.join(OUTPUT_FOLDER, f'{icon_folder}.rc')
    create_rc_file(icon_folder, rc_file)

    # Copy the .dll file from the template
    dll_file = os.path.join(OUTPUT_FOLDER, f'{icon_folder}.dll')
    copy_template(dll_file)

    # Compile the .rc file into a .res
    res_file = os.path.join(OUTPUT_FOLDER, f'{icon_folder}.res')
    compile_rc_to_res(RESOURCE_HACKER_PATH, rc_file, res_file)

    # Compile the .res file into a .dll
    compile_res_to_dll(RESOURCE_HACKER_PATH, res_file, dll_file)
    
    print(f"Icons compiled into {dll_file}")

    os.remove(rc_file)
    os.remove(res_file)

if __name__ == "__main__":
    for folder in os.listdir(OUTPUT_FOLDER):
        folder_path = os.path.join(OUTPUT_FOLDER, folder)
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder}")
            compile_dll(folder_path)
