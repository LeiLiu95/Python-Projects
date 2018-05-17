#  File: DNA.py

#  Description: Find longest DNA strand

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10-25-16

#  Date Last Modified: 10-26-16

def main():
  # open file for reading
	in_file = open ("dna.txt", "r")

  # read the number of pairs
	num_pairs = in_file.readline()
	num_pairs = num_pairs.strip()
	num_pairs = int (num_pairs)

  # read each pair of dna strands
	if (num_pairs>0):
		print("Longest Common Sequences")
		print()
	else:
		in_file.close()
		return
	for i in range (num_pairs):
		pair=str(i+1)
		print("Pair "+ pair+ ": ",end="")
		st1 = in_file.readline()
		st2 = in_file.readline()

		st1 = st1.strip()
		st2 = st2.strip()

		st1 = st1.upper()
		st2 = st2.upper()

    # order strands by size
		if (len(st1) > len(st2)):
			dna1 = st1
			dna2 = st2
		else:
			dna1 = st2
			dna2 = st1

	    # get all substrings of dna2
		wnd = len (dna2)
		found=False
		while (wnd > 1):
			start_idx = 0
			while ((start_idx + wnd) <= len (dna2)):
				sub_strand = dna2[start_idx: start_idx + wnd]
				if(found==False):
					if(dna1.find(sub_strand)!=-1):
						print (sub_strand)
						found=True
				else:
					if(dna1.find(sub_strand)!=-1):
						space=8
						if(i+1>=10 and i+1<100):
							space=7
						if(i+1>=100):
							space=6
						print(" "*8+sub_strand)		
	        # shift window by one
				start_idx += 1
	      # decrease window size
			wnd = wnd - 1
			if(found==True):
				break
		if(found==False):
			print("No Common Sequence Found")
		print()
  # close file
	in_file.close()

main()