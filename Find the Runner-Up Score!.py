n = int(input())
for i in range(n):
    arr =list(map(int, input().split(" ")))
if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar - 2])
k = max(arr)
    for i in range(0,n):
        if max(arr) == k:
            arr.remove(max(arr))
arr.sort(reverse=True)
print(arr[0])
