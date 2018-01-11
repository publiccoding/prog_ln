import optparse

#usage = 'usage: %prog'
options=optparse.OptionParser('[-a], [-s],[-m],[-d]')
options.add_option('-a',action='store_true',dest='add',default=False,help='Addition the two given value')
options.add_option('-s',action='store_true',dest='sub',default=False,help='subtract the two given value')
options.add_option('-m',action='store_true',dest='mul',default=False,help='Multiply the two given value')
options.add_option('-d',action='store_true',dest='div',default=False,help='Divide the two given value')
(option,args)=options.parse_args()
print(option.add)
if option.add:
    print('add value',args,)
elif option.sub:
    print("subtract value")