def countNumOfUnique(int_list):
    """Count number of diff int
    
    Arguments:
        int_list {[list of int]} -- [only odd or even ints]
    
    Returns:
        [int] -- [number of diff int]
    """
    set_of_number = set(int_list)
    num_of_uniq = len(set_of_number)
    return num_of_uniq