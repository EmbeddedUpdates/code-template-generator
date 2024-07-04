
# import cog
from common_types import fileMetaData, function, parameter

print("start")
myFunc = function()
myFunc.brief = "I have changed the description"
myFuncParam0 = parameter()
myFuncParam0.ptype = "int"
myFuncParam0.name = "param0"
myFuncParam0.brief = "This is a small description about the parameter itself"
myFunc.parameters.append(myFuncParam0)


fileData = fileMetaData()
fileData.author = "Patrick"
fileData.brief = "I changed the file brief"
fileData.functions.append(myFunc)





