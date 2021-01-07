temp = input('what is the temperature:')

ttype = input('f or c:')
if ttype == 'f':
    ftemp = int(temp) - 32
    stemp = int(ftemp) * 5
    ttemp = int(stemp) / 9
    print(ttemp)
if ttype == 'c':
    cftemp = int(temp) / 5
    cstemp = int(cftemp) * 9
    cttemp = int(cstemp) + 32
    print(cttemp)


input('press Enter to exit')