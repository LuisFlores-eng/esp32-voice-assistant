from machine import Pin
import time

#-----Secuencia de leds-----
#heartbeat_led=Pin(2, Pin.OUT)
pines=[13, 12, 14]
leds=[Pin(p, Pin.OUT) for p in pines ]
i_if=Pin(23, Pin.IN)

try:
     while True:

          if i_if.value()==0 :
     
               #Avanzar de izquierda a derecha
               for led in leds:
                    led.value(1)
                    time.sleep(0.5)
                    led.value(0)

               #Avanzar de derecha a izquierda
               for led in reversed(leds):
                    led.value(1)
                    time.sleep(0.5)
                    led.value(0)

except KeyboardInterrupt:   
     print("\nPrueba finalizada por el usuario")
     for led in leds:
          led.value(0)
     