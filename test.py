import os
var='test'
os.environ['var']=var

os.system('set var=%var%')