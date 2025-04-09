from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        # Aquí puedes procesar o guardar el mensaje
        print(f"Mensaje de {nombre} ({email}): {mensaje}")
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)