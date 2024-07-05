
import datetime

class fileMetaData:
    moduleName = "moduleName"
    author = "Madrick3"
    date = datetime.date.today()
    brief = "This is a brief description about the module"
    functions = []

class function:
    brief = "This is a brief description about a function"
    parameters = []
    preCondition = "n/a"
    postCondition = "n/a"
    invariantCondition = "n/a"
    returnType = "int"
    name = "Function_Name"

    def toFuncPrototype(self):
        prototype = "%s %s (" % (self.returnType, self.name)
        for p in self.parameters:
            prototype += p.ptype + " " + p.name + " "
        prototype += ")"
        return prototype

    def toFuncComment(self):
        comment = "/**\n"
        comment += " * %s\n" % self.brief
        comment += " *\n"
        for p in self.parameters:
            comment += " * %s\n" % p.toParamComment()
        comment += " *\n"
        comment += " *@pre %s\n" % self.preCondition
        comment += " *@post %s\n" % self.postCondition
        comment += " *@invariant %s\n" % self.invariantCondition
        comment += " *\n"
        comment += " */\n"
        return comment

class parameter:
    ptype = "int"
    name = "param1"
    brief = "This is a brief description about the parameter"

    #forms and returns the string "@param 
    def toParamComment(self):
        return "@param %s: %s" % (self.name, self.brief)


        