
import datetime
import math

class fileMetaData:
    moduleName = "moduleName"
    author = "Madrick3"
    date = datetime.date.today()
    brief = "This is a brief description about the module"
    functions = []
    includeList = []

class function:
    longDescription = "This is a long description about the function, including  its general purpose and design intentions. This comment should be long and include a thorough description of the use case for the function, and also its potential change history. "
    brief = "This is a brief description about a function"
    parameters = []
    preCondition = "n/a"
    postCondition = "n/a"
    invariantCondition = "n/a"
    returnType = "int"
    name = "Function_Name"


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
            for i in range( 119, -1, -1):
                if workspace[i] == " ":
                    subWorkspace = workspace[i:]
                    break
            workspace = workspace[:i] + "\n *" + self.formatStringFor120CharacterLimit(subWorkspace)
        newString = workspace
        # print("newstring: %s " % newString)
        return newString


    def toFuncPrototype(self):
        prototype = "%s %s (" % (self.returnType, self.name)
        for p in self.parameters:
            prototype += p.ptype + " " + p.name + " "
        prototype += ")"
        return prototype
    
    def toBigFuncComment(self):
        comment = "/**\n"
        comment += " * %s\n" % self.formatStringFor120CharacterLimit(self.longDescription)
        comment += " *\n"
        for p in self.parameters:
            comment += " * %s\n" % p.toParamComment()
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
        comment += " *\n"
        for p in self.parameters:
            comment += " * %s\n" % p.toParamComment()
        comment += " *\n"
        comment += " * @pre %s\n" % self.preCondition
        comment += " * @post %s\n" % self.postCondition
        comment += " * @invariant %s\n" % self.invariantCondition
        comment += " *\n"
        comment += " */"
        return comment

class parameter:
    ptype = "int"
    name = "param1"
    brief = "This is a brief description about the parameter"

    #forms and returns the string "@param 
    def toParamComment(self):
        return "@param %s: %s" % (self.name, self.brief)


        