# 📅 Generador de Guardias HGGS

Una herramienta Python para generar calendarios de guardias médicas en formato TXT e ICS, facilitando la organización y visualización de turnos hospitalarios.

## 🚀 Características

- **Procesamiento intuitivo**: Introduce tus guardias en formato simple (`N12 L L M8 M12`)
- **Múltiples formatos**: Genera archivos TXT (legible) e ICS (para calendarios)
- **Compatibilidad multiplataforma**: Funciona en Windows, Linux y Android (Termux)
- **Interfaz amigable**: Guía paso a paso con mensajes claros
- **Estadísticas automáticas**: Resumen de días de guardia y libres
- **Código optimizado**: Legible, mantenible y bien documentado

## 📋 Formatos de Guardia Soportados

| Código | Descripción | Horario |
|--------|-------------|---------|
| `N12` | Guardia PM 12 horas | 19:30 - 08:00 (día siguiente) |
| `M12` | Guardia AM 12 horas | 07:30 - 20:00 |
| `M8` | Guardia AM 8 horas | 07:30 - 15:30 |
| `L` | Día Libre | - |

## 🛠️ Instalación

### Prerrequisitos
- Python 3.6 o superior
- No se requieren librerías externas

### Ejecución directa
```
python generador_guardias.py

```

## 📖 Uso

1. **Ejecuta el script**
2. **Selecciona el mes** (1-12)
3. **Pega tu cadena de guardias** en el formato:
```

N12 L L M8 M12 N12 L L L M12 N12 L L L M12

```
4. **Archivos generados automáticamente** en la carpeta de Descargas

### 📝 Ejemplo de Entrada Completa
```

N12 L L M8 M12 N12 L L L M12 N12 L L L M12 L L M8 N12 L L M12 M8 L L N12

```

### 📤 Archivos Generados
- `listado_guardias_enero_2024.txt` - Listado legible con estadísticas
- `guardias_enero_2024.ics` - Para importar en Google Calendar, Outlook, Apple Calendar, etc.

### 🎮 Interfaz de Usuario
El programa guía al usuario paso a paso:
```

📅 GENERADOR DE GUARDIAS HGGS
==================================================
👉Ingresa el número del mes (1-12): 3

📋 Mes seleccionado: MARZO 2024

==================================================
FORMATO:Cadena con N12, M12, M8, L separados por espacios/tabs
EJEMPLO:N12 L L M8 M12 N12 L L L M12
==================================================
Pega la cadena completa de guardias:

```

## 🗂️ Estructura del Proyecto

```

generador_guardias.py    # Script principal
README.md# Esta documentación

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

Los archivos se guardan automáticamente en /storage/emulated/0/Download/

## 🔧 Características Técnicas

* ✅ Validación de entrada robusta - Verifica formatos y valores válidos
* ✅ Manejo de timezones y fechas - Gestión correcta de horarios que cruzan medianoche
* ✅ Generación de UUID únicos - Para eventos de calendario sin conflictos
* ✅ Soporte para guardias nocturnas - Manejo automático de guardias que terminan al día siguiente
* ✅ Estadísticas automáticas - Conteo por tipo de guardia y días libres
* ✅ Código modular y mantenible - Arquitectura orientada a objetos
* ✅ Compatibilidad multiplataforma - Windows, Linux, macOS, Android

## 🎯 Ejemplo de Salida

Archivo TXT generado:

```
GUARDIAS MARZO 2024 HGGS
==========================

* 01/03/2024 - Guardia PM 12 horas
* 04/03/2024 - Guardia AM 8 horas
* 05/03/2024 - Guardia AM 12 horas

--- RESUMEN ---
Total de días del mes: 30
Días de guardia: 15
Días libres: 15
Guardia PM 12 horas: 5
Guardia AM 12 horas: 7
Guardia AM 8 horas: 3
```

**Archivo ICS:**

Archivo compatible con todas las aplicaciones de calendario modernas, listo para importar.

## 📄 Estructura del Código

El proyecto sigue una arquitectura modular:

```python
class GeneradorGuardias:
    ├── _procesar_entrada_mes()      # Validación de entrada del mes
    ├── _procesar_cadena_guardias()  # Procesamiento de la cadena de guardias
    ├── _generar_txt()              # Generación de archivo de texto
    ├── _generar_ics()              # Generación de archivo de calendario
    └── ejecutar()                  # Método principal que orquesta el flujo
```

## 🐛 Solución de Problemas

*Error: "No se encontraron guardias válidas"*

* Verifica que estés usando los códigos correctos (N12, M12, M8, L)
* Asegúrate de separar los elementos con espacios o tabs

*Error: "Entrada inválida"*

* Solo se aceptan números del 1 al 12 para el mes
* La cadena de guardias no debe contener caracteres especiales

*Los archivos no aparecen en Descargas*

* Verifica los permisos de escritura en la carpeta de descargas
* En Android, asegúrate de que Termux tenga permisos de almacenamiento.

## 📄 Licencia

Este proyecto es de uso libre para la comunidad médica. Distribuido bajo licencia MIT.

## 👨‍💻 Autor

Desarrollado por el Dr. Jorge Menéndez para facilitar la gestión de guardias médicas en el HGGS.
