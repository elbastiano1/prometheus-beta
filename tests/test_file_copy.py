import os
import pytest
import shutil
import tempfile

from src.file_copy import copy_file

def test_successful_file_copy():
    """Test successful file copy operation."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create source file
        source_path = os.path.join(temp_dir, 'source.txt')
        dest_path = os.path.join(temp_dir, 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write("Test content")
        
        # Copy file
        result = copy_file(source_path, dest_path)
        
        # Verify
        assert result is True
        assert os.path.exists(dest_path)
        with open(dest_path, 'r') as f:
            assert f.read() == "Test content"

def test_copy_to_nested_directory():
    """Test copying a file to a nested directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source.txt')
        dest_path = os.path.join(temp_dir, 'nested', 'sub', 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write("Nested directory test")
        
        result = copy_file(source_path, dest_path)
        
        assert result is True
        assert os.path.exists(dest_path)

def test_nonexistent_source_file():
    """Test copying a nonexistent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'nonexistent.txt')
        dest_path = os.path.join(temp_dir, 'destination.txt')
        
        with pytest.raises(FileNotFoundError):
            copy_file(source_path, dest_path)

def test_source_is_directory():
    """Test attempting to copy a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source_dir')
        os.makedirs(source_dir)
        dest_path = os.path.join(temp_dir, 'destination.txt')
        
        with pytest.raises(IsADirectoryError):
            copy_file(source_dir, dest_path)

def test_copy_large_file():
    """Test copying a larger file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'large_source.txt')
        dest_path = os.path.join(temp_dir, 'large_destination.txt')
        
        # Create a larger file
        with open(source_path, 'w') as f:
            f.write('x' * 1000000)  # 1 MB of data
        
        result = copy_file(source_path, dest_path)
        
        assert result is True
        assert os.path.exists(dest_path)
        assert os.path.getsize(source_path) == os.path.getsize(dest_path)