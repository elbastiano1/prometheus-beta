import pytest
import lzma
from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compress_decompress_text():
    """Test compression and decompression of text data."""
    original_text = "Hello, World! This is a test of LZMA2 compression."
    compressed = lzma2_compress(original_text)
    assert compressed != original_text.encode('utf-8')
    decompressed = lzma2_decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_lzma2_compress_decompress_bytes():
    """Test compression and decompression of byte data."""
    original_bytes = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    compressed = lzma2_compress(original_bytes)
    assert compressed != original_bytes
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_bytes

def test_lzma2_compress_empty_input():
    """Test handling of empty input for compression."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma2_compress("")
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma2_compress(b"")

def test_lzma2_decompress_empty_input():
    """Test handling of empty input for decompression."""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzma2_decompress(b"")

def test_lzma2_compress_invalid_type():
    """Test handling of invalid input types for compression."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma2_compress(123)
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma2_compress(["list", "of", "items"])

def test_lzma2_decompress_invalid_type():
    """Test handling of invalid input types for decompression."""
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma2_decompress("string")
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma2_decompress(456)

def test_lzma2_large_data_compression():
    """Test compression of a larger dataset."""
    large_text = "A" * 10000  # 10,000 character string
    compressed = lzma2_compress(large_text)
    assert len(compressed) < len(large_text)
    decompressed = lzma2_decompress(compressed)
    assert decompressed.decode('utf-8') == large_text

def test_lzma2_invalid_compressed_data():
    """Test decompression of invalid compressed data."""
    with pytest.raises(lzma.LZMAError):
        # Attempt to decompress random bytes
        lzma2_decompress(b'invalid compressed data')