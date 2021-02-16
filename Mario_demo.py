from machine import Pin,I2C
import ssd1306
from time import sleep_ms,sleep
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

hero_char = "."
speed = 2 
x=-20
y=16
player_x=10
player_y=25

bg_x=120
status="begin"

first_coin_y=10
first_coin_char = "?"

mg_y=8
first_mg_char = "?"

def player():
    display.text(hero_char,player_x, player_y)

   
def background():
    bg_y=15
    display.text("{0}  #{1}#?".format(first_coin_char,first_mg_char),bg_x, bg_y)
    display.text("          T          <",bg_x, bg_y+10)


def first_coin():
    global first_coin_y
    if status =="first_jump_down":
        #coin get
        first_coin_y-=1
        display.text("o",bg_x, first_coin_y)
    
def show_mg():
    global mg_y
    global hero_char
    if status =="herogo_and_mg_down":
        mg_y+=2
        if mg_y >= player_y:
           hero_char ="I"
    display.text("Y",player_x, mg_y)
    
t=0

def act():
    global bg_x
    global player_y
    global status
    global first_coin_char
    global first_mg_char
    if status =="begin":
        if bg_x>=10:
            bg_x-=speed
        if bg_x<=10:
            status = "first_jump_up"
    if status =="first_jump_up":
        player_y-=1
        if player_y<=15:
            status = "first_jump_down"
            first_coin_char = "?"
    if status =="first_jump_down":
        first_coin()
        player_y+=1
        if player_y>=25:
            status = "first_get_big"
            first_coin_char = "#"
    if status =="first_get_big":
        if bg_x>=-21:
            bg_x-=speed
        else:
            status = "first_get_big_up"
    if status =="first_get_big_up":
        player_y-=1
        if player_y<=15:
            status = "first_get_big_down"
            first_mg_char = "#"
    if status =="first_get_big_down":
        show_mg()
        player_y+=1
        if player_y>=25:
            status = "herogo"
    if status =="herogo":
        show_mg()
        if bg_x>=-45:
            bg_x-=speed
        else:
            status = "herogo_and_mg_down"
    if status =="herogo_and_mg_down":
        show_mg()
        if bg_x>=-60:
            bg_x-=speed
        else:
            status = "hero_jump_T_up"
    if status =="hero_jump_T_up":
        if bg_x>=-69:
            bg_x-=speed
            player_y-=3
        else:
           status = "hero_jump_T_down"
    if status =="hero_jump_T_down":
        player_y+=3
        bg_x-=speed
        if player_y>=25:
            player_y=25
            status = "herogogo"
    if status =="herogogo":
        if bg_x>=-152:
            bg_x-=speed*2
        else:
           status = "gameover"
    if status =="gameover":
        display.text("Game Over",30, 15)
    
    
while True:
    display.fill(0)
    act()
    background()
    player()
    sleep_ms(1)
    display.show()
    
