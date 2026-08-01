from machine import Pin
import time

#configuracion de hardware
led=Pin(2, Pin.OUT)
btn=Pin(15, Pin.IN)
last_time=0

# Funcion de respuesta (callback)
def toggle_led(pin):
    #global last_time
    #current_time=time.ticks_ms()

    #Filtro antirrebote
    #if time.ticks_diff(current_time, last_time)>200:
        led.value(not led.value())
       # last_time=current_time

btn.irq(trigger=Pin.IRQ_RISING, handler=toggle_led)

# bucle principal
print("Esperando pulsaciones.....")
i=0
while True:
    #Prueba para verificar que el bucle sigue ejecutandose
    i+=2
    print("Inizio",i)
    time.sleep(1)

