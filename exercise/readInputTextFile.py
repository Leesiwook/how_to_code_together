def readInputTextFile(filename):
    """Read input file(filename) and return list of int
    
    Arguments:
        filename {[string]} -- [name of input file]
    
    Returns:
        [list of int] -- [input list]
    """
    with open(filename, 'r') as f:
        content = f.read()

    str_list = content.split()
    int_list = [int(s) for s in str_list]
    return int_list