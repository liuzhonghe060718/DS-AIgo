import pygame.font
#font让pygame能将文本渲染到屏幕上
class Button():
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮属性"""
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #设置按钮的尺寸等
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        #name参数规定渲染的字体，size指定字号,font是一个字体工具，理解为画笔设置，render是画的操作
        self.font=pygame.font.SysFont(None,48)

        #创建按钮的rect对象，使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮的标签只需要创建一次
        self.prep_msg(msg)


    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        #font。render将文本转换为图像，然后储存在image中（还结束一个布尔实参，决定是否开启反锯齿功能，反锯齿让文本边缘更平滑，余下两个实参分别是文本色和背景色）,返回一个rect对象
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        #fill() 函数是 Pygame 中用于填充颜色的函数，通常作用于 Surface 对象，比如屏幕或图像。它的主要作用是给一个区域（通常是整个屏幕或图层）快速地涂上纯色背景，通常用于清屏或绘制背景。
        #Surface.fill(color, rect=None)
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)#指定位置绘制的函数





