def mutate_string(string, position, character):
    s=position+1
    string=string[:position]+character+string[s:]
     
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
