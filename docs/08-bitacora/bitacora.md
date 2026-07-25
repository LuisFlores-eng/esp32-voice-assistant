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
