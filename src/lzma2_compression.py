import lzma
import io

def lzma2_compress(data):
    """
    Compress input data using LZMA2 compression algorithm.

    Args:
        data (bytes or str): The input data to be compressed.
            If str is provided, it will be encoded to UTF-8 bytes.

    Returns:
        bytes: Compressed data using LZMA2 compression.

    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA2 (LZMA with advanced features)
    try:
        # Use LZMA compression with LZMA2 preset
        compressed = lzma.compress(data, preset=lzma.PRESET_DEFAULT)
        return compressed
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzma2_decompress(compressed_data):
    """
    Decompress LZMA2 compressed data.

    Args:
        compressed_data (bytes): The compressed data to be decompressed.

    Returns:
        bytes: Decompressed original data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompress using LZMA2
    try:
        decompressed = lzma.decompress(compressed_data)
        return decompressed
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Decompression failed: {str(e)}")