def capitalize(s):
    name = s.split(' ')
    return ' '.join((i.capitalize() for i in name))


if __name__ == '__main__':
    s = input()
    p = capitalize(s)
    print(p)
