import os

def list_all_files(directory):
    exclude_dirs = [os.path.join(directory, '.git')]
    exclude_files = [os.path.join(directory, 'new.py'), os.path.join(directory,'README.md'), os.path.join(directory,'book_manager.py')]

    for root, dirs, files in os.walk(directory):
        # Exclude specific directories by modifying dirs in-place
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        
        # Exclude specific files
        for file in files:
            file_path = file
            if file_path not in exclude_files:
                print([root] , file_path)

# Example usage
directory = '/home/rockingsnp/Desktop/Python/Debo/Bookpository'
exclude_directories = [os.path.join(directory, '.git'), os.path.join(directory, 'another_directory')]
exclude_files = [os.path.join(directory, 'file_to_exclude.txt'), os.path.join(directory, 'another_file_to_exclude.txt')]

list_all_files(directory)
