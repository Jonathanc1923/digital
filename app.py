from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Reemplaza 'tu_clave_secreta_aqui' por una clave segura.

# Diccionario para almacenar usuarios y contraseñas (esto es solo para demostración)
usuarios = {
    'usuario1@gmail.com': 'contraseña1',
    'usuario2@gmail.com': 'contraseña2',
}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/inicioproyecto', methods=['POST'])
def inicioproyecto():
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')

    if correo in usuarios and usuarios[correo] == contraseña:
        return render_template('inicioproyecto.html')
    else:
        flash('Contraseña incorrecta. Por favor, inténtalo de nuevo.', 'error')
        return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run()
