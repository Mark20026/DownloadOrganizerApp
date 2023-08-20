import os
import shutil


def main():
    downloads_path = get_downloads_path()
    print("Downloads Path:", downloads_path)

    create_folder_of_type()
    move_file()


def get_downloads_path():
    return os.path.join(os.path.expanduser("~"), "Downloads")


def finder():
    """
    Find every file in the Downloads folder.

    Yields:
        str: The full path of each file in the Downloads folder.
    """
    downloads_path = get_downloads_path()

    files_in_download = os.listdir(downloads_path)

    for file_name in files_in_download:
        yield os.path.join(downloads_path, file_name)


def check_file_type(file_path):
    """
    Check the type of the files
    """
    return os.path.splitext(file_path)[1]


def get_file_type():
    """
    Get unique file types (extensions) of files in the Downloads folder.

    Returns:
        List[str]: A list containing unique file types (extensions) of files in the Downloads folder.
    """
    file_types = []
    for file_path in finder():
        files = check_file_type(file_path)
        if files not in file_types and files != "":
            file_types.append(files)
    return file_types


def create_folder_of_type():
    """
    Create folders for unique file types (extensions) in the Downloads folder.

    Returns:
        List[str]: A list containing the paths of the newly created folders.
    """
    download_path = os.path.expanduser("~/Downloads")
    new_folders = []

    for file_type in get_file_type():
        new_folder = os.path.join(download_path, file_type)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
            new_folders.append(new_folder)

    return new_folders


def move_file():
    """
    Move files from the Downloads folder to their respective folders based on file types.

    This function iterates through the files in the Downloads folder and moves each file to a corresponding
    subfolder based on its file type (extension).

    Note: The function relies on the `get_file_type()` and `finder()` functions to obtain information about the
    unique file types and file paths in the Downloads folder.

    Returns:
        None
    """
    download_path = os.path.expanduser("~/Downloads")

    for file_type in get_file_type():
        new_folder = os.path.join(download_path, file_type)

        for file_path in finder():
            if check_file_type(file_path) == file_type:
                shutil.move(file_path, new_folder)


if __name__ == "__main__":
    main()