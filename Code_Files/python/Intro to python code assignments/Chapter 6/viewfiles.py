import os

def displayFiles(path, indent=""):
    if not os.path.exists(path):
        print("Path does not exist:", path)
        return

    if os.path.isfile(path):
        # If the path is a file, display its name and contents
        print(indent + "File name:", path)
        with open(path, 'r') as file:
            print(file.read())
    elif os.path.isdir(path):
        # If the path is a directory, display its name and call the function recursively for each entry
        print(indent + "Directory name:", path)
        entries = os.listdir(path)
        for entry in entries:
            entry_path = os.path.join(path, entry)
            displayFiles(entry_path, indent + "    ")
    else:
        print("Invalid path:", path)

def main():
    path = input("Enter the pathname of a file or directory: ")
    displayFiles(path)

if __name__ == "__main__":
    main()
