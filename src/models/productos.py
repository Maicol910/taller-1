from src.config.db import DB

class productosModel():
    def traerTodos(self):
        cursor = DB.cursor()
        
        cursor.execute('select * from productos')
        
        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre, descripcion, precio_venta, precio_compra, ganancia, estado):
        cursor = DB.cursor()

        cursor.execute('insert into productos(nombre, descripcion, precio_venta, precio_compra,ganancia, estado) values(?, ?, ?, ?, ?, ?)',(nombre, descripcion, precio_venta, precio_compra, ganancia, estado,))

        cursor.close()

    def editar(self,id,nombre, descripcion, precio_venta, precio_compra,ganancia, estado):
        cursor = DB.cursor()

        cursor.execute('update productos set nombre=?, descripcion=?, precio_venta=?, precio_compra=?, ganancia=?, estado=? where id=?',(nombre, descripcion, precio_venta, precio_compra,ganancia, estado,id,))

        cursor.close()
        
    