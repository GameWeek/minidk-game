from machine import Pin,I2C
import ssd1306
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.text("      ^__^", 0, 0)
display.text("  ____(oo)", 0, 5)
display.text("/(   /(__)", 0, 10)
display.text(" | w-||", 0, 15)
display.text(" ||  ||", 0, 20)
display.show()
