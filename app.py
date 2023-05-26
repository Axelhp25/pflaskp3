from flask import *
from Models.persona import modelPersona
import conexion
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Bienvenido</h1>"
@app.route('/crear',methods=['GET','POST'])
def crear():
    if request.method == 'POST':
        nombre=request.form['nombre']
        apellido = request.form['apellido']
        tel = request.form['telefono']
        correo = request.form['correo']
        modelPersona.create(conexion.obtener_conexion(),nombre,apellido,tel,correo)
        return redirect(url_for('listar'))
    else:
        return render_template('create.html')
@app.route('/index',methods=['GET','POST'])
def listar():
    listado = modelPersona.ver(conexion.obtener_conexion())
    return render_template('index.html',listado=listado)

if __name__ == '__main__':
    app.run(debug=True)