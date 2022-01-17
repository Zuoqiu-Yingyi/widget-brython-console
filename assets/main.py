from interpreter import Interpreter
from browser import bind, document

# 在 id 为 "code" 文本区中启动一个交互式控制台
# Start an interactive interpreter in textarea with id "code"
Interpreter("code")

COLOR_DARK = "#CCC"
BACKGROUND_COLOR_DARK = "#1F1F1F"

COLOR_DEFAULT = "var(--b3-theme-on-background)"
BACKGROUND_COLOR_DEFAULT = "transparent"


@bind("#switch-theme", "click")
def colorChange(event):
    def setColor(color, backgroundColor, elements):
        """ 设置控制台的颜色(Set the color of the console) """
        for element in elements:
            element.style.color = color
            element.style.backgroundColor = backgroundColor

    if document["switch-theme-input"].checked:  # 跟随主题(Follow the theme)
        setColor(
            color=COLOR_DEFAULT,
            backgroundColor=BACKGROUND_COLOR_DEFAULT,
            elements=document.select('.codearea'),
        )
    else:  # 变更为深色主题(change to dark theme)
        setColor(
            color=COLOR_DARK,
            backgroundColor=BACKGROUND_COLOR_DARK,
            elements=document.select('.codearea'),
        )


class ElementMove:
    """ 鼠标移动元素(Mouse moves element) """

    def __init__(self, moving):
        """Make "moving" element movable with the mouse"""
        self.moving = moving
        self.is_moving = False
        self.moving.bind("mousedown", self.start)
        self.moving.bind("mouseup", self.stop)
        moving.style.cursor = "move"

    def start(self, event):
        """When user clicks on the moving element, set boolean is_moving
        to True and store mouse and moving element positions"""
        self.is_moving = True
        self.mouse_pos = [event.x, event.y]
        self.elt_pos = [self.moving.left, self.moving.top]
        document.bind("mousemove", self.move)
        # prevent default behaviour to avoid selecting the moving element
        event.preventDefault()

    def move(self, event):
        """User moves the mouse"""
        if not self.is_moving:
            return

        # set new moving element coordinates
        self.moving.left = self.elt_pos[0] + event.x - self.mouse_pos[0]
        self.moving.top = self.elt_pos[1] + event.y - self.mouse_pos[1]

    def stop(self, event):
        """When user releases the mouse button, stop moving the element"""
        self.is_moving = False
        document.unbind("mousemove")


ElementMove(document["tool-box"])
