from machine import Pin,I2C
import ssd1306
from time import sleep_ms,sleep
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
    
def cow():
    display.text("      \__/", 0, 0)
    display.text("  ____(..)", 0, 6)
    display.text("/(   /(__)", 0, 12)
    display.text(" | w-||", 0, 18)
    display.text(" ||  ||", 0, 24)
    display.text("z Z", 90, 5)

def cow2():
    display.text("      \__/", 0, 0)
    display.text("  ____(..)", 0, 6)
    display.text("-(   /(__)", 0, 12)
    display.text(" | w-||", 0, 18)
    display.text(" ||  ||", 0, 24)
    display.text(".. .", 90, 5)

while True:
    display.fill(0)
    cow()
    display.show()
    sleep(1)
    display.fill(0)
    cow2()
    display.show()
    sleep(1)
    

