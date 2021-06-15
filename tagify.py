import sys, getopt

def tag(input_str, outputfile = "tags.txt", file = True):
     # read in names tag file 
    member_lst = []

    if file:

        with open(input_str, "r", encoding="utf8") as f:
            member_lst = f.readlines()
        print(member_lst)

    else:
        member_lst = input_str
    # create tag file
    members = ["@" + member for member in member_lst.split(", ")]
    member_str = " ".join(members);
    
    print(member_str)
    
    with open(outputfile, "w", encoding="utf8") as of:
        of.write(member_str)
    

def main(argv):
    inputfile = ''
    outputfile = ''

    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])

    except getopt.GetoptError:
       print ('tagify.py -i <inputfile> -o <outputfile>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print ('tagify.py -i <inputfile> -o <outputfile>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg

    if inputfile == '':
        print("Copy in your input: \n")
        inputfile = input()
        tag(inputfile, file=False)

    elif outputfile == '':
        tag(inputfile)

    else:
        tag(inputfile, outputfile, True)

if __name__ == "__main__":
   main(sys.argv[1:])
