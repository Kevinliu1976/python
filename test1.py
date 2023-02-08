score=[33,73,63,39]


for y in score:
    for x in range(0,100,5):
        if x>y & x-y<3:
            newy=x
            if newy<40:
                print(y)
            else:
                print(newy)
            break
