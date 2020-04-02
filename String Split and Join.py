
def split_and_join(line):
    N = line
    N = N.split()
    N = "-".join(N)
    return N
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)