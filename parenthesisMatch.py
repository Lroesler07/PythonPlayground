def ValidParenthesis(input):
    strOpen = 0
    #isValid = True
    if len(input) > 1: 
        for i in range(len(input)):
            if input[i] == "(":
                strOpen = strOpen + 1
            elif input[i] == ")":
                    if strOpen != 0:
                        strOpen = strOpen -1
            elif input[i] == ")":
                            if strOpen == 0:
                                return False
            else:
                return False
    return strOpen == 0

isvalid = ValidParenthesis("{{{}}")
print(isvalid)