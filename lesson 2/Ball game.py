import pgzrun
from random import randint

TITLE="BOUNCING BALL"
WIDTH=800
HEIGHT=600

R=randint(0,255)
G=randint(0,255)
B=randint(0,255)

CLR = R,G,B
GRAVITY=2000.0

class Ball:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

class bal:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball=Ball(50, 100)
balll=bal(30, 20)
def draw():
    screen.clear()
    ball.draw()
    balll.draw()

def update(dt):
    #apply the acceleration formulae
    uy = ball.vy
    ball .vy += GRAVITY * dt
    ball.y += (uy + ball.vy )* 0.5 * dt

    if ball.y > HEIGHT - ball.radius : #we have bounced
        ball.y = HEIGHT - ball.radius #fix the position of the ball
        ball.vy = - ball.vy * 0.9 #inelastic collision

    ball.x += ball.vx * dt
    if ball.x > WIDTH-ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

     #apply the acceleration formulae
    uy = balll.vy
    balll .vy += GRAVITY * dt
    balll.y += (uy + balll.vy )* 0.5 * dt

    if balll.y > HEIGHT - balll.radius : #we have bounced
        balll.y = HEIGHT - balll.radius #fix the position of the ball
        balll.vy = - balll.vy * 0.9 #inelastic collision

    balll.x += balll.vx * dt
    if balll.x > WIDTH-balll.radius or balll.x < balll.radius:
        balll.vx = -balll.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -200


    #apply the acceleration formulae
    uy = balll.vy
    balll .vy += GRAVITY * dt
    balll.y += (uy + balll.vy )* 0.5 * dt

    if balll.y > HEIGHT - balll.radius : #we have bounced
        balll.y = HEIGHT - balll.radius #fix the position of the ball
        balll.vy = - balll.vy * 0.9 #inelastic collision

    balll.x += balll.vx * dt
    if balll.x > WIDTH-balll.radius or balll.x < balll.radius:
        balll.vx = -balll.vx


def on_key_down(key):
    if key == keys.SPACE:
        balll.vy = -200

pgzrun.go()
