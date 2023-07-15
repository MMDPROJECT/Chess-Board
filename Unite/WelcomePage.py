import flet as ft
import time
import math

class NewGame(ft.UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content = ft.Text(self.btnName, size=13, weight="bold"),
                style=ft.ButtonStyle(
                    shape={
                        "":ft.RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320  
            )
        )

               
class LoadGame(ft.UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(self.btnName, size=13, weight="bold"),
                style=ft.ButtonStyle(
                    shape={
                        "":ft.RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320
            )
        )
        
class ScoreBoard(ft.UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content = ft.Text(self.btnName, size=13, weight="bold"),
                style=ft.ButtonStyle(
                    shape={
                        "":ft.RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "" : "white",
                    },
                    bgcolor={"":"#181818"},
                ),
                height=42,
                width=320
            )
        )
        
class Exit(ft.UserControl):
    
    def __init__(self ,btnName):
        super().__init__()
        self.btnName = btnName
        
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content = ft.Text(self.btnName, size=13, weight="bold"),
                style=ft.ButtonStyle(
                    shape={
                        "":ft.RoundedRectangleBorder(radius=8),
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
    
        
class Animated(ft.UserControl):
    
    
    def __init__ (self , border_color , bg_color , rotate_angle):  #early after you run this class it comes here first
        
        super().__init__()
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        
    def build(self):
        
        return ft.Container(
            width=40,
            height=40,
            border=ft.border.all(2.5,self.border_color),
            bgcolor=self.bg_color, #short form of background color
            border_radius=2,
            rotate=ft.transform.Rotate(self.rotate_angle,ft.alignment.center),
            animate_rotation=ft.animation.Animation(700,"caseInOut"),
        )
        
      
def main(page: ft.Page):
       
    #Design the mainPage
    page.title = "WelcomePage"
    page.horizontal_alignment = "center"
    page.veritical_alignment = "center" 
    page.bgcolor = "#181818"
    
    #Go to other pages
    def route_change(route):
     page.HandlerPages.clear()
     page.HandlerPages.append(
         handler(page)[page.route] #functionality like dictionary
    
     )
     page.on_route_change = route_change
     page.go('/')
    
    def animate():
        clock_wise_rotate = math.pi/4
        counter_clock_wise_rotate =  - math.pi/2
        
        box1 = page.controls[0].content.content.controls[1].controls[0].controls[0]
        box2 = page.controls[0].content.content.controls[1].controls[1].controls[0]
        
        counter = 0
        color_index = 0
        while True:
    
            if counter >= 0 and counter <= 4:
                
                box1.rotate = ft.transform.Rotate(
                    counter_clock_wise_rotate , ft.alignment.center
                )
                box2.rotate = ft.transform.Rotate(
                    clock_wise_rotate , ft.alignment.center
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
                 
                 box1.rotate = ft.transform.Rotate(
                    counter_clock_wise_rotate , ft.alignment.center
                 )
                 box2.rotate = ft.transform.Rotate(
                    clock_wise_rotate , ft.alignment.center
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
        ft.Card(
            width=650,
            height=560,
            elevation=15,
            #make each ui
            content=ft.Container(
                
                bgcolor="#181818",
                border_radius=10, # NOTE : it should be int not string
                
                content=ft.Column(
                    
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        #main controller
                        ft.Divider(height=40,color="transparent"),
                        ft.Stack(
                            controls = [
                                #it is the animation part
                                Animated("#FFFFFF",None,0),
                                Animated("#FFFFFF",None,math.pi/4),
                            ],
                            ),
                        ft.Divider(height=20,color="transparent"),
                        #Let's introduce the menu
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                ft.Text("♜ CHESS GAME ♖", size = 22,weight="bold"),  
                            ]
                        ),
                        ft.Divider(height=20,color="transparent"),
                        NewGame("New Game"),
                        LoadGame("Load Game"),
                        ScoreBoard("Score Board"),
                        Exit("Exit"),
                    ],
                ),
            ),
        ),
    )
    animate()

ft.app(target=main) #create page