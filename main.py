class Uhelang():
    def __init__(self):
        self.var = [0]*256
        self.line_index = 0
        self.output = ""

    def get_cmd(self,code):
        if "으" in code and "헤" in code:
            return "var", "으헤"
        if "으헿" in code:
            return "if", "으헿"
        if "으헷" in code:
            return "unless", "으헷"
        if "아쯔이" in code:
            return "print", "아쯔이"
        if "유메" in code:
            return "printascii", "유메"
        
        return None, None
    def operation(self,numbcode:str):

        multiply_split = numbcode.split("?")
        number = 1
        for x in multiply_split:
            plus = x.count("~")
            minus = x.count(".")
            varplus=0
            inputvar=0
            getvarindex=0
            if "이야" in x:
                getvarindex = x.count("아")
                varplus=self.var[getvarindex]
            
            if "히요리" in x:
                inputvar = int(input())
                
            number *= plus - minus + varplus + inputvar
            
        return number
            
    def line_compile(self,codeline:str):
        #print(self.line_index, "컴파일 중... ", codeline, "메모리:",self.var)
        cmd, cmdname = self.get_cmd(codeline)
        if (cmd == None or cmdname == None):
            return
        codeline=codeline.replace(cmdname,'')
        parameter = self.operation(codeline)
        if cmd == "var":
            self.var[codeline.count("에")] = parameter
        elif cmd == "if":
            parameter_split = codeline.split(",")
            p1 = self.operation(parameter_split[0])
            p2 = self.operation(parameter_split[1])
            
            if (p1 == 0):
                self.line_index = p2-2
        elif cmd == "unless":
            parameter_split = codeline.split(",")
            p1 = self.operation(parameter_split[0])
            p2 = self.operation(parameter_split[1])
            if (p1 != 0):
                self.line_index = p2-2
        elif cmd == "print":
            self.output += f"{parameter}"
        elif cmd == "printascii":
            self.output += chr(parameter)
            
    def compile(self,code:list):
        print("입력:")
        while (self.line_index < len(code)):
            self.line_compile(code[self.line_index])
            
            if (self.line_index <= -1):
                break
            
            self.line_index+=1
        
        print("출력:")
        print(self.output)


compiler = Uhelang()

with open('difference.uhe', 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()
    compiler.compile(lines)
