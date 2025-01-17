# Output Statement: The print() method in python is used to display output on standard output on output devices.
# Syntax: 
# print(value(s),sep='',end='\n', file=file, flush=flush)
# Parameters:
# 1. value(s): Any value, and as many as we like will be converted to string before printed.
# 2. sep='seprator': (Optional) Specify how to separate the objects, if there is more that one Default:''
# 3. end='end': (Optional) Specify what to print at the end Default: '\n'
# 4. file: (Optional) An object with a white method Default:sys:stdout
# 5. flush: (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default : False.
print("Hello Python")
print('P','Y','T','H','O','N')
print("Python",end="###\n")
print('P','Y','T','H','O','N',sep="*")