N = int(input())
def check(w):
    start = 0
    end = len(w) - 1
    if w==w[::-1]:
        return(0)
    else:
        while start < end:
            if w[start] == w[end]: 
                start += 1
                end -= 1
            else:#서로 다른경우 
                if start+1 < end:
                    text = w[:start] + w[start+1:]
                    if text==text[::-1]:
                        return(1)
                if start < end + 1:
                    text = w[:end] + w[end+1:]
                    if text==text[::-1]:
                        return(1)
                return(2)

for i in range(N):
    word = input()
    print(check(word))