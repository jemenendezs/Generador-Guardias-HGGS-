# 📅 Generador de Guardias HGGS

Una herramienta Python para generar calendarios de guardias médicas en formato TXT e ICS, facilitando la organización y visualización de turnos hospitalarios.

## 🚀 Características

- **Procesamiento intuitivo**: Copia y pega directamente desde Excel tu fila completa de guardias
- **Múltiples formatos**: Genera archivos TXT (legible) e ICS (para calendarios)
- **Compatibilidad multiplataforma**: Funciona en Windows, Linux y Android (Termux)
- **Interfaz amigable**: Guía paso a paso con mensajes claros e instrucciones detalladas
- **Estadísticas automáticas**: Resumen de días de guardia y libres por tipo de turno
- **Código optimizado**: Legible, mantenible y bien estructurado

## 📋 Formatos de Guardia Soportados

| Código | Descripción | Horario |
|--------|-------------|---------|
| `M8` | Guardia AM 8 horas | 07:30 - 15:30 |
| `N8` | Guardia PM 8 horas | 15:30 - 23:30 |
| `M12` | Guardia AM 12 horas | 07:30 - 20:00 |
| `N12` | Guardia PM 12 horas | 19:30 - 08:00 (día siguiente) |
| `M16` | Guardia AM 16 horas | 07:30 - 23:30 |
| `N16` | Guardia PM 16 horas | 15:30 - 07:30 (día siguiente) |
| `L` | Día Libre | - |

## 🛠️ Instalación

### Prerrequisitos
- Python 3.6 o superior
- No se requieren librerías externas

### Ejecución directa
```
python generador_guardias.py
```

# 📖 Uso

1. **Ejecuta el script**
2. **Selecciona el mes** (1-12)
3. **Sigue las instrucciones** para copiar desde Excel:
   - Abre el archivo Excel de guardias
   - Busca tu fila correspondiente
   - Selecciona toda la fila desde el día 1 hasta el final del mes
   - Copia y pega la secuencia completa
4. **Archivos generados automáticamente** en la carpeta de Descargas

### 📝 Ejemplo de Entrada Completa

```
M16 L L N8 M12 N16 L L L M12 N8 L L L M16

```

### 📤 Archivos Generados
- `listado_guardias_enero_2024.txt` - Listado legible con estadísticas detalladas
- `guardias_enero_2024.ics` - Para importar en Google Calendar, Outlook, Apple Calendar, etc.

### 🎮 Interfaz de Usuario
El programa guía al usuario paso a paso:

```

📅 GENERADOR DE GUARDIAS HGGS
==================================================
👉 Ingresa el número del mes (1-12): 3

📋 Mes seleccionado: MARZO 2024

==================================================
📋 INSTRUCCIONES PARA COPIAR DESDE EXCEL
==================================================
Para el mes de MARZO 2024 (31 días):

1. 📊 Abre el archivo Excel de guardias
2. 👤 Busca la fila correspondiente a tu usuario/nombre
3. 📝 En esa fila, localiza la secuencia de guardias que comienza desde el día 1
4. 🖱️  Selecciona TODA la fila desde la columna del día 1 hasta el final del mes
5. 📋 Copia (Ctrl+C) toda esa secuencia

🔍 FORMATO ESPERADO (ejemplo con 7 días):
   M16   L    L   N8   M12   N16   L
   (puede contener espacios o tabulaciones entre los códigos)

📌 CÓDIGOS DISPONIBLES:
   M8  = Guardia AM 8h (07:30-15:30)
   N8  = Guardia PM 8h (15:30-23:30)
   M12 = Guardia AM 12h (07:30-20:00)
   N12 = Guardia PM 12h (19:30-08:00)
   M16 = Guardia AM 16h (07:30-23:30)
   N16 = Guardia PM 16h (15:30-07:30)
   L   = Día Libre

👉 Ahora PEGA la cadena copiada desde Excel y presiona ENTER:
--------------------------------------------------
```

## 🗂️ Estructura del Proyecto
```
generador_guardias.py    # Script principal
README.md                # Esta documentación
```

## 💻 Tecnologías Utilizadas

- **Python Standard Library**: 
  - `datetime` - Manejo de fechas y horas
  - `os` - Operaciones del sistema de archivos
  - `uuid` - Generación de identificadores únicos
- **Formatos soportados**: 
  - TXT (formato legible para humanos)
  - ICS (estándar iCalendar para aplicaciones de calendario)
- **Codificación**: UTF-8 para soporte de caracteres especiales

## 📱 Uso en Android (Termux)

```bash
# Instalar Python en Termux
pkg install python

# Ejecutar el script
python generador_guardias.py

```

Los archivos se guardan automáticamente en `/storage/emulated/0/Download/`

## 🔧 Características Técnicas

* ✅ Validación de entrada robusta - Verifica formatos y valores válidos
* ✅ Manejo de timezones y fechas - Gestión correcta de horarios que cruzan medianoche
* ✅ Generación de UUID únicos - Para eventos de calendario sin conflictos
* ✅ Soporte para guardias nocturnas - Manejo automático de guardias que terminan al día siguiente
* ✅ Estadísticas automáticas - Conteo por tipo de guardia y días libres
* ✅ Código modular y mantenible - Arquitectura orientada a objetos
* ✅ Compatibilidad multiplataforma - Windows, Linux, macOS, Android
* ✅ Procesamiento flexible - Acepta espacios y tabulaciones en la entrada

## 🎯 Ejemplo de Salida

Archivo TXT generado:

```
GUARDIAS MARZO 2024 HGGS
==========================

* 01/03/2024 - Guardia AM 16 horas
* 04/03/2024 - Guardia PM 8 horas
* 05/03/2024 - Guardia AM 12 horas
* 06/03/2024 - Guardia PM 16 horas

--- RESUMEN ---
Total de días del mes: 31
Días de guardia: 15
Días libres: 16
Guardia AM 8 horas: 3
Guardia PM 8 horas: 2
Guardia AM 12 horas: 4
Guardia PM 12 horas: 2
Guardia AM 16 horas: 3
Guardia PM 16 horas: 1
```

Archivo ICS: Archivo compatible con todas las aplicaciones de calendario modernas, listo para importar.

## 📄 Estructura del Código

El proyecto sigue una arquitectura modular:

```
class GeneradorGuardias:
    ├── procesar_entrada_mes()      # Validación de entrada del mes
    ├── mostrar_instrucciones()     # Instrucciones detalladas para el usuario
    ├── procesar_cadena_guardias()  # Procesamiento de la cadena de guardias
    ├── generar_txt()               # Generación de archivo de texto
    ├── generar_ics()               # Generación de archivo de calendario
    └── ejecutar()
```

## 🐛 Solución de Problemas

**Error: "No se encontraron guardias válidas"**

* Verifica que estés usando los códigos correctos (M8, N8, M12, N12, M16, N16, L)
* Asegúrate de copiar toda la fila desde el día 1 en Excel

**Error: "Entrada inválida"**

* Solo se aceptan números del 1 al 12 para el mes
* La cadena de guardias no debe contener caracteres especiales

**Los archivos no aparecen en Descargas**

* Verifica los permisos de escritura en la carpeta de descargas
* En Android, asegúrate de que Termux tenga permisos de almacenamiento

**Problemas con el formato de entrada**

* Asegúrate de copiar directamente desde Excel, no modificar manualmente
* El programa acepta tanto espacios como tabulaciones entre los códigos

## 📄 Licencia

Este proyecto es de uso libre para la comunidad médica. Distribuido bajo licencia MIT.

## 👨‍💻 Autor

Desarrollado por el Dr. Jorge Menéndez para facilitar la gestión de guardias médicas en el HGGS.

---

**Versión 2.0** - Actualizado con nuevos tipos de guardia y mejoras en la interfaz de usuario.
