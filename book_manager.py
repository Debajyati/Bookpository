import os

def list_all_files(directory):
    exclude_dirs = [os.path.join(directory, '.git')]
    exclude_files = [os.path.join(directory, 'README.md'), os.path.join(directory, 'book_manager.py')]

    toc_lines = []
    for root, dirs, files in os.walk(directory):
        # Exclude specific directories by modifying dirs in-place
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in exclude_files:
                # Create table of contents line with proper indentation
                toc_line = f"1. ***{(root[2:]).upper()}*** --> [{file.capitalize()}]({file_path})"
                toc_lines.append(toc_line)

    return toc_lines

# Example usage
directory = '.'
toc = list_all_files(directory)
toc.sort()
# Write the table of contents to README.md
with open('README.md', 'w') as readme:
    readme.write("# Books Pository\n\n")
    readme.write("### A bundle of books in pdf/html format that may be helpful for CSE/IT students\n ")
    for line in toc:
        readme.write(line + '\n')
    readme.write("\n ## ***Automated by [BookManager](./book_manager.py)***")
    readme.write("\n[N.S. If anyone finds any book useful then he/she should purchase that book.]")
