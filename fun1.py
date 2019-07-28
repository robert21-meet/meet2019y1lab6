def pluscalc(start,end,jumps=1):
    total=0
    for i in range(start,end+1,jumps):
        total=total+i
    print (total)
pluscalc(1,2)
pluscalc(1,100)
pluscalc(1000,5000)
pluscalc(333,777)
pluscalc(1,10,2)



        
