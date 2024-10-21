import os
import zipfile

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
    directory_to_compress = 'path/to/your/directory'  # Change this to your directory
    output_zip_file = 'compressed_files.zip'  # Name of the output zip file
    compress_files(directory_to_compress, output_zip_file)
