# create and open two txt files
infiles = open("input.txt","r+")                       
outfiles = open("output.txt","r+")

Ofiles = infiles.readlines()             # read the lines of the input txt files

def min():                               # create a function called min
    files = Ofiles[0]                    # work on the min number line to find the min number
    min = files.split(",")               # split the number you're working with
    min1 = files.replace("min:1","1")    # replace "min:1" with "1"
    min2 = min1.split(",")
    print(f" The min of {min2} is {min2[0]}")   # print out your findings
    outfiles.write(f" The min of {min2} is {min2[0]}\n") # write your finding on the output txt file
    outfiles.readline()


min()                                    # call the min function


def max():                               # create a function called max
    files1 = Ofiles[1]                   # work on the max number line to find the min number
    max = files1.split(",")              # split the number you're working with
    max1 = files1.replace("max:1","1")   # replace "max:1" with "1"
    max2 = max1.split(",")
    print(f" The max of {max2} is {max1[-2]}")   # print out your finding
    outfiles.write(f" The max of {max2} is {max1[-2]}\n") # write your finding on the output txt file
    outfiles.readline()


max()                                    # call the max function

def avg():                               # create a function called avg
    files2 = Ofiles[2]                   # work on the avg number line to find the min number
    avg = files2              # remove the ":" in the avg line
    avg1 = avg.replace("avg:1","1")      # replace "avg:1" with "1" 
    avg2 = avg1.strip()
    avg3 = avg2.split(",")
    avg4 = int(avg3[0])+int(avg3[1])+int(avg3[2])+int(avg3[3])+int(avg3[4])+int(avg3[5])
    avg5 = avg4 / len(avg3)
    print(f"The avg of {avg3} is {avg5}")  # print out your finding
    outfiles.write(f"The avg of {avg3} is {avg5}") # write your finding on the output txt file
    outfiles.readline()
    outfiles.close()                     # close both of the txt files
    infiles.close()

avg()                                   # call the avg function