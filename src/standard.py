

def pointInRect( point, rect):
    return point[0] >= rect[0] and point[0] <= rect[0]+rect[2] and point[1] >= rect[1] and point[1] <= rect[1]+rect[3]

def getArg(frame, tag, exceptions):
    if exceptions==None:
        exceptionscase=False
    tagpos=frame.find(tag)+len(tag)
    temp=""
    for a in range(tagpos, len(frame)):
        if exceptions!=None:
            exceptionscase=frame[a] in exceptions
            
        if frame[a].isdigit() or exceptionscase:
            while True:
                if (not frame[a].isdigit() and exceptions==None) or (exceptions!=None and (not frame[a] in exceptions) and (not frame[a].isdigit())):
                    return temp
                temp+=frame[a]
                a+=1
                if a==len(frame):
                    return  temp

        if not frame[a].isspace():
            return '0'


