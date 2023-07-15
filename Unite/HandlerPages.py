from flet import *
import NewGame
def handler(page):
    return{
        '/':View(
        route='/',
        controls=[
            NewGame.Newgame(page)
            ]
        ),
    }