 if __name__ == '__main__':
    s = raw_input()
    print(any(str.isalnum()for str in s))
    print(any(str.isalpha()for str in s))
    print(any(str.isdigit()for str in s))
    print(any(str.islower()for str in s))
    print(any(str.isupper()for str in s))
