import os

def make_sub_dirs():
	fold_template = "%02d"
	file_template = "%02d.md"

	for i in range(20):
		folder = fold_template % (i+1)
		file = file_template % (i+1)
		os.mkdir(folder)
		location = os.path.join(folder, file)
		description = open(location, 'w')
		description.write(template(i+1))

def template(number):
	return '''%02d : 

Summary: 
	''' % number

def get_file_addresses():
	addresses = []
	folders = os.listdir('.')

	for folder in folders:
		try:
			int(folder)
			# print(folder)
			files = os.listdir(folder)
			# print(files)
			for file in files:
				if folder in file:
					addresses.append(os.path.join(folder, file))
		except:
			continue
	return sorted(addresses)

def extract_summary(file_name):
	header = '#[%s](%s)'
	output = ''
	with open(file_name, 'r') as text:
		output += header % (text.readline(), file_name)
		output += text.readline()
		output += text.readline()

	return output+'\n'
def generate_readme():
	addresses = get_file_addresses()
	# print(addresses)
	block_text = ''
	for project in addresses:
		block_text += extract_summary(project)
	readme = open('readme.md', 'w')
	readme.write(block_text)

def main():
	# make_sub_dirs()
	generate_readme()

if __name__ == '__main__':
	main()