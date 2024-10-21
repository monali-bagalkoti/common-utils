import os
import zipfile
import sys

def compress_files(directory, output_zip):
    # Create a zip file
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        # Walk through the directory
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                # Create a complete filepath
                file_path = os.path.join(foldername, filename)
                # Add file to the zip file
                zipf.write(file_path, os.path.relpath(file_path, directory))
    print(f'Files compressed into {output_zip}')

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compress.py <directory_to_compress> <output_zip_file>")
        sys.exit(1)

    directory_to_compress = sys.argv[1]
    output_zip_file = sys.argv[2]
    compress_files(directory_to_compress, output_zip_file)
