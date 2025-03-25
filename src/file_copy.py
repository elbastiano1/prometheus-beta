import os
import shutil

def copy_file(source_path: str, destination_path: str) -> bool:
    """
    Copy a file from source path to destination path.

    Args:
        source_path (str): The full path to the source file.
        destination_path (str): The full path to the destination file.

    Returns:
        bool: True if the file was successfully copied, False otherwise.

    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If source path is a directory.
        PermissionError: If there are insufficient permissions to read source or write destination.
    """
    try:
        # Validate source file exists and is a file
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {source_path}")
        
        if not os.path.isfile(source_path):
            raise IsADirectoryError(f"Source path is not a file: {source_path}")
        
        # Ensure destination directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Perform the file copy
        shutil.copy2(source_path, destination_path)
        return True
    
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        # Re-raise specific exceptions for clear error handling
        raise
    except Exception as e:
        # Catch any unexpected errors
        print(f"Unexpected error during file copy: {e}")
        return False