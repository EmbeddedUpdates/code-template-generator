
# import cog
from common_types import fileMetaData, function, parameter


# print("start")
pubFunc0 = function()
pubFunc0.setFuncName("pubFunc0")
pubFunc0.setBrief("I have changed the brief for the public function")
pubFunc0Param0 = parameter()
pubFunc0Param0.setType("uint32")
pubFunc0Param0.setName("count")
pubFunc0Param0.setBrief("This public func is important and has been set as so")
pubFunc0.addParameter(pubFunc0Param0)

pubFunc1 = function()
pubFunc1.setFuncName("pubFunc1")
pubFunc1.setBrief("I have changed the brief for the public function")
pubFunc1Param0 = parameter()
pubFunc1Param0.setType("uint32")
pubFunc1Param0.setName("count0")
pubFunc1Param0.setBrief("This param is the first param in the second function")
pubFunc1Param1 = parameter()
pubFunc1Param1.setType("uint32")
pubFunc1Param1.setName("count1")
pubFunc1Param1.setBrief("This is count1 for the second function")
pubFunc1.addParameter(pubFunc1Param0)
pubFunc1.addParameter(pubFunc1Param1)

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
fileData.addPublicFunctions(pubFunc0)
fileData.addPublicFunctions(pubFunc1)
fileData.addPrivateFunctions(privFunc)

fileData.includeList.append("Platform_Types.h")
fileData.includeList.append("Timer_RP2040_SFR.h")




