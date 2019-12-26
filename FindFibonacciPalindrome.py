'''
分三步，1.切片
       2.筛选是否满足回文
       3.筛选是否满足斐波那契
'''

sequence = [1,2,3,4,1,2,3,5,8,8,5,3,2,1]

def list_generator(a):
    '''
    切片，返回由元素，元素起始索引下表，元素长度的元组组成的列表
    :param a: 输入列表
    :return: 由元素，元素起始索引下表，元素长度的元组组成的列表
    '''
    list_01 = []
    for i in range(len(a) - 2):
        for j in range(i + 3, len(a) + 1):
            list_02 = a[i:j]
            list_01.append((list_02,i,len(list_02)))
    return list_01

def Palindrome_filter(l):
    '''
    判断是否是回文
    :param l: 输入列表
    :return: 满足回文元素组成的列表
    '''
    list_03 = []
    for i in l:
        if i[0] == i[0][::-1]:
            list_03.append(i)
    return list_03

def fbnq_true(l):
    '''
    判断是否满足斐波那契
    :param l: 输入列表
    :return: 是或者否
    '''
    list_04 = []
    if len(l) % 2 == 0:
        list_04 = l[:len(l) // 2]
    elif len(l) % 2 == 1:
        list_04 = l[:len(l) // 2 + 1]

    for i in range(len(list_04)-2):
        if list_04[i] + list_04[i+1] == list_04[i+2]:
            continue
        else:
            return False
    return True

def FindFibonacciPalindrome(sequence):
    '''
    寻找列表中满足斐波那契回文的一个最大元素的起始索引和长度组成的元组
    :param sequence: 输入列表
    :return: 满足斐波那契回文的一个最大元素的起始索引和长度组成的元组
    '''
    list = list_generator(sequence)
    list_Palindrome = Palindrome_filter(list)
    list_tuple = []
    for i in list_Palindrome:
        if fbnq_true(i[0]):
            list_tuple.append(i)
    list_result = sorted(list_tuple, key=lambda x: x[2], reverse=True)
    return list_result[0][1:]

if __name__ == '__main__':
    result = FindFibonacciPalindrome(sequence)
    print('斐波那契回文的一个最大元素的起始索引下标%2d,长度%2d'
          %(result[0],result[1]))