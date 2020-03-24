def Kendalls(l1,l2):
    s = p
    ascii_limit = 97
    char_to_index = {char:ord(char)-97 for char in s}
    print(char_to_index)
    mat = {}
    for char in s:
        sub_list = []
        for i in range(len(s)):
            sub_list.append(0)
        mat[char] = sub_list
    print(mat)
    for index, char in enumerate(s):
        for after_char in s[index+1:]:
            mat[char][char_to_index[after_char]] = 1
    print(mat)
    output = [[0 for i in range(len(s))] for j in range(len(s))]
    print(output)
    for char, sub_lists in mat.items():
        output[char_to_index[char]] = mat[char]
    print(output)
    return l1,l2

'''Input:
p = "cefdab"
q = "cfebad"
Kendalls(p,q)
'''
