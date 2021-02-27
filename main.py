from samplesort import sortSamples, getListOfFiles, SPLICE_DIR



def main():
	isNewDir = input("Are you creating a fresh sort? (y / n): ")
	if (isNewDir == "y"):
		samples = getListOfFiles(SPLICE_DIR)
		sortSamples(samples, True)
	else:
		dirPath = input("What is the directory you would like to sort?: ")
		try:
			samples = getListOfFiles(dirPath)
			sortSamples(samples, False)
		except:
			print("Sorry that wasn't a valid directory!")
			quit = input("Would you like to quite?")
			if quit == "y":
				return
			else:
				main()



if __name__ == "__main__":
	main()