from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensiones import mysql
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__) # Define el blueprint para las rutas de autenticación

@auth_bp.route('/login', methods=['GET', 'POST']) # Ruta para iniciar sesión 
def login():
    if request.method == 'POST': # esta linea verifica si la solicitud es de tipo POST, lo que significa que se está enviando un formulario
        email = request.form['email'] # Obtiene el email del formulario
        password = request.form['password'] # Obtiene la contraseña del formulario

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = %s", (email,)) # esta consulta busca al usuario en la base de datos por su email
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[3], password):  # user[3] es la contraseña hasheada en la base de datos 
            session['user_id'] = user[0] # ID del usuario que va inicializar la sesión
            session['username'] = user[1] # Nombre del usuario
            session['rol_id'] = user[4] # Rol del usuario (1 = admin, 2 = editor, 3 = cliente) 
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('public.index'))
        else:
            flash('Credenciales incorrectas', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (username, email, password, rol_id) VALUES (%s, %s, %s, %s)", 
                    (username, email, password, 3))  # 3 = cliente
        mysql.connection.commit()
        cur.close()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('public.index'))


