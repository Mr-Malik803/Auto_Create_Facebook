import platform
arch=platform.architecture()[0]
if arch=="64bit":import Create
else:print('It is a 64bit compiled code. Not Supported on your device.')

