from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.extensiones import mysql

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def requiere_admin(): # Verifica si el usuario tiene rol de administrador
    return session.get('rol_id') == 1  # Solo el admin tiene rol_id = 1
 
@admin_bp.route('/usuarios') # Ruta para listar usuarios. ruta protegida por el rol de administrador
def usuarios():
    if not requiere_admin(): # Verifica si el usuario tiene rol de administrador
        flash('Acceso denegado', 'danger') # Si el usuario no es administrador, muestra un mensaje de acceso denegado
        return redirect(url_for('public.index'))

    cur = mysql.connection.cursor() 
    cur.execute("""
        SELECT u.id, u.username, u.email, r.nombre AS rol
        FROM usuarios u
        JOIN roles r ON u.rol_id = r.id
        WHERE r.nombre != 'admin'
    """) # Consulta para obtener los usuarios y sus roles, excluyendo al administrador 
    usuarios = cur.fetchall()
    cur.close()
    return render_template('admin/usuarios.html', usuarios=usuarios)

@admin_bp.route('/cambiar_rol/<int:user_id>/<int:nuevo_rol>') # Ruta para cambiar el rol de un usuario. ruta protegida por el rol de administradorSSSSS
def cambiar_rol(user_id, nuevo_rol):
    if not requiere_admin(): # Verifica si el usuario tiene rol de administrador
        flash('Acceso denegado', 'danger')
        return redirect(url_for('public.index')) 

    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET rol_id = %s WHERE id = %s", (nuevo_rol, user_id)) # Actualiza el rol del usuario en la base de datos
    mysql.connection.commit()
    cur.close()

    flash('Rol actualizado correctamente', 'success') # Muestra un mensaje de éxito al cambiar el rol del usuario
    return redirect(url_for('admin.usuarios'))
