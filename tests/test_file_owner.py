import os
import pytest
import tempfile
import pwd
from src.file_owner import get_file_owner

def test_get_file_owner_existing_file():
    """Test getting owner of an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
    try:
        # Get current user
        current_user = pwd.getpwuid(os.getuid()).pw_name
        
        # Test the function
        owner = get_file_owner(temp_path)
        assert owner == current_user, f"Expected owner {current_user}, got {owner}"
    
    finally:
        # Clean up
        os.unlink(temp_path)

def test_get_file_owner_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_owner('/path/to/nonexistent/file.txt')

def test_get_file_owner_permissions():
    """Test handling of files with different permissions."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
    try:
        # Remove all permissions
        os.chmod(temp_path, 0o000)
        
        # Should still return the owner
        current_user = pwd.getpwuid(os.getuid()).pw_name
        owner = get_file_owner(temp_path)
        assert owner == current_user
    
    finally:
        # Restore permissions and clean up
        os.chmod(temp_path, 0o644)
        os.unlink(temp_path)

def test_get_file_owner_is_string():
    """Verify the returned owner is a non-empty string."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
    try:
        owner = get_file_owner(temp_path)
        assert isinstance(owner, str), "Owner should be a string"
        assert len(owner) > 0, "Owner string should not be empty"
    
    finally:
        os.unlink(temp_path)