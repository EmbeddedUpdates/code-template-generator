
# import cog
from common_types import fileMetaData, function, parameter

# print("start")
myFunc = function()
myFunc.name = "pubFunc"
myFunc.brief = "I have changed the description"
myFuncParam0 = parameter()
myFuncParam0.ptype = "int"
myFuncParam0.name = "pubparam0"
myFuncParam0.brief = "This is a small description about the parameter itself"
myFunc.parameters.append(myFuncParam0)

privFunc = function()
privFunc.name = "privFunc"
privFunc.brief = "this is a private function that is static"
privFunc.longDescription = "This is an example for a long description in the private or local functions. You don't need to add \\n characters or anything like that and it will generate in the source code with them automatically added."
privFuncParam0 = parameter()
privFuncParam0.ptype = "void"
privFuncParam0.name = ""
privFuncParam0.brief = "void"
privFunc.parameters.append(privFuncParam0)

fileData = fileMetaData()
fileData.moduleName = "Timer_RP2040"
fileData.author = "Madrick3"
fileData.brief = "I changed the file brief"
fileData.publicFunctions.append(myFunc)
fileData.privateFunctions.append(privFunc)

fileData.includeList.append("Platform_Types.h")
fileData.includeList.append("Timer_RP2040_SFR.h")




