
import os
import hashlib
import shutil

def find_duplicates(source_directory, destination_directory):
    # Create a dictionary to store the file paths and their corresponding SHA-1 hashes
    files_dict = {}

    # Traverse through the source directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(source_directory):
        # Loop through the filenames
        for filename in filenames:
            # Get the full path of the file
            filepath = os.path.join(dirpath, filename)

            # Calculate the SHA-1 hash of the file
            with open(filepath, 'rb') as file:
                file_hash = hashlib.sha1(file.read()).hexdigest()

            # Check if the hash already exists in the dictionary
            if file_hash in files_dict:
                # Duplicate file found, move the duplicate file to the destination directory
                new_filepath = os.path.join(destination_directory, filename)
                shutil.move(filepath, new_filepath)
                print(f"Duplicate moved: {filepath} -> {new_filepath}")
            else:
                # Add the file path and its hash to the dictionary
                files_dict[file_hash] = filepath

if __name__ == '__main__':
    source_directory = input("Enter source directory to search for duplicates: ")
    destination_directory = input("Enter destination directory to move duplicates: ")
    find_duplicates(source_directory, destination_directory)