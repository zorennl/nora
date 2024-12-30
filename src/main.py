from pyray import *

class Window2D:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        init_window(width, height, title)

        
    def draw(self, fps, bkg, rect, size, color):
        self.fps = int
        self.bkg = Color
        self.rect = Vector2
        self.size = Vector2
        self.color = Color

        set_target_fps(fps)
        
        while not window_should_close():

            begin_drawing()

            clear_background(bkg)

            draw_rectangle_v(rect, size, color)
            
            end_drawing()

        close_window()

player = Vector2(0, 0)

window = Window2D(800,500,"nora").draw(60, RED, player, Vector2(10,10), WHITE)
