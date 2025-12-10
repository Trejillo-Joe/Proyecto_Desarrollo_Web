from flask import Flask
from app.extensiones import mysql
from app.routes.public_routes import public_bp
from app.routes.auth_routes import auth_bp
from app.routes.editor_routes import editor_bp
from app.routes.admin_routes import admin_bp

def create_app(): # Esta funcion crea la aplicacion Flask y la configura, la configuracion se base en las extensiones y las rutas que se importan
    app = Flask(__name__)
    app.secret_key = 'zapachi_puro_ct' # Clave secreta para la aplicacion, se usa para firmar cookies y sesiones, si se cambia la clave, se invalidan las sesiones existentes

    app.config['MYSQL_HOST'] = 'Zapachi.mysql.pythonanywhere-services.com' # Host del servidor MySQL, en este caso es el servidor de PythonAnywhere
    app.config['MYSQL_USER'] = 'Zapachi' # Usuario de la base de datos MySQL, en este caso es el usuario de PythonAnywhere
    app.config['MYSQL_PASSWORD'] = 'Bash2149' # Contraseña del usuario de la base de datos MySQL, en este caso es la contraseña de PythonAnywhere
    app.config['MYSQL_DB'] = 'Zapachi$Zproductos_db' # Nombre de la base de datos MySQL, en este caso es la base de datos de PythonAnywhere

    mysql.init_app(app) # Inicializa la extension MySQL con la aplicacion Flask

    app.register_blueprint(public_bp) # Registra los blueprints de las rutas publicas, de autenticacion, de editor y de administrador
    app.register_blueprint(auth_bp) # Registra el blueprint de las rutas de autenticacion
    app.register_blueprint(editor_bp) # Registra el blueprint de las rutas del editor
    app.register_blueprint(admin_bp) # Registra el blueprint de las rutas del administrador

    return app 
