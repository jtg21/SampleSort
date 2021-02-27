import os, shutil
import re

SPLICE_DIR = "/Users/jasperemhoff/Music/Splice/sounds/packs"
MUSIC_DIR = "/Users/jasperemhoff/Music/A1/"
KEYWORDS = ["kick", "snare", "hihat", "loop", "synth", "fx", 
			"vox", "build", "vocal", "brass", "trap", "808", "riser", "break", 
			"clap", "snap", "tom", "crash", "ride", "percussion", "block", 
			"bass", "lead", "whitenoise", "reverse", "chop", "clock", "sample"]

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = []
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)

        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

# pass a list of all the sample strings
def sortSamples(samples, newdir):
	total_count = 0

	if (newdir):
		clearDir(MUSIC_DIR)

	for keyword in KEYWORDS:
		count = 1
		print("Samples: ", keyword.upper())
		
		#Create sub diretory for keyword name if newdir is true
		path = MUSIC_DIR + keyword.upper()
		if (newdir):
			os.mkdir(path)

		for sample in samples:

			# removes the dir path from the sample string
			filtered = re.search("\\/+(\\w)*\\.(wav|aif|mp3)+", sample)

			if (filtered):
				filtered = filtered.group()

				# removes the / on the sample string
				filtered = filtered[1:]

				if keyword in filtered.lower():
					# copies sample to dir labeled KEYWORD
					shutil.copy(sample, path)
					print(count,":", filtered)
					count += 1

		total_count += count;
		print("==========\n")

	print("All samples listed")
	print("Total samples sorted: ", total_count)
	print("Total samples passed: ", len(samples))
	print("Total coverage: ", (total_count/len(samples))*100, "%")
	print()


# Sorts a given keyword by musical key then places those files into respective sub dirs
def sortByKey(dirName):
	# path in which to create sub directories
	path = MUSIC_DIR + dirName.upper()

	# array that holds what keys we've seen so far
	keys = []

	listOfFile = os.listdir(path)
	
	for file in listOfFile:
		filtered = re.search("([a-z]|[A-Z])*\\.[a-z]+", file)
		if (filtered):
			filtered = filtered.group()
			filtered = filtered[:len(filtered)-4]

			if filtered not in keys:
				keys.append(filtered)
	print(keys)

# Clears the directory before starting the file sort
def clearDir(dirName):
	listOfFile = os.listdir(dirName)

	for file in listOfFile:
		if "." not in file:
			print(file)
			path = MUSIC_DIR + file
			shutil.rmtree(path)

