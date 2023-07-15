import flet as ft
import time
import math

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
        if page.route == "/":
            # Building root view (main menu)
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        # A card containing everything in menu
                        ft.Card(
                            width=650,
                            height=560,
                            elevation=15,
                            content=ft.Container(
                                bgcolor="#181818",
                                border_radius=10, # NOTE : it should be int not string
                                # A column to layout things in vertical manner
                                content=ft.Column(
                                    
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
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

                                        # New Game container
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content = ft.Text("New Game", size=13, weight="bold"),
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
                                                on_click=lambda _:page.go("/newgame")  
                                            )
                                        ),

                                        # Load Game container
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content=ft.Text("Load Game", size=13, weight="bold"),
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
                                                on_click=lambda _:page.go("/loadgame")
                                            )
                                        ),

                                        # Score Board container
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content = ft.Text("Score Board", size=13, weight="bold"),
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
                                                on_click=lambda _:page.go("/scoreboard")
                                            )
                                        ),

                                        # Exit Container
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content = ft.Text("Exit", size=13, weight="bold"),
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
                                                # on_click=#TODO exit every motha fucking window 
                                            )
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ]
                )
            )

        elif page.route == "/newgame":
            # Building new game view (chess-board and stuff)
            page.views.append(
                ft.View(
                    route="/newgame",
                    controls=[
                        # TODO instantiate an object of NewGame and start playing
                    ]
                )
            )
        

        elif page.route == "/loadgame":
            # Building load game view
            page.views.append(
                ft.View(
                    route="/loadgame",
                    controls=[
                        # TODO instantiate an object of LoadGame
                    ]
                )
            )
        
        elif page.route == "/scoreboard":
            # Building score board view
            page.views.append(
                ft.View(
                    route="/scoreboard",
                    controls=[
                        # TODO instantiate an object of ScoreBoard
                    ]
                )
            )

    def on_view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = on_view_pop
    page.go("/")
            
    # def animate():
    #     clock_wise_rotate = math.pi/4
    #     counter_clock_wise_rotate =  - math.pi/2
        
    #     box1 = page.controls[0].content.content.controls[1].controls[0].controls[0]
    #     box2 = page.controls[0].content.content.controls[1].controls[1].controls[0]
        
    #     counter = 0
    #     color_index = 0
    #     while True:
    
    #         if counter >= 0 and counter <= 4:
                
    #             box1.rotate = ft.transform.Rotate(
    #                 counter_clock_wise_rotate , ft.alignment.center
    #             )
    #             box2.rotate = ft.transform.Rotate(
    #                 clock_wise_rotate , ft.alignment.center
    #             )
                
    #             box1.update()
    #             box2.update()        
                
    #             clock_wise_rotate+= math.pi/2
    #             counter_clock_wise_rotate -= math.pi/2
                
    #             counter+=1
    #             time.sleep(0.7)
                
    #         if counter >= 5 and counter <=10:
                    
    #              clock_wise_rotate -= math.pi/2
    #              counter_clock_wise_rotate += math.pi/2
                 
    #              box1.rotate = ft.transform.Rotate(
    #                 counter_clock_wise_rotate , ft.alignment.center
    #              )
    #              box2.rotate = ft.transform.Rotate(
    #                 clock_wise_rotate , ft.alignment.center
    #              )
                 
    #              box1.update()
    #              box2.update()
                 
    #              counter+=1
    #              time.sleep(0.7)
                
    #         if counter > 10:
    #             counter = 0
                
    #color_index = (color_index + 1) % len(change_color)
    #box1.content.border.color = change_color[color_index]
                
    # Building controls
    # animate()

ft.app(target=main) #create page