
# import cog
from common_types import fileMetaData, function, parameter


# print("start")
pubFunc = function()
pubFunc.setFuncName("pubFunc")
pubFunc.setBrief("I have changed the brief for the public function")
pubFuncParam0 = parameter()
pubFuncParam0.setType("uint32")
pubFuncParam0.setName("count")
pubFuncParam0.setBrief("This public func is important and has been set as so")
pubFunc.addParameter(pubFuncParam0)

privFunc = function()
privFunc.setFuncName("privFunc")
privFunc.setReturnType("void")
privFunc.setBrief("This is a private function that is static")
privFunc.setDescription("This is an example of a long description in  a private function that we want to  make sure to keep informative. There is no need to add a newLine character for this, and we will take care of it in the generator tool. Later, we can just have this as a part of a CSV or .txt file or something")
# no parameter is given to the private func, so that later we can create a privFunc that has void params

fileData = fileMetaData()
fileData.setModuleName("Timer_RP2040")
fileData.setAuthor("Madrick3")
fileData.setBrief("I changed the file brief")
fileData.addPublicFunctions(pubFunc)
fileData.addPrivateFunctions(privFunc)

fileData.includeList.append("Platform_Types.h")
fileData.includeList.append("Timer_RP2040_SFR.h")




