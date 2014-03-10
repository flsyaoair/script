import sys
def exitFunc(value):
        '''Clear function'''
        print value
        sys.exit()

#print "hello"

try:
        sys.exit(2)
except SystemExit,value:
        exitFunc(value)
#print "Ok"