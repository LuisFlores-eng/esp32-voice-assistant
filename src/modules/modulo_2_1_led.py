from machine import Pin
import time

# ============================================================================
# CONFIGURACIÓN DE PINES Y PERIFÉRICOS
# ============================================================================
pines = [13, 12, 14]          # GPIOs asignados a los LEDs: Verde (13), Amarillo (12), Rojo (14)
leds = [Pin(p, Pin.OUT) for p in pines]

i_SensorIF1 = Pin(22, Pin.IN)  # Sensor de entrada: Detecta presencia del peatón al iniciar el cruce
i_SensorIF2 = Pin(23, Pin.IN)  # Sensor de salida: Detecta cuando el peatón completa el cruce
o_buzzer = Pin(15, Pin.OUT)    # Actuador sonoro: Emite alertas por permanencia o infracción


# ============================================================================
# FUNCIONES AUXILIARES DE CONTROL
# ============================================================================
def alerta_buzzer(estado):
    """Activa (1) o desactiva (0) la señal del buzzer de advertencia."""
    o_buzzer.value(estado)

def off_all():
    """Apaga todos los LEDs y la alerta sonora para dejar la placa en estado seguro."""
    for led in leds:
        led.value(0)
    alerta_buzzer(0)


# ============================================================================
# BUCLE PRINCIPAL (SECUENCIA DE SEMÁFORO INTELIGENTE)
# ============================================================================
try:
    while True:

        # --------------------------------------------------------------------
        # 1. ESTADO LUZ VERDE (Paso libre - 3 segundos)
        # --------------------------------------------------------------------
        leds[0].value(1)

        inicio = time.ticks_ms()
        peaton_via = False

        # Muestreo no bloqueante del sensor 1 durante 3000 ms
        while time.ticks_diff(time.ticks_ms(), inicio) < 3000:
            if i_SensorIF1.value() == 0:  # Lectura Active-LOW del sensor IR
                peaton_via = True

        leds[0].value(0)

        # --------------------------------------------------------------------
        # 2. TRANSICIÓN A AMARILLO (Parpadeo de aviso - 3 ciclos)
        # --------------------------------------------------------------------
        for _ in range(3):
            # Fase encendido (100 ms)
            inicio = time.ticks_ms()
            leds[0].value(1)
            while time.ticks_diff(time.ticks_ms(), inicio) < 100:
                if i_SensorIF1.value() == 0:
                    peaton_via = True

            # Fase apagado (100 ms)
            inicio = time.ticks_ms()
            leds[0].value(0)
            while time.ticks_diff(time.ticks_ms(), inicio) < 100:
                if i_SensorIF1.value() == 0:
                    peaton_via = True

        # --------------------------------------------------------------------
        # 3. BUCLE DE EMERGENCIA (Retención por peatón en vía)
        # Se ejecuta solo si el peatón ingresó y aún no llega al Sensor 2.
        # --------------------------------------------------------------------
        while peaton_via:
            # Fase encendido con buzzer activo (100 ms)
            leds[0].value(1)
            inicio = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), inicio) < 100:
                if i_SensorIF2.value() == 0:
                    peaton_via = False  # El peatón salió; rompe la condición del while
                    break
                alerta_buzzer(1)

            # Fase apagado con buzzer activo (100 ms)
            inicio = time.ticks_ms()
            leds[0].value(0)
            while time.ticks_diff(time.ticks_ms(), inicio) < 100:
                if i_SensorIF2.value() == 0:
                    peaton_via = False  # El peatón salió; rompe la condición del while
                    break
                alerta_buzzer(1)

        # --------------------------------------------------------------------
        # 4. ESTADO LUZ AMARILLA (Precaución - 1 segundo)
        # Activa buzzer inmediatamente si un peatón ingresa de forma indebida.
        # --------------------------------------------------------------------
        leds[1].value(1)
        inicio = time.ticks_ms()

        while time.ticks_diff(time.ticks_ms(), inicio) < 1000:
            if i_SensorIF1.value() == 0:
                alerta_buzzer(1)
            else:
                alerta_buzzer(0)

        leds[1].value(0)

        # --------------------------------------------------------------------
        # 5. ESTADO LUZ ROJA (Detención vehicular / Alto peatonal - 3 segundos)
        # Detecta cruces indebidos y emite alarma sonora.
        # --------------------------------------------------------------------
        leds[2].value(1)
        inicio = time.ticks_ms()

        while time.ticks_diff(time.ticks_ms(), inicio) < 3000:
            if i_SensorIF1.value() == 0:
                alerta_buzzer(1)
            else:
                alerta_buzzer(0)

        leds[2].value(0)

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
    off_all()