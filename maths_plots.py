result=[]
for count in range (1,50):
    if count%3==0:
        result.append("fizz")
    else:
        result.append(count)
print(result)
