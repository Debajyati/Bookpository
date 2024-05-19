# Import libraries
import os
import time

# Insert the directory path in here
path = '.'

# Extracting all the contents in the directory corresponding to path
l_files = os.listdir(path)

# Iterating over all the files
for file in l_files:

# Instantiating the path of the file
	file_path = f'{path}//{file}'

	# Checking whether the given file is a directory or not
	if os.path.isfile(file_path):
		try:
			# Printing the file pertaining to file_path
			os.startfile(file_path, 'print')
			print(f'Printing {file}')

			time.sleep(5)
		except:
			# Catching if any error occurs and alerting the user
			print(f'ALERT: {file} could not be printed! Please check\
			the associated softwares, or the file type.')
	else:
		print(f'ALERT: {file} is not a file, so can not be printed!')

print('Task finished!')
