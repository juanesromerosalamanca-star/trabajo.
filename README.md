# Sistema de Inventario y Préstamos del Laboratorio



---

##  Características principales
* **Control de Inventario:** Gestión de equipos de laboratorio (multímetros, osciloscopios, fuentes de poder, kits, etc.) con cálculo automático de unidades disponibles
* **Control de Préstamos y Devoluciones:** Permite registrar salidas y entradas de unidades actualizando el stock en tiempo real[cite: 43, 45].
* **Autenticación por Roles:** 
  * **Encargado (Administrador):** Gestión total del inventario, préstamos y devoluciones.
  * **Estudiante:** Consulta de equipos disponibles en el laboratorio.
* **Persistencia en Archivos de Texto:** Almacenamiento local utilizando archivos planos (`equipos.txt`, `estudiantes.txt`, `encargados.txt`)[cite: 44, 46, 48].

---

##  Estructura del Proyecto

```text
├── main.py               # Archivo principal con la Interfaz Gráfica (GUI) y lógica de ejecución
├── Administrador.py      # Clase Administrador / Encargado[cite: 39]
├── Estudiante.py         # Clase Estudiante[cite: 47]
├── equipo.py             # Clase Equipo y propiedades calculadas[cite: 45]
├── base_de_datos.py      # Lógica de persistencia y manejo de datos[cite: 40]
├── equipos.txt           # Base de datos en texto plano para equipos[cite: 46]
├── estudiantes.txt       # Base de datos en texto plano para estudiantes
└── encargados.txt        # Credenciales de acceso para encargados# trabajo.
