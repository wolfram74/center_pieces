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

def main():
	make_sub_dirs()

if __name__ == '__main__':
	main()