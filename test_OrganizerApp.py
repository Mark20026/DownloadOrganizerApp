from OrganizerApp import get_file_type, create_folder_of_type, check_file_type
import os

def test_get_file_type():
    file_types = get_file_type()
    assert isinstance(file_types, list)
    assert all(isinstance(file_type, str) for file_type in file_types)

def test_create_folder_of_type():
    # Clean up any previous test runs
    test_download_path = os.path.expanduser("~/Downloads/test_folder")
    if os.path.exists(test_download_path):
        os.rmdir(test_download_path)

    # Run the function and check the result
    folders = create_folder_of_type()
    assert isinstance(folders, list)
    assert all(isinstance(folder, str) for folder in folders)

    # Check if the test folders have been created
    assert all(os.path.exists(folder) for folder in folders)

def test_check_file_type():
    # Prepare some test files in the test Downloads folder
    test_download_path = os.path.expanduser("~/Downloads/test_folder")
    os.makedirs(test_download_path, exist_ok=True)
    test_files = ["test1.txt", "test2.jpg", "test3.pdf"]
    for file_name in test_files:
        file_path = os.path.join(test_download_path, file_name)
        open(file_path, "a").close()

    # Run the function and check the result
    file_types = [check_file_type(file_path) for file_path in test_files]
    assert isinstance(file_types, list)
    assert all(isinstance(file_type, str) for file_type in file_types)
    assert file_types == [".txt", ".jpg", ".pdf"]