import bz2
import os

def decompress_bzip2_file(input_file_path, output_file_path=None):
    """
    Decompress a bzip2-compressed file.

    Args:
        input_file_path (str): Path to the bzip2-compressed input file.
        output_file_path (str, optional): Path to save the decompressed file.
            If not provided, uses input filename without .bz2 extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If input file is not a valid bzip2 compressed file.
        PermissionError: If there are permission issues writing the output file.
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file {input_file_path} does not exist.")

    # Determine output file path
    if output_file_path is None:
        # Remove .bz2 extension if present
        output_file_path = input_file_path.removesuffix('.bz2') if input_file_path.endswith('.bz2') else input_file_path + '_decompressed'

    try:
        # Open and read compressed file
        with bz2.open(input_file_path, 'rb') as compressed_file:
            # Open output file in write binary mode
            with open(output_file_path, 'wb') as output_file:
                # Try to read and decompress contents
                decompressed_content = compressed_file.read()
                
                # Validate that decompression worked
                if not decompressed_content:
                    raise ValueError(f"Invalid bzip2 compressed file: {input_file_path}")
                
                # Write decompressed contents
                output_file.write(decompressed_content)

        return output_file_path

    except (OSError, EOFError):
        raise ValueError(f"Invalid bzip2 compressed file: {input_file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to {output_file_path}")