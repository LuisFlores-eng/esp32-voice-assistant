# 📖 Bitácora de Ingeniería - ESP32 Voice Assistant

## 🗓️ 24 de Julio, 2026
* **Fase completada:** Fase 0 - Configuración de entorno y repositorio Git.
* **Actividades realizadas:**
  - Estructuración de carpetas profesionales en VS Code.
  - Sincronización remota con repositorio de GitHub.
  - Creación del archivo `.gitignore` y reglas de inclusión.
* **Notas técnicas:** Se puede configurar archivos `.gitkeep` para garantizar el rastreo de carpetas de documentación.

---

## Fase 1: Configuración del Entorno y MicroPython
**Estado:** Completado ✅

### 🎯 Objetivos Alcanzados
- Instalación de herramientas CLI en la PC para gestión de MicroPython.
- Borrado de memoria e instalación del firmware oficial de MicroPython en el ESP32.
- Configuración y validación del flujo de trabajo con mpremote.
- Verificación de comunicación serie y ejecución exitosa del script main.py.

### 🛠️ Comandos Clave Utilizados

1. Instalación de herramientas en la PC:
pip install mpremote

2. Borrado y Flasheo de Firmware (esptool):
python -m esptool --chip esp32 --port COM3 erase_flash
python -m esptool --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 ruta/al/firmware.bin

3. Transferencia y Ejecución en ESP32 (mpremote):
python -m mpremote connect COM3 cp src/main.py :main.py
python -m mpremote connect COM3 run src/main.py

---
## Entrada Bitácora - Fase 2: Control de Actuadores y Sensores Digitales (Semáforo Inteligente)

**Fecha:** 31 de Julio de 2026  
**Módulo:** 2.1 - LEDs, Sensores IR (FC-51) y Buzzer Activo  
**Estado de Fase:** Completada  

### 📝 Descripción del Avance
Se construyó el algoritmo completo para un semáforo inteligente de tránsito con detección de vía peatonal en el ESP32. El programa lee de forma continua dos sensores infrarrojos para registrar el ingreso y egreso de peatones sin usar temporizadores bloqueantes (`time.sleep`), garantizando el monitoreo constante.

### 🎯 Objetivos Alcanzados
- [✓] Control de secuencia del semáforo vehicular/peatonal con muestreo no bloqueante usando `time.ticks_ms()` y `time.ticks_diff()`.
- [✓] Lógica de prioridad peatonal: Si el tiempo de luz verde expira y el peatón sigue en la vía (registrado por Sensor 1 pero no por Sensor 2), el sistema entra en un bucle de retención manteniendo el parpadeo verde y activando el buzzer hasta que se desocupe la vía.
- [✓] Detección de infracciones: Activación del buzzer ante presencia peatonal durante las fases de luz amarilla y luz roja.
- [✓] Apagado seguro de actuadores mediante manejo de interrupciones con `KeyboardInterrupt`.

### 📦 Archivos Modificados/Añadidos
- `src/modules/modulo_2_1_led.py` (Código fuente del semáforo inteligente).
- `docs/08-bitacora` (Registro de avance).

---