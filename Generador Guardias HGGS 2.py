# Licencia MIT
# Copyright (c) 2025 Jorge Menéndez S.
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para tratar el Software sin restricción, incluidos, entre otros, los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y para permitir a las personas a quienes se les proporcione el Software que lo hagan, sujeto a las siguientes condiciones:
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADA A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADA DE, O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.

from datetime import datetime, timedelta
import os
import uuid

# Configuración constante
CONFIG = {
    "horarios": {
        "N12": ("19:30", "08:00"),  # Guardia PM 12h (termina al día siguiente)
        "M12": ("07:30", "20:00"),  # Guardia AM 12h
        "M8": ("07:30", "15:30"),   # Guardia AM 8h
        "L": None  # Libre
    },
    "descripciones": {
        "N12": "Guardia PM 12 horas",
        "M12": "Guardia AM 12 horas", 
        "M8": "Guardia AM 8 horas",
        "L": "Día Libre"
    },
    "meses": {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 
        5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
}

class GeneradorGuardias:
    def __init__(self):
        self.ruta_descargas = self._obtener_ruta_descargas()
    
    def _obtener_ruta_descargas(self):
        """Obtiene la ruta de descargas compatible con diferentes sistemas"""
        if os.name == 'posix' and 'ANDROID_STORAGE' in os.environ:
            return "/storage/emulated/0/Download/"
        return os.path.join(os.path.expanduser("~"), "Downloads")
    
    def _procesar_entrada_mes(self):
        """Solicita y valida la entrada del mes"""
        while True:
            try:
                mes_num = int(input("👉 Ingresa el número del mes (1-12): "))
                if 1 <= mes_num <= 12:
                    return mes_num
                print("⚠ Número de mes inválido. Intenta de nuevo.")
            except ValueError:
                print("⚠ Entrada inválida. Ingresa un número del 1 al 12.")
    
    def _mostrar_instrucciones(self):
        """Muestra las instrucciones de formato"""
        print("\n" + "=" * 50)
        print("FORMATO: Cadena con N12, M12, M8, L separados por espacios/tabs")
        print("EJEMPLO: N12 L L M8 M12 N12 L L L M12 N12 L L L M12")
        print("=" * 50)
        print("Pega la cadena completa de guardias:")
    
    def _procesar_cadena_guardias(self, cadena):
        """
        Procesa la cadena de texto con formato: N12 L L M8 M12 N12...
        Retorna lista de guardias y estadísticas
        """
        elementos = cadena.replace('\t', ' ').split()
        guardias = []
        dia_actual = 1
        
        for elemento in elementos:
            tipo = elemento.strip().upper()
            
            if tipo in CONFIG["horarios"]:
                if tipo != "L":  # Solo agregar si no es libre
                    guardias.append((dia_actual, tipo))
                dia_actual += 1
            else:
                print(f"⚠ Elemento no reconocido: '{elemento}' - se omitirá")
        
        return guardias
    
    def _mostrar_calendario(self, guardias, mes_nombre, mes_num, anio):
        """Muestra el calendario de guardias procesado"""
        print(f"\n📅 Calendario de guardias para {mes_nombre.upper()} {anio}:")
        for dia, tipo in guardias:
            fecha = f"{dia:02d}/{mes_num:02d}/{anio}"
            print(f"   - {fecha}: {CONFIG['descripciones'][tipo]}")
    
    def _mostrar_estadisticas(self, guardias, total_dias):
        """Muestra estadísticas del procesamiento"""
        dias_guardia = len(guardias)
        dias_libres = total_dias - dias_guardia
        
        print(f"\n✅ Procesamiento completado:")
        print(f"   - Días procesados: {total_dias}")
        print(f"   - Días de guardia: {dias_guardia}")
        print(f"   - Días libres: {dias_libres}")
        
        # Conteo por tipo de guardia
        for tipo in ["N12", "M12", "M8"]:
            count = sum(1 for _, t in guardias if t == tipo)
            if count > 0:
                print(f"   - {CONFIG['descripciones'][tipo]}: {count}")
    
    def _generar_txt(self, guardias, mes_nombre, mes_num, anio, total_dias):
        """Genera archivo TXT con el listado de guardias"""
        titulo = f"GUARDIAS {mes_nombre.upper()} {anio} HGGS"
        contenido = [titulo, "=" * len(titulo), ""]
        
        # Lista de guardias
        for dia, tipo in guardias:
            fecha = f"{dia:02d}/{mes_num:02d}/{anio}"
            contenido.append(f"* {fecha} - {CONFIG['descripciones'][tipo]}")
        
        # Estadísticas
        contenido.extend([
            "", "--- RESUMEN ---",
            f"Total de días del mes: {total_dias}",
            f"Días de guardia: {len(guardias)}",
            f"Días libres: {total_dias - len(guardias)}"
        ])
        
        for tipo in ["N12", "M12", "M8"]:
            count = sum(1 for _, t in guardias if t == tipo)
            if count > 0:
                contenido.append(f"{CONFIG['descripciones'][tipo]}: {count}")
        
        # Guardar archivo
        nombre_archivo = f"listado_guardias_{mes_nombre}_{anio}.txt"
        ruta_completa = os.path.join(self.ruta_descargas, nombre_archivo)
        
        with open(ruta_completa, "w", encoding='utf-8') as archivo:
            archivo.write('\n'.join(contenido))
        
        return ruta_completa
    
    def _generar_ics(self, guardias, mes_nombre, mes_num, anio):
        """Genera archivo ICS para calendario"""
        uid_base = str(uuid.uuid4())
        lineas = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0", 
            "PRODID:-//Guardias HGGS//iCal//ES",
            f"X-WR-CALNAME:GUARDIAS {mes_nombre.upper()} {anio} HGGS",
            "CALSCALE:GREGORIAN"
        ]
        
        for dia, tipo in guardias:
            inicio, fin = CONFIG["horarios"][tipo]
            inicio_dt = datetime(anio, mes_num, dia, 
                               int(inicio.split(':')[0]), 
                               int(inicio.split(':')[1]))
            
            # Manejar guardias que terminan al día siguiente
            if tipo == "N12":
                fin_dt = datetime(anio, mes_num, dia,
                                int(fin.split(':')[0]), 
                                int(fin.split(':')[1])) + timedelta(days=1)
            else:
                fin_dt = datetime(anio, mes_num, dia,
                                int(fin.split(':')[0]), 
                                int(fin.split(':')[1]))
            
            evento = [
                "BEGIN:VEVENT",
                f"UID:{uid_base}-{anio}{mes_num:02d}{dia:02d}{tipo}",
                f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}",
                f"DTSTART:{inicio_dt.strftime('%Y%m%dT%H%M%S')}",
                f"DTEND:{fin_dt.strftime('%Y%m%dT%H%M%S')}",
                f"SUMMARY:{CONFIG['descripciones'][tipo]}",
                f"DESCRIPTION:Turno de {CONFIG['descripciones'][tipo].lower()}",
                "CLASS:PUBLIC",
                "PRIORITY:5",
                "COLOR:RED",
                "END:VEVENT"
            ]
            lineas.extend(evento)
        
        lineas.append("END:VCALENDAR")
        
        # Guardar archivo
        nombre_archivo = f"guardias_{mes_nombre}_{anio}.ics"
        ruta_completa = os.path.join(self.ruta_descargas, nombre_archivo)
        
        with open(ruta_completa, "w", encoding='utf-8') as archivo:
            archivo.write('\n'.join(lineas))
        
        return ruta_completa
    
    def ejecutar(self):
        """Función principal que orquesta todo el proceso"""
        print("📅 GENERADOR DE GUARDIAS HGGS")
        print("=" * 50)
        
        # Configuración inicial
        mes_num = self._procesar_entrada_mes()
        anio = datetime.now().year
        mes_nombre = CONFIG["meses"][mes_num]
        
        print(f"\n📋 Mes seleccionado: {mes_nombre.upper()} {anio}")
        
        # Entrada de datos
        self._mostrar_instrucciones()
        cadena = input().strip()
        
        if not cadena:
            print("❌ No se ingresó ninguna cadena. Saliendo...")
            return
        
        # Procesamiento
        guardias = self._procesar_cadena_guardias(cadena)
        total_dias = len(cadena.split())  # Total de elementos procesados
        
        if not guardias:
            print("❌ No se encontraron guardias válidas. Saliendo...")
            return
        
        # Resultados
        self._mostrar_calendario(guardias, mes_nombre, mes_num, anio)
        self._mostrar_estadisticas(guardias, total_dias)
        
        # Generación de archivos
        self._generar_txt(guardias, mes_nombre, mes_num, anio, total_dias)
        self._generar_ics(guardias, mes_nombre, mes_num, anio)
        
        print(f"\n💾 Archivos guardados en: {self.ruta_descargas}")

def main():
    """Punto de entrada principal"""
    generador = GeneradorGuardias()
    generador.ejecutar()

if __name__ == "__main__":
    main()