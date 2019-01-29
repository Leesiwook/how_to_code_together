def remainOddOrEven(int_list):
    output = []
    if len(int_list)%2==0:
        for i in int_list:
            if i%2 ==0:
                output.append(i)
    else:
        for j in int_list:
            if i%2 ==1:
                output.append(j)
    return output