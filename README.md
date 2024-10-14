# Proyecto: Sistema Medico 🏥

✨ *Descripción*  

Este proyecto es un sistema de gestión médica desarrollado con Django. Permite gestionar información de pacientes, médicos, citas, historiales clínicos y más. 

El sistema está diseñado para facilitar la administración de una clínica o consultorio médico, proporcionando herramientas para agilizar procesos, organizar información y mejorar la atención al paciente.


**Características Principales**

* **Gestión de Pacientes:** Registro, actualización y consulta de información de pacientes (datos personales, historial médico, etc.).
* **Gestión de Médicos:** Registro, actualización y consulta de información de médicos (especialidad, horario, etc.).
* **Gestión de Citas:** Agendamiento, reprogramación y cancelación de citas médicas.
* **Historiales Clínicos:** Creación y consulta de historiales clínicos para cada paciente, incluyendo diagnósticos, tratamientos y medicamentos.
* **Reportes:** Generación de reportes de pacientes, citas, ingresos, etc.
* **Autenticación de Usuarios:**  Sistema de inicio de sesión seguro para proteger la información del sistema.
* **Interfaz Intuitiva:**  Diseño amigable y fácil de usar para facilitar la navegación y el acceso a la información.

🛠️ **Tecnologías Utilizadas**

* **Backend:**
    * **Django:** Framework web robusto para el desarrollo del backend.
    * **SQLite:** Base de datos para almacenar la información del sistema.
* **Frontend:**
    * **HTML, CSS, JavaScript:** Lenguajes para la creación de la interfaz de usuario.
    * **Bootstrap (opcional):** Framework CSS para un diseño responsivo y moderno.

## ⚙️ Cómo Ejecutar la Aplicación  

1. *Clonar el repositorio:*
   ```bash
   git clone https://github.com/SnayderCJ/proy_crud_POO_B1.git
   cd proy_crud_POO_B1
   ```
    
3. *Crear (o activar) un entorno virtual::*   
    ```bash
    py -m venv venv  # Windows
    venv\Scripts\activate 

    python3 -m venv venv #Linux
    source venv/bin/activate
    ```

4. *Instalar las dependencias:*
    ```bash
    pip install -r requirements.txt
    ```

5. *Aplicar las migraciones:*
    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```

6. *Crear un superusuario:*
    ```bash
    py manage.py createsuperuser
    ```

7. *Ejecutar el servidor de desarrollo:*
    ```bash
    py manage.py runserver
    ```

8. *Acceder a la aplicación en tu navegador:*
    
    *   Abre tu navegador web y visita: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (para la interfaz principal)
    

9. *Iniciar sesión en el panel de administración:*
    
    *   Accede al panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (utiliza las credenciales del superusuario). que creaste en el paso 5.
    

🤝 *Contribuciones*:
Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna sugerencia, no dudes en abrir un "issue" o enviar un "pull request".
