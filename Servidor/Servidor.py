from flask import Flask, request, Response

#************ IMPORTACIONES DE CLASES *************#
from ListaCircularDoble.ListaCircularDoble import ListaCircularDoble
from AVL.AVL import AVL
from ArbolB.ArbolB import ArbolB
#**************************************************#
app = Flask('Proyecto1_Servidor')

#************ INSTANCIAMIENTO DE CLASES ***********#
lcd = ListaCircularDoble()
avl = AVL()
aB = ArbolB()

#**************************************************#

#********** METODOS LISTA CIRCULAR DOBLE **********#
"""lcd.insertar("aom92","aom1792")
lcd.insertar("jma","jma123")
lcd.insertar("dc","dc21")
lcd.insertar("rtda","rtda127")
lcd.mostrar()
lcd.buscar("dc")
lcd.verificarUsuario("aom92", "aom1792")
lcd.graficar()
lcd.eliminar("jma")
lcd.mostrar()
lcd.graficar()"""
"""@app.route('/insertarLista',methods=['POST']) 
#@app.route('/insertarLista') 
def insertarLista():
	#parametro = str(request.args['palabra'])
	parametro = str(request.form['palabra'])
	ls.insertarFinal(str(parametro))
	ls.mostrar()
	return "Palabra insertada con exito!"	

@app.route('/buscarLista',methods=['POST']) 
#@app.route('/buscarLista') 
def buscarLista():
	#parametro = str(request.args['indice'])
	parametro = str(request.form['palabra'])
	return str(ls.buscarPalabra(str(parametro)))

@app.route('/eliminarLista',methods=['POST']) 
#@app.route('/eliminarLista') 
def eliminarLista():
	#parametro = str(request.args['indice'])
	parametro = str(request.form['indice'])
	ls.eliminarIndice(int(parametro))
	ls.mostrar()
	return "Palabra" + str(parametro) + "eliminada"  

@app.route('/graficarLista',methods=['POST']) 
#@app.route('/eliminarLista') 
def graficarLista():
	ls.graficar()
	return "Lista Graficada" """
#**************************************************#
#****************** METODOS AVL *******************#
'''avl.insertarAVL("hola","txt")
avl.insertarAVL("arbol","jpg")
avl.insertarAVL("casa","png")
avl.insertarAVL("dos","txt")
avl.enOrdenAVL()
avl.graficarAVL()
avl.buscarAVL("casa")
avl.buscarAVL("dos")
avl.buscarAVL("hola")
#avl.buscarAVL("arbol")
avl.eliminarAVL("casa","txt")
avl.graficarAVL()'''
#**************************************************#
#****************** METODOS ARBOL B *******************#
aB.ingresar("hola0")
aB.ingresar("hola1")
aB.ingresar("hola2")
aB.ingresar("hola3")
aB.ingresar("hola4")
aB.ingresar("hola5")
aB.ingresar("hola6")
aB.ingresar("hola7")
aB.graficarAB()
aB.eliminarNodo("hola7")
aB.graficarAB()
#**************************************************#
#***************** METODOS  COLA  *****************#

"""@app.route('/queueCola',methods=['POST']) 
#@app.route('/insertarLista') 
def queueCola():
	#parametro = str(request.args['palabra'])
	parametro = str(request.form['dato'])
	cl.queue(str(parametro))
	cl.mostrar()
	return "Dato insertado con exito!"	

@app.route('/dequeueCola',methods=['POST']) 
#@app.route('/eliminarLista') 
def dequeueCola():
	#parametro = str(request.args['indice'])
	parametro = str(request.form['dato'])
	resultado = cl.dequeue(str(parametro))
	cl.mostrar()
	return "Dato " + resultado + " eliminado" 

@app.route('/graficarCola',methods=['POST']) 
#@app.route('/eliminarLista') 
def graficarCola():
	cl.graficar()
	return "Cola Graficada" """
#**************************************************#

#***************** METODOS  PILA  *****************#

"""@app.route('/pushPila',methods=['POST']) 
#@app.route('/insertarLista') 
def pushPila():
	#parametro = str(request.args['palabra'])
	parametro = str(request.form['dato'])
	pl.push(str(parametro))
	pl.mostrar()
	return "Dato insertado con exito!"	

@app.route('/popPila',methods=['POST']) 
#@app.route('/eliminarLista') 
def popPila():
	#parametro = str(request.args['indice'])
	parametro = str(request.form['dato'])
	resultado = pl.pop(str(parametro))
	#pl.pop(str(parametro))
	pl.mostrar()
	return "Dato " + resultado + " eliminado" 

@app.route('/graficarPila',methods=['POST']) 
#@app.route('/eliminarLista') 
def graficarPila():
	pl.graficar()
	return "Pila Graficada" """
#**************************************************#

if __name__ == "__main__":
	print("Servidor iniciado...")
	app.run(debug=True, host='127.0.0.1')