import RPi.GPIO as GPIO
import time

LCD_RS = 26
LCD_E  = 24
LCD_D4 = 22
LCD_D5 = 18
LCD_D6 = 16
LCD_D7 = 12
LCD_WIDTH = 16  
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
E_PULSE = 0.0005
E_DELAY = 0.0005

def first(i,j):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)    
  GPIO.setup(LCD_E, GPIO.OUT)  
  GPIO.setup(LCD_RS, GPIO.OUT) 
  GPIO.setup(LCD_D4, GPIO.OUT) 
  GPIO.setup(LCD_D5, GPIO.OUT) 
  GPIO.setup(LCD_D6, GPIO.OUT) 
  GPIO.setup(LCD_D7, GPIO.OUT) 
  lcd_init()
  lcd_string(i,LCD_LINE_1)
  lcd_string(j,LCD_LINE_2)
  time.sleep(0.1)
  
def lcd_init():
  lcd_byte(0x33,LCD_CMD) 
  lcd_byte(0x32,LCD_CMD) 
  lcd_byte(0x06,LCD_CMD) 
  lcd_byte(0x0C,LCD_CMD) 
  lcd_byte(0x28,LCD_CMD) 
  lcd_byte(0x01,LCD_CMD) 
  time.sleep(E_DELAY)
  
def lcd_byte(bits, mode):
  GPIO.output(LCD_RS, mode)
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)  
  lcd_toggle_enable()
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
  lcd_toggle_enable()

def lcd_toggle_enable():
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

if __name__ == '__main__':
  try:
      first(i,j)
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Makerdemy!",LCD_LINE_1)
    GPIO.cleanup()

