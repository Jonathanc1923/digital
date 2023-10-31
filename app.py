from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'as8327e9adak3iiq9'  # Reemplaza 'tu_clave_secreta_aqui' por una clave segura.

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/inicioproyecto', methods=['POST'])
def inicioproyecto():
    return render_template('inicioproyecto.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

