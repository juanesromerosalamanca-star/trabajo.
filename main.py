import tkinter as tk
from tkinter import messagebox, ttk
from Administrador import Administrador
from Estudiante import Estudiante
from equipo import Equipo


class SistemaInventario:
    def __init__(self):
        self.equipos = []
        self.estudiantes = []
        self.encargados = []
        self.cargar_datos()

    def cargar_datos(self):
    
        try:
            with open("equipos.txt", "r", encoding="utf-8") as f:
                while True:
                    id_eq = f.readline().strip()
                    if not id_eq:
                        break
                    nombre = f.readline().strip()
                    categoria = f.readline().strip()
                    cantidad = int(f.readline().strip())
                    estado = f.readline().strip()
                    prestados_str = f.readline().strip()
                    prestados = int(prestados_str) if prestados_str.isdigit() else 0
                    self.equipos.append(Equipo(id_eq, nombre, categoria, cantidad, estado, prestados))
        except FileNotFoundError:
            pass

        # Cargar Estudiantes
        try:
            with open("estudiantes.txt", "r", encoding="utf-8") as f:
                while True:
                    id_est = f.readline().strip()
                    if not id_est:
                        break
                    estado = f.readline().strip()
                    contrasena = f.readline().strip()
                    correo = f.readline().strip()
                    rol = f.readline().strip()
                    telefono = f.readline().strip()
                    self.estudiantes.append(Estudiante(id_est, estado, contrasena, correo, rol, telefono))
        except FileNotFoundError:
            pass

        
        try:
            with open("encargados.txt", "r", encoding="utf-8") as f:
                while True:
                    id_enc = f.readline().strip()
                    if not id_enc:
                        break
                    cuenta = f.readline().strip()
                    contrasena = f.readline().strip()
                    correo = f.readline().strip()
                    rol = f.readline().strip()
                    self.encargados.append(Administrador(id_enc, cuenta, contrasena, correo, rol))
        except FileNotFoundError:
            pass

    def guardar_equipos(self):
        with open("equipos.txt", "w", encoding="utf-8") as f:
            for eq in self.equipos:
                f.write(f"{eq.id}\n{eq.nombre}\n{eq.categoria}\n{eq.cantidad}\n{eq.estado}\n{eq.prestados}\n")


class SistemaInventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario y Préstamos del Laboratorio")
        self.root.geometry("850x550")
        self.sistema = SistemaInventario()
        self.usuario_actual = None

        self.mostrar_menu_principal()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        self.limpiar_ventana()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Laboratorio - Control de Inventario", font=("Arial", 16, "bold")).pack(pady=15)
        
        tk.Button(frame, text="Iniciar Sesión como Encargado", width=30, command=self.login_encargado, bg="#2459d3", fg="white", font=("Arial", 11)).pack(pady=10)
        tk.Button(frame, text="Iniciar Sesión como Estudiante", width=30, command=self.login_estudiante, bg="#142840", fg="white", font=("Arial", 11)).pack(pady=10)

    def login_encargado(self):
        self.limpiar_ventana()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Login Encargado", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(frame, text="Cuenta / ID:").pack(anchor="w")
        e_cuenta = tk.Entry(frame, width=30)
        e_cuenta.pack(pady=5)

        tk.Label(frame, text="Contraseña:").pack(anchor="w")
        e_pass = tk.Entry(frame, width=30, show="*")
        e_pass.pack(pady=5)

        def verificar():
            cuenta = e_cuenta.get()
            pwd = e_pass.get()
            for enc in self.sistema.encargados:
                if (enc.cuenta == cuenta or enc.id == cuenta) and enc.contrasena == pwd:
                    self.usuario_actual = enc
                    self.panel_encargado()
                    return
            messagebox.showerror("Error", "Credenciales incorrectas")

        tk.Button(frame, text="Ingresar", command=verificar, bg="#2459d3", fg="white", width=15).pack(pady=10)
        tk.Button(frame, text="Volver", command=self.mostrar_menu_principal, width=15).pack()

    def login_estudiante(self):
        self.limpiar_ventana()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Login Estudiante", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(frame, text="Documento / ID:").pack(anchor="w")
        e_id = tk.Entry(frame, width=30)
        e_id.pack(pady=5)

        tk.Label(frame, text="Contraseña:").pack(anchor="w")
        e_pass = tk.Entry(frame, width=30, show="*")
        e_pass.pack(pady=5)

        def verificar():
            est_id = e_id.get()
            pwd = e_pass.get()
            for est in self.sistema.estudiantes:
                if est.id == est_id and est.contrasena == pwd:
                    self.usuario_actual = est
                    self.panel_estudiante()
                    return
            messagebox.showerror("Error", "Documento o contraseña incorrectos")

        tk.Button(frame, text="Ingresar", command=verificar, bg="#2459d3", fg="white", width=15).pack(pady=10)
        tk.Button(frame, text="Volver", command=self.mostrar_menu_principal, width=15).pack()

    def panel_encargado(self):
        self.limpiar_ventana()
        
        
        top_frame = tk.Frame(self.root, bg="#142840", height=40)
        top_frame.pack(fill="x", side="top")
        tk.Label(top_frame, text=f"Panel Encargado: {self.usuario_actual.cuenta}", bg="#142840", fg="white", font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        tk.Button(top_frame, text="Cerrar Sesión", command=self.mostrar_menu_principal, bg="#d32f2f", fg="white").pack(side="right", padx=10, pady=5)

        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        tk.Label(main_frame, text="Inventario Actual de Equipos", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        columns = ("ID", "Nombre", "Categoría", "Cantidad Total", "Prestados", "Disponibles", "Estado")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=12)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)
        
        self.tree.pack(fill="both", expand=True, pady=5)
        self.actualizar_tabla()

      
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill="x", pady=10)

        def simular_prestamo():
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("Aviso", "Seleccione un equipo para prestar.")
                return
            item = self.tree.item(selected)
            eq_id = item['values'][0]
            for eq in self.sistema.equipos:
                if eq.id == eq_id:
                    if eq.disponibles > 0:
                        eq.prestados += 1
                        eq.actualizar_estado()
                        self.sistema.guardar_equipos()
                        self.actualizar_tabla()
                        messagebox.showinfo("Éxito", "Préstamo registrado con éxito.")
                    else:
                        messagebox.showerror("Error", "No hay unidades disponibles.")
                    return

        def simular_devolucion():
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("Aviso", "Seleccione un equipo para devolver.")
                return
            item = self.tree.item(selected)
            eq_id = item['values'][0]
            for eq in self.sistema.equipos:
                if eq.id == eq_id:
                    if eq.prestados > 0:
                        eq.prestados -= 1
                        eq.actualizar_estado()
                        self.sistema.guardar_equipos()
                        self.actualizar_tabla()
                        messagebox.showinfo("Éxito", "Devolución registrada con éxito.")
                    else:
                        messagebox.showerror("Error", "Este equipo no tiene préstamos activos.")
                    return

        tk.Button(btn_frame, text="Prestar Unidad", command=simular_prestamo, bg="#2459d3", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Devolver Unidad", command=simular_devolucion, bg="#2b8a3e", fg="white", width=15).pack(side="left", padx=5)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for eq in self.sistema.equipos:
            eq.actualizar_estado()
            self.tree.insert("", "end", values=(eq.id, eq.nombre, eq.categoria, eq.cantidad, eq.prestados, eq.disponibles, eq.estado))

    def panel_estudiante(self):
        self.limpiar_ventana()
        
        top_frame = tk.Frame(self.root, bg="#2459d3", height=40)
        top_frame.pack(fill="x", side="top")
        tk.Label(top_frame, text=f"Panel Estudiante - ID: {self.usuario_actual.id}", bg="#2459d3", fg="white", font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        tk.Button(top_frame, text="Cerrar Sesión", command=self.mostrar_menu_principal, bg="#d32f2f", fg="white").pack(side="right", padx=10, pady=5)

        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        tk.Label(main_frame, text="Equipos Disponibles en el Laboratorio", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        columns = ("ID", "Nombre", "Categoría", "Disponibles", "Estado")
        self.tree_est = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree_est.heading(col, text=col)
            self.tree_est.column(col, width=140)
        
        self.tree_est.pack(fill="both", expand=True, pady=5)
        
        for eq in self.sistema.equipos:
            eq.actualizar_estado()
            self.tree_est.insert("", "end", values=(eq.id, eq.nombre, eq.categoria, eq.disponibles, eq.estado))

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaInventarioApp(root)
    root.mainloop()
  
