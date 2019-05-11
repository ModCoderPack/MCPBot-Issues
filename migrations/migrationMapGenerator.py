import re
import sys

# This script generates IntelliJ migration maps from the CSV files, allowing you to automatically
#   perform renames across your entire project all at once.
# Usage: python migrationMapGenerator.py <input.csv|input.tsrg> <output path>
# Then, drop the resulting XML file into your Intellij migrations directory. 
#   This is usually <USER FOLDER>/.IdeaIC2018.3/config/migrations/ or similar
# Restart IntelliJ, then do Ctrl+Shift+A -> Migrate -> Select the XML -> Run -> Do refactor

def main():
	tsrgmode = False
	infile = open(sys.argv[1], "r")
	outfile = open(sys.argv[2], "w")

	if sys.argv[1].endswith(".tsrg"):
		tsrgmode = True
	
	# Python's XML libraries aren't really nice to use and we aren't doing anything complicated
	# So just hard-emit the XML
	print('<?xml version="1.0" encoding="UTF-8"?>', file=outfile)
	print('<migrationMap>', file=outfile)
	print(f'\t<name value="{sys.argv[1]}" />', file=outfile)
	print(f'\t<description value="{sys.argv[1]}" />', file=outfile)

	for line in infile:
		try:
			# Strip comments in tsrg files
			if tsrgmode:
				line = re.sub(r"#.*$", "", line).strip()
			old, new = line.split() if tsrgmode else line.split(',')
			old = old.replace("/", ".").replace("$", ".").strip()
			new = new.replace("/", ".").replace("$", ".").strip()
			entry = f'\t<entry oldName="{old}" newName="{new}" type="class" />'
			print(entry, file=outfile)
		except:
			print(f"Error at line {line}")

	print('</migrationMap>', file=outfile)

if __name__ == "__main__":
	main()
