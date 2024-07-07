
import datetime
# import math

class fileMetaData:
    def __init__(self, name="MODULE", author="AUTHOR"):
        self.moduleName = name
        self.author = author
        self.date = datetime.date.today()
        self.brief = "This is a brief description about the module"
        self.privateFunctions = []
        self.publicFunctions = []
        self.includeList = []
    
    def getModuleName(self):
        return self.moduleName
    
    def setModuleName(self, string):
        self.moduleName = string
    
    def getAuthor(self):
        return self.author
    
    def setAuthor(self, string):
        self.author = string
    
    def getCreationDate(self):
        return self.date
    
    def setCreationDate(self, date):
        self.date = date

    def setCreationDateToToday(self):
        self.date = datetime.date.today()

    def getBrief(self):
        return self.brief
    
    def setBrief(self, brief):
        self.brief = brief
    
    def getPrivateFunctions(self):
        return self.privateFunctions
    
    def clrPrivateFunctions(self):
        self.privateFunctions = []

    def setPrivateFunctions(self, privateFunctions):
        self.privateFunctions = privateFunctions
    
    def addPrivateFunctions(self, func):
        self.privateFunctions.append(func)
    
    def getPublicFunctions(self):
        return self.publicFunctions

    def clrPublicFunctions(self):
        self.publicFunctions = []

    def setPublicFunctions(self, publicFunctions):
        self.publicFunctions = publicFunctions
    
    def addPublicFunctions(self, func):
        self.publicFunctions.append(func)
    
    def getIncludeList(self):
        return self.includeList
class function:
    def __init__(self):
        self.longDescription = "This is a long description about the function, including  its general purpose and design intentions. This comment should be long and include a thorough description of the use case for the function, and also its potential change history. "
        self.brief = "This is a brief description about a function"
        self.parameters = []
        self.preCondition = "n/a"
        self.postCondition = "n/a"
        self.invariantCondition = "n/a"
        self.returnType = "int"
        self.name = "Function_Name"
        self.retDesc = "@return void"

    def getDescription(self):
        return self.longDescription
    
    def setDescription(self, desc):
        self.longDescription = desc

    def getBrief(self):
        return self.brief
    
    def setBrief(self, brief):
        self.brief = brief

    def getReturnDesc(self):
        return self.retDesc
    
    def setReturnDesc(self, desc):
        self.retDesc = desc
    
    def getParameters(self):
        return self.parameters
    
    def setParameters(self, params):
        self.parameters = params

    def addParameter(self, param):
        self.parameters.append(param)
    
    def getPreCondition(self):
        return self.preCondition
    
    def setPreCondition(self, pre):
        self.preCondition = pre
    
    def getPostCondition(self):
        return self.postCondition
    
    def setPostCondition(self, post):
        self.postCondition = post

    def getInvConditions(self):
        return self.invariantCondition
    
    def setInvCondition(self, inv):
        self.invariantCondition = inv
    
    def getReturnType(self):
        return self.returnType
    
    def setReturnType(self, ret):
        self.returnType = ret
    
    def getFuncName(self):
        return self.name
    
    def setFuncName(self, name):
        self.name = name

    '''
    formatStringFor120CharacterLimit()
        recursive function: step 0 - breakout condition is if string is less than 120 characters long
        now, the recursive stuff:
        first, we will need to create a small workspace, we can call this 'workspace' or 'tempString'
        the workspace isn't useful, but we will need to read through parts of the string and modify them.
        a recursive loop might work very well here actually:
            if(len(workspace) > 120):
                we need to break the string up
                start at index 120 in this string and iterate backwards for a delimiter
                for i in range (119, -1, -1):
                    if workspace[i] == " ":
                        break the string here with a newline, but we can't just modify the string here.
                        create a subWorkspace, that will remain untouched by this instance
                        subWorkspace = workspace[i:]
                        workspace[i] = "\n" #this is concerning cause it looks like two characters, not sure what it will be treated as by python
                        now we can clear the garbage afterwards, cause we dont care how the rest of it looks:
                        workspace[i+1:] = formatStringFor120CharacterLimit(subWorkspace)
    '''
    def formatStringFor120CharacterLimit(self, string):
        newString = ""
        # print(string)
        # print(len(string))
        # wait = input("this is a recursive loop, we can use this input to pause and see whats going wrong")
        #if the string is 120 characters or less, we should just put it in newString and return:
        if len(string) <= 120:
            workspace = string
        else:
            workspace = string
            for i in range( 116, -1, -1):
                if workspace[i] == " ":
                    subWorkspace = workspace[i:]
                    break
            workspace = workspace[:i] + "\n *" + self.formatStringFor120CharacterLimit(subWorkspace)
        newString = workspace
        # print("newstring: %s " % newString)
        return newString


    def toFuncPrototype(self):
        prototype = "%s %s (" % (self.returnType, self.name)
        if len(self.parameters) == 0:
            prototype += " void "
        else:
            params = self.parameters
            endIdx = len(params) - 1
            currIdx = 0
            while( currIdx < endIdx ):
                prototype += " " + params[currIdx].getType() + " " + params[currIdx].getName() + ","
                currIdx+=1
            prototype += " " + params[currIdx].getType() + " " + params[currIdx].getName() + " "
        prototype += ")"
        return prototype
    
    def toBigFuncComment(self):
        comment = "/**\n"
        comment += " * %s\n" % self.formatStringFor120CharacterLimit(self.longDescription)
        for p in self.parameters:
            comment += " * %s\n" % p.toParamComment()
        comment += " *\n"
        comment += "%s\n" % self.retDesc
        comment += " *\n"
        comment += " * @pre %s\n" % self.preCondition
        comment += " * @post %s\n" % self.postCondition
        comment += " * @invariant %s\n" % self.invariantCondition
        comment += " *\n"
        comment += " */"
        return comment

    def toFuncComment(self):
        comment = "/**\n"
        comment += " * %s\n" % self.brief
        for p in self.parameters:
            comment += " * %s\n" % p.toParamComment()
        comment += " *\n"
        comment += "%s\n" % self.retDesc
        comment += " *\n"
        comment += " * @pre %s\n" % self.preCondition
        comment += " * @post %s\n" % self.postCondition
        comment += " * @invariant %s\n" % self.invariantCondition
        comment += " *\n"
        comment += " */"
        return comment

class parameter:
    def __init__(self):
        self.pType = "TYPE"
        self.name = "PARAMNAME"
        self.brief = "THIS IS A BRIEF DESCRIPTION ABOUT THE PARAMETER"

    def setType(self, ptype):
        self.pType = ptype
    
    def getType(self):
        return self.pType
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getBrief(self):
        return self.brief
    
    def setBrief(self, brief):
        self.brief = brief

    #forms and returns the string "@param 
    def toParamComment(self):
        return "@param %s: %s" % (self.name, self.brief)


        