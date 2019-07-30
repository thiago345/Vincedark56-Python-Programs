import glob

txt_list_folder = glob.glob("*.txt")

with open("output.txt", "w") as outfile:
	for f in txt_list_folder:
            outfile.write('\n'.join(txt_list_folder))
