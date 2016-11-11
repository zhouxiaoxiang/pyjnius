#!/usr/bin/python


from jnius import autoclass
obj = autoclass('com.leiyuntop.machine.ISCInfo')()
print(obj.toString())    
## 'com.leiyuntop.machine.ISCInfo@6d6f6e28'

