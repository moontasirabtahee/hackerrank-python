def count_substring(p, q):
    c =0
    for i in range(len(p)):
        if p[i]==q[0]:
            if p[i:i+len(q)]==q:
                c+=1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)