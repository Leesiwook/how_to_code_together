def deleteOutlier(int_list):
    modified_list=[]
    """Delelte outlier (not 10-20) int
    
    Arguments:
        int_list {[list of int]} -- [input list]
    
    Returns:
        [list of int] -- [outlier deleted list]
    """
    '''
    input.txt
6 14 9 2 25 1 15 7 13 11 7 16 26 19 12 15 14
    def deleteOutlier(int_list)
input : 인풋 숫자들의 리스트 (list)
output : 숫자들의 리스트 (list)
effect : 10-20 사이가 아닌 outlier를 제거하여 list를 return 한다.
'''
    for i in int_list:
        if i not in range(10,21):
            modified_list.append(i)
    return modified_list
