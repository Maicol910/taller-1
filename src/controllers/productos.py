from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import productosModel

@app.route('/productos')
def productos():

    ProductosModel = productosModel() 

    productos = ProductosModel.traerTodos()
    
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    # esta funcion sirve para mostral el formulario
    # y para crear un nuevo producto 
    # estos pasos se identifican con los metodos

    if request.method == 'GET':
        # mostrar el formulario de creacion
        return render_template ('productos/crear.html')
    
    # la creacion del producto 
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_venta = request.form.get('precio_venta')
    precio_compra = request.form.get('precio_compra')
    estado = request.form.get('estado')
    
    ProductosModel = productosModel()

    ProductosModel.crear(nombre, descripcion, precio_venta, precio_compra, estado)

    return redirect(url_for('productos'))