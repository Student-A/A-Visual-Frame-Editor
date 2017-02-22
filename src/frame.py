import standard

class Bdy:
    def __init__(self, line ):
        self._x=eval(standard.getArg(frame_line, "x=", "-+/*()"))
        self._y=eval(standard.getArg(frame_line, "y=", "-+/*()"))
        if frame_line.find("z=")!=-1:
            self._z=eval(standard.getArg(frame_line, "z=", "-+/*()"))
        else:
            self._z=-6
        self._w=eval(standard.getArg(frame_line, "w=", "-+/*()"))
        self._h=eval(standard.getArg(frame_line, "h=", "-+/*()"))
        if frame_line.find("d=")!=-1:
            self._d=eval(standard.getArg(frame_line, "d=", "-+/*()"))
        else:
            self._d=12


class Rect:
    def __init__( self, line ):
        self._x=eval(standard.getArg(frame_line, "x=", "-+/*()"))
        self._y=eval(standard.getArg(frame_line, "y=", "-+/*()"))
        if frame_line.find("z=")!=-1:
            self._z=eval(standard.getArg(frame_line, "z=", "-+/*()"))
        else:
            self._z=-6
        self._w=eval(standard.getArg(frame_line, "w=", "-+/*()"))
        self._h=eval(standard.getArg(frame_line, "h=", "-+/*()"))
        if frame_line.find("d=")!=-1:
            self._d=eval(standard.getArg(frame_line, "d=", "-+/*()"))
        else:
            self._d=12        

class Frame:
    def __init__( self, frame_id, frame_line ):
        self._bdys=[]
        self._rects=[]
        while frame_line.find("set_bdy[")!=-1:
            self._bdys.append(Bdy(frame_line[frame_line.find("set_bdy[")+8:frame_line.find("]",frame_line.find("set_bdy["))]))
            frame_line=frame_line[0:frame_line.find("set_bdy[")]+frame_line[frame_line.find("]",frame_line.find("set_bdy["))+1:len(frame_line)]
        while frame_line.find("set_rect[")!=-1:
            self._rects.append(Rect(frame_line[frame_line.find("set_rect[")+9:frame_line.find("]",frame_line.find("set_rect["))]))
            frame_line=frame_line[0:frame_line.find("set_rect[")]+frame_line[frame_line.find("]",frame_line.find("set_rect["))+1:len(frame_line)]

        self._id= frame_id
        self._img= eval(standard.getArg(frame_line, "img=", "-+/*()"))
        self._delay= eval(standard.getArg(frame_line, "delay=", "-+/*()"))
        temp= standard.getArg(frame_line, "center=", "-+/*(),").split(",")
        self._center=(eval(temp[0]), eval(temp[1]))
        if frame_line.find("goto=")!=-1:
            self._goto= eval(standard.getArg(frame_line, "goto=", "-+/*()"))
        else:
            self._goto= frame_id+1

        
        
def SplitSequences( lines ):
    new_frames=""
    while lines.find("[s=")!=-1:
        sequence=lines[lines.find("]", lines.find("[s="))+1:lines.find("[/s]")]
        img=eval(standard.getArg(sequence, "img=", "-+/*()"))
        goto=eval(standard.getArg(sequence, "goto=", "-+/*()"))
        sequence=sequence.replace("img="+standard.getArg(sequence,"img=","+-/*() "), "%img%",1)
        sequence=sequence.replace("goto="+standard.getArg(sequence,"goto=","+-/*() "), "%goto%",1)
        init_frame, final_frame = standard.getArg(lines, "[s=", "->").split("->")
        for frame_id in range(int(init_frame), int(final_frame)+1):
            new_frames+="[f="+str(frame_id)+"]%seq%"+sequence.replace("%img%","img="+str(img)).replace("%goto%","goto="+str([goto,]))
