n = input()
b = list(input())
g = list(input())
cgr = 0
cgm = 0
ans = 0
for i in g:
    if i == 'r':
        cgr += 1
    if i == 'm':
        cgm += 1

while(len(b) > 0):
    # print(len(b))
    i = 0
    if b[i] == 'r':
        if cgr > 0:
            cgr -= 1
            b.pop(0)
        else:
            ans = len(b)
            break
    if b[i] == 'm':
        if cgm > 0:
            cgm -= 1
            b.pop(0)
        else:
            ans = len(b)
            break
    # print(len(b))
    #c += 1
# print(c)

print(ans)
