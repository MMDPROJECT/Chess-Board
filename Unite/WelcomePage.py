from flet import *
import flet
import time
import math

change_color = ["red","green","blue"] #rgb color cross of the square

class NewGame(UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return Container(
            content=ElevatedButton(
                content = Text(self.btnName,size =13,weight = "bold"),
                style=ButtonStyle(
                    shape={
                        "":RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320,
            )
        )
        
class LoadGame(UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return Container(
            content=ElevatedButton(
                content = Text(self.btnName,size =13,weight = "bold"),
                style=ButtonStyle(
                    shape={
                        "":RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320,
            )
        )
        
class ScoreBoard(UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return Container(
            content=ElevatedButton(
                content = Text(self.btnName,size =13,weight = "bold"),
                style=ButtonStyle(
                    shape={
                        "":RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320,
            )
        )
        
class Exit(UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return Container(
            content=ElevatedButton(
                content = Text(self.btnName,size =13,weight = "bold"),
                style=ButtonStyle(
                    shape={
                        "":RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320,
            )
        )
    
        
class Animated(UserControl):
    
    
    def __init__ (self , border_color , bg_color , rotate_angle):  #early after you run this class it comes here first
        
        super().__init__()
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        
    def build(self):
        
        return Container(
            width=40,
            height=40,
            border=border.all(2.5,self.border_color),
            bgcolor=self.bg_color, #short form of background color
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle,alignment.center),
            animate_rotation=animation.Animation(700,"caseInOut"),
        )
        
def main(page: Page):
       
    #Design the mainPage
    page.title = "WelcomePage"
    page.horizontal_alignment = "center"
    page.veritical_alignment = "center" 
    page.bgcolor = "#181818"
    
    def animate():
        clock_wise_rotate = math.pi/4
        counter_clock_wise_rotate =  - math.pi/2
        
        box1 = page.controls[0].content.content.controls[1].controls[0].controls[0]
        box2 = page.controls[0].content.content.controls[1].controls[1].controls[0]
        
        counter = 0
        color_index = 0
        while True:
    
            if counter >= 0 and counter <= 4:
                
                box1.rotate = transform.Rotate(
                    counter_clock_wise_rotate , alignment.center
                )
                box2.rotate = transform.Rotate(
                    clock_wise_rotate , alignment.center
                )
                
                box1.update()
                box2.update()        
                
                clock_wise_rotate+= math.pi/2
                counter_clock_wise_rotate -= math.pi/2
                
                counter+=1
                time.sleep(0.7)
                
            if counter >= 5 and counter <=10:
                    
                 clock_wise_rotate -= math.pi/2
                 counter_clock_wise_rotate += math.pi/2
                 
                 box1.rotate = transform.Rotate(
                    counter_clock_wise_rotate , alignment.center
                 )
                 box2.rotate = transform.Rotate(
                    clock_wise_rotate , alignment.center
                 )
                 
                 box1.update()
                 box2.update()
                 
                 counter+=1
                 time.sleep(0.7)
                
            if counter > 10:
                counter = 0
                
            #color_index = (color_index + 1) % len(change_color)
            #box1.content.border.color = change_color[color_index]
                
                    

    #Controller
    page.add(
        Card(
            width = 650,
            height = 560,
            elevation = 15,
            #make each ui
            content = Container(
                
                bgcolor = "#181818",
                border_radius = 10, # NOTE : it should be int not string
                
                content=Column(
                    
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        #main controller
                        Divider(height=40,color="transparent"),
                        Stack(
                            controls = [
                                #it is the animation part
                                Animated("#FFFFFF",None,0),
                                Animated("#FFFFFF",None,math.pi/4),
                            ],
                            ),
                        Divider(height=20,color="transparent"),
                        #Let's introduce the menu
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                Text("CHESS GAME TEAM", size = 22,weight="bold"),
                                
                            ]
                            
                        ),
                        Divider(height=20,color="transparent"),
                        NewGame("New Game"),
                        LoadGame("Load Game"),
                        ScoreBoard("Score Board"),
                        Exit("Exit"),
                        
                        
                    ],
                    
                ),
                
            ),
        ),
    )
    
    pass
    animate()

app(target=main) #create page