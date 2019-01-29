import sys
from readInputTextFile import readInputTextFile
from deleteOutlier import deleteOutlier
from remainOddOrEven import remainOddOrEven
from countNumOfUnique import countNumOfUnique

def myOwnCounter(filename):
    """Our Final Function
    
    Arguments:
        filename {[string]} -- [input file name]
    
    Returns:
        [int] -- [result]
    """
    a1=readInputTextFile(filename)
    a2=deleteOutlier(a1)
    a3=remainOddOrEven(a2)
    num_of_uniq=countNumOfUnique(a3)
    
    return num_of_uniq

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = "input.txt"
    else:
        filename = sys.argv[1]
    print("Answer in {}".format(myOwnCounter(filename)))
