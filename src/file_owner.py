import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by username.

    Args:
        file_path (str): Path to the file whose owner is to be retrieved.

    Returns:
        str: Username of the file owner.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        OSError: If there's an error retrieving the file owner.
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file stats
        file_stat = os.stat(file_path)
        
        # Convert user ID to username
        return pwd.getpwuid(file_stat.st_uid).pw_name
    
    except (OSError, KeyError) as e:
        raise OSError(f"Could not retrieve file owner: {e}")