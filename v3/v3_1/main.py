import sys
import  os

#父路径
str1 = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
#再次取父路径
str1 = os.path.abspath(os.path.join(str1, os.pardir))
sys.path.append(str1+"\\gg")

import newmodule


newmodule.newPrint('kkkk')

