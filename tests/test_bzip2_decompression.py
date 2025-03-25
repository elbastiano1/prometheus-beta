import os
import pytest
import bz2
from src.bzip2_decompression import decompress_bzip2_file

@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing."""
    sample_content = b"This is a test file for bzip2 decompression."
    compressed_file = tmp_path / "sample.txt.bz2"
    
    with bz2.open(compressed_file, 'wb') as f:
        f.write(sample_content)
    
    return compressed_file

def test_decompress_valid_bzip2_file(sample_bzip2_file, tmp_path):
    """Test decompressing a valid bzip2 file."""
    output_path = tmp_path / "decompressed.txt"
    result = decompress_bzip2_file(str(sample_bzip2_file), str(output_path))
    
    assert os.path.exists(result)
    with open(result, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_without_output_path(sample_bzip2_file, tmp_path):
    """Test decompressing with auto-generated output path."""
    result = decompress_bzip2_file(str(sample_bzip2_file))
    
    assert os.path.exists(result)
    with open(result, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("/path/to/nonexistent/file.bz2")

def test_decompress_invalid_bzip2_file(tmp_path):
    """Test handling of invalid bzip2 file."""
    invalid_file = tmp_path / "invalid.bz2"
    with open(invalid_file, 'wb') as f:
        f.write(b"Not a valid bzip2 file")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_file))

def test_decompress_multiple_times(sample_bzip2_file, tmp_path):
    """Test that multiple decompressions work correctly."""
    output_paths = []
    for _ in range(3):
        output_path = tmp_path / f"decompressed_{len(output_paths)}.txt"
        result = decompress_bzip2_file(str(sample_bzip2_file), str(output_path))
        output_paths.append(result)
        
        with open(result, 'rb') as f:
            content = f.read()
        assert content == b"This is a test file for bzip2 decompression."
    
    # Ensure each output path is unique
    assert len(set(output_paths)) == 3