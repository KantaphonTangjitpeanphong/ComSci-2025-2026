ctr = 0
d = 0 
while True:
    mark = int(input())
    if mark == -1:
        award = d/ctr 
        if award > 0.5:
            print("highly commended")
            break
        else:
            break 
    else:
        ctr = ctr+1 
        if mark >= 80:
            d = d+ 1
            
       
    