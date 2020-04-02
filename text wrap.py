import textwrap

def wrap(c, i):
    x = textwrap.wrap(c,i)
    x="\n".join(x)
    return x

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)