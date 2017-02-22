import pygame, sys
from pygame.locals import *
from grid import *
from buttons import *
import standard

class Application:
    def __init__(self,window_name ,window_width, window_height):
        self._a_files={}
        self._grid_lines=[]
        self._tag_mouse_rect={"id": None,"vertex": None, "origin": (None,None)}
        self._rects=[]
        self._bdys=[]
        self._canvas_width=700
        self._canvas_height=300
        self._canvas_x=50
        self._canvas_y=130
        pygame.init()
        self._window=pygame.display.set_mode((window_width, window_height),0,32)
        self._canvas=pygame.Surface((700,300), pygame.SRCALPHA, 32)
        self._canvas.fill((50, 50, 50, 255))
        pygame.display.set_caption(window_name)

        self._bdy_rect_toggle=RadioButton(8,(255,255,255), 2, 0, 18)
        self._font1=pygame.font.SysFont(None, 16, False, False)
        
    def updateWindow(self):
        pygame.draw.line(self._canvas, (200,200,200,255), (0,200), (800,200))
        pygame.draw.line(self._canvas, (200,200,200,255), (350,0), (350,600))
        self._window.blit(self._canvas, pygame.Rect(self._canvas_x,self._canvas_y,self._canvas_width,self._canvas_height))
        pygame.display.flip()
        self._window.fill((0,0,0))
        self._canvas.fill((50, 50, 50, 255))

    def canvasCoords( self, value, axis=None ):
        if axis == None:
            return(value[0]-self._canvas_x, value[1]-self._canvas_y)
        elif axis == 'x':
            return value - self._canvas_x
        elif axis == 'y':
            return value - self._canvas_y
        return



    def checkForEvents(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._bdy_rect_toggle.checkButtonClicked( event.pos )
                    if standard.pointInRect( event.pos, [self._canvas_x, self._canvas_y, self._canvas_width, self._canvas_height]):
                        if self._bdy_rect_toggle._current_choice==0:
                            self._tag_mouse_rect["id"]=self.addRect(event.pos[0], event.pos[1],1,1)
                        elif self._bdy_rect_toggle._current_choice==1:
                            self._tag_mouse_rect["id"]=self.addBdy(event.pos[0], event.pos[1],1,1)
                        self._tag_mouse_rect["vertex"]=2
                        self._tag_mouse_rect["origin"]=event.pos
    
            if event.type==MOUSEBUTTONUP:
                if event.button == 1:
                    self._tag_mouse_rect["id"]=None
                    self._tag_mouse_rect["vertex"]=None
                    self._tag_mouse_rect["origin"]=(None, None)
            if event.type==MOUSEMOTION:
                if self._tag_mouse_rect["id"]!=None:
                    if self._bdy_rect_toggle._current_choice==0:
                        if self._tag_mouse_rect["origin"][0] < event.pos[0]:
                            self._rects[self._tag_mouse_rect["id"]][2]= event.pos[0]-self._tag_mouse_rect["origin"][0]
                        elif self._tag_mouse_rect["origin"][0] > event.pos[0]:
                            self._rects[self._tag_mouse_rect["id"]][0]= event.pos[0]
                            self._rects[self._tag_mouse_rect["id"]][2]= self._tag_mouse_rect["origin"][0]-event.pos[0]

                        if self._tag_mouse_rect["origin"][1] < event.pos[1]:
                            self._rects[self._tag_mouse_rect["id"]][3]= event.pos[1]-self._tag_mouse_rect["origin"][1]
                        elif self._tag_mouse_rect["origin"][1] > event.pos[1]:
                            self._rects[self._tag_mouse_rect["id"]][1]= event.pos[1]
                            self._rects[self._tag_mouse_rect["id"]][3]= self._tag_mouse_rect["origin"][1]-event.pos[1]
                    elif self._bdy_rect_toggle._current_choice==1:
                        if self._tag_mouse_rect["origin"][0] < event.pos[0]:
                            self._bdys[self._tag_mouse_rect["id"]][2]= event.pos[0]-self._tag_mouse_rect["origin"][0]
                        elif self._tag_mouse_rect["origin"][0] > event.pos[0]:
                            self._bdys[self._tag_mouse_rect["id"]][0]= event.pos[0]
                            self._bdys[self._tag_mouse_rect["id"]][2]= self._tag_mouse_rect["origin"][0]-event.pos[0]

                        if self._tag_mouse_rect["origin"][1] < event.pos[1]:
                            self._bdys[self._tag_mouse_rect["id"]][3]= event.pos[1]-self._tag_mouse_rect["origin"][1]
                        elif self._tag_mouse_rect["origin"][1] > event.pos[1]:
                            self._bdys[self._tag_mouse_rect["id"]][1]= event.pos[1]
                            self._bdys[self._tag_mouse_rect["id"]][3]= self._tag_mouse_rect["origin"][1]-event.pos[1]



                        

                    
        return

    def loadLoadTxt(self, directory):
        with open(directory) as load_txt:
            loadtxt=load_txt.read().replace(" ","").replace(";",'').split("\n")
            a_files=loadtxt[loadtxt.index("{object}")+1:loadtxt.index("{/object}")]
            while True:
                try:
                    a_files.remove("")
                except ValueError:
                    break
            
            for line in a_files:
                self._a_files[line.split("::")[0]]=line.split("::")
        return

    def loadAFile(self, id_number):
        self._grid_lines=[]
        with open(self._a_files[str(id_number)][2]) as a_file:
            file_txt=a_file.read().replace(" ","").split("\n")
            img_txt=file_txt[file_txt.index("[img]")+1:file_txt.index("[/img]")]
            while True:
                try:
                    img_txt.remove("")
                except ValueError:
                    break
            for line in img_txt:
                self._grid_lines.append(line.split(','))
        return
                


    def loadGrid(self, grid_number):
        self._grid=Grid(self._grid_lines[grid_number][0],
                        int(self._grid_lines[grid_number][1]),
                        int(self._grid_lines[grid_number][2]),
                        int(self._grid_lines[grid_number][3]),
                        int(self._grid_lines[grid_number][4]),
                        self._grid_lines[grid_number][5])
        return
        
    def renderButtons(self):
        self._bdy_rect_toggle.renderButtons(self._window, 740, 469)

    def renderText(self):
        self.drawText("Drawing Option:", self._font1, 660, 445, (255,255,0))

        self.drawText("RECT", self._font1, 665, 465, (0,255,0))
        self.drawText("BDY", self._font1, 665, 465+18, (0,255,0))
        
    def update(self):
        return
    def drawLayout(self):
        rect = pygame.Surface((700,300), pygame.SRCALPHA, 32)
        rect.fill((50, 50, 50))
        screen.blit(rect, (100,100))
        pygame.draw.rect(self._window, (50,50,50),pygame.Rect(0,0,700,300))
    
    def drawText(self, text, font, x, y, color, bgcolor=None):
        if bgcolor==None:
            textobj = font.render(text, 1, color)
        else:
            textobj = font.render(text, 1, color, bgcolor)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._window.blit(textobj, textrect)
        
    def addRect(self, x, y, w, h):
        self._rects.append([x,y,w,h])
        return len(self._rects)-1

    def addBdy(self, x, y, w, h):
        self._bdys.append([x, y, w, h])
        return len(self._bdys)-1

    def renderSprite(self, sprite_number, x, y):
        self._grid.renderSprite(self._canvas,sprite_number,x,y) 
        
    def drawRects(self):
        for rect in self._rects:
            pygame.draw.rect(self._canvas, (255, 0, 0), pygame.Rect(self.canvasCoords(rect[0],'x'),self.canvasCoords(rect[1],'y'),rect[2],rect[3]), 3)

    def drawBdys(self):
        for bdy in self._bdys:
            pygame.draw.rect(self._canvas, (0, 0, 255), pygame.Rect(self.canvasCoords(bdy[0],'x'),self.canvasCoords(bdy[1],'y'),bdy[2],bdy[3]), 3)


MainApp=Application("A-Engine Utility: A-Visual Frame Editor" ,800, 600)
MainApp.loadLoadTxt("obj/load.txt")
MainApp.loadAFile(1)
MainApp.loadGrid(0)
while True:
    MainApp.checkForEvents()
    MainApp.renderSprite(33, 100, 100)
    MainApp.drawRects()
    MainApp.drawBdys()
    MainApp.renderText()
    MainApp.renderButtons()
    MainApp.updateWindow()
