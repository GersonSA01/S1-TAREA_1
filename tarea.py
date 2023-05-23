class Producto:
    def __init__(self, id_producto,cant_venta,cant_min,id_detalle):
        self.id_producto = id_producto
        self.cant_venta = cant_venta
        self.cant_min = cant_min
        self.id_detalle = id_detalle
        self.detalle=[]

    
    def __str__(self):
        return f"{self.id_producto} - {self.cant_venta} - {self.cant_min} - {self.id_detalle}"
    
    def calcular(self,deta1):
        self.detalle.append(deta1)
    
    
class Detalle_producto:
    def __init__(self,id_detalle,nombre,tipo,precio,iva):
        self.id_detalle = id_detalle
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.iva = iva
        
    def __str__(self):
        return f"{self.id_detalle} - {self.nombre} - {self.tipo} - {self.precio} - {self.iva}"
  


class Tienda:
    def __init__(self,id_tienda,saldo_caja):
        self.id_tienda = id_tienda
        self.saldo_caja = saldo_caja
        self.producto=[]
    
    def __str__(self):
        return f"{self.id_tienda} - {self.saldo_caja}"

    
    def calcular(self,p1):
        self.producto.append(p1)
        

    
class Inventario:
    def __init__(self,id_inventario,producto,cant_actual):
        self.id_inventario = id_inventario
        self.producto = producto
        self.cant_actual = cant_actual

    
    def __str__(self):
        return f"{self.id_inventario} - {self.producto} - {self.cant_actual}"

    
    
class Impuesto:
    def __init__(self, iva_papeleria, iva_supermercado, iva_drogueria):
        self.iva_papeleria = iva_papeleria
        self.iva_supermercado = iva_supermercado
        self.iva_drogueria = iva_drogueria

    def __str__(self):
        return f"{self.iva_papeleria} - {self.iva_supermercado} - {self.iva_drogueria}"
    
    
class Tipo_producto:
    def __init__(self, papeleria, supermercado, drogueria):
        self.papeleria = papeleria
        self.supermercado = supermercado
        self.drogueria = drogueria

    def __str__(self):
        return f"{self.papeleria} - {self.supermercado} - {self.drogueria}"

    



#Agregacion
tip=Tipo_producto("papeleria","supermercado","drogueria")
impu=Impuesto(1.16,1.04,1.12)

deta1 = Detalle_producto(1, "pan", tip, 0.5, impu)
print("Agregacion:\n", deta1)




#Compososicion
p1=Producto(1,23,12,0)
p1.calcular(deta1)
print("\nComposicion producto:\n",p1)

tienda=Tienda(1,"saldo cuenta")
tienda.calcular(p1)
print("\nComposicion tienda:\n",tienda)


#Agregacion
invent=Inventario(1,p1,"calculo")
print("\nAgregacion Inventario:\n",invent)




