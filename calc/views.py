from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Calculadora

PAGE_INDEX = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h2>Calculadora con Django</h2>
    <h4><p>La calculadora dispone de los siguientes operaciones:</p></h4>
    <p>- Sumar: <a href=http://127.0.0.1:{port}/suma>http://127.0.0.1:{port}/suma</a></p>
    <p>- Restar: <a href=http://127.0.0.1:{port}/resta>http://127.0.0.1:{port}/resta</a></p>
    <p>- Multiplicar: <a href=http://127.0.0.1:{port}/multi>http://127.0.0.1:{port}/multi</a></p>
    <p>- Dividir: <a href=http://127.0.0.1:{port}/div>http://127.0.0.1:{port}/div</a></p>
  </body>
</html>
"""

PAGE_INFO = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h2>Calculadora con Django</h2>
    <h4><p>Para {operacion1} puedes escribir dos alternativas:</p></h4>
    <p>1/ Con dos sumandos y sin persistencia: <br><br> http://127.0.0.1/{operacion2}/numero1/numero2<br>
    <br>2/ Con un unico sumando y con persistencia: <br><br> http://127.0.0.1/{operacion2}/numero1</p>
  </body>
</html>
"""

PAGE_SAVE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h2>Calculadora con Django</h2>
    <h4><p>Operacion: {operacion}</p></h4>
    <p>Se ha guardado el siguiente numero: {operador}</p>
  </body>
</html>
"""

PAGE_RESULT = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h2>Calculadora con Django</h2>
    <h4><p>Operacion: {operacion}</p></h4>
    <p>{numero1} {operador} {numero2} = {resultado}</p>
  </body>
</html>
"""

PAGE_ERROR = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Refresh" content="5; url=http://127.0.0.1:{port}/" />
  </head>
  <body>
    <h2>Calculadora con Django</h2>
    <h4><p>El recurso introducido no es valido. Se redigira al recurso principal.</p></h4>
  </body>
</html>
"""


def index(request):
    return HttpResponse(PAGE_INDEX.format(port=request.META['SERVER_PORT']))


def sumar_index(request):
    return HttpResponse(PAGE_INFO.format(operacion1="sumar",
                                         operacion2="suma"))


def sumar_num(request, numero):
    try:
        operation = Calculadora.objects.get(operation='suma')
        first_number = operation.operator
        operation.delete()
        return sumar(request, first_number, numero)
    except Calculadora.DoesNotExist:
        operation = Calculadora(operation='suma', operator=numero)
        operation.save()
        return HttpResponse(PAGE_SAVE.format(operacion='suma',
                                             operador=numero))


def sumar(request, numero1, numero2):
    return HttpResponse(PAGE_RESULT.format(operacion='suma',
                                           numero1=numero1,
                                           operador='+',
                                           numero2=numero2,
                                           resultado=(numero1 + numero2)))


def restar_index(request):
    return HttpResponse(PAGE_INFO.format(operacion1="restar",
                                         operacion2="resta"))


def restar_num(request, numero):
    try:
        operation = Calculadora.objects.get(operation='resta')
        first_number = operation.operator
        operation.delete()
        return restar(request, first_number, numero)
    except Calculadora.DoesNotExist:
        operation = Calculadora(operation='resta', operator=numero)
        operation.save()
        return HttpResponse(PAGE_SAVE.format(operacion='resta',
                                             operador=numero))


def restar(request, numero1, numero2):
    return HttpResponse(PAGE_RESULT.format(operacion='resta',
                                           numero1=numero1,
                                           operador='-',
                                           numero2=numero2,
                                           resultado=(numero1 - numero2)))


def multiplicar_index(request):
    return HttpResponse(PAGE_INFO.format(operacion1="multiplica",
                                         operacion2='multi'))


def multi_num(request, numero):
    try:
        operation = Calculadora.objects.get(operation='multi')
        first_number = operation.operator
        operation.delete()
        return multiplicar(request, first_number, numero)
    except Calculadora.DoesNotExist:
        operation = Calculadora(operation='multi', operator=numero)
        operation.save()
        return HttpResponse(PAGE_SAVE.format(operacion='multiplicacion',
                                             operador=numero))


def multiplicar(request, numero1, numero2):
    return HttpResponse(PAGE_RESULT.format(operacion='multiplicacion',
                                           numero1=numero1,
                                           operador='x',
                                           numero2=numero2,
                                           resultado=(numero1 * numero2)))


def dividir_index(request):
    return HttpResponse(PAGE_INFO.format(operacion1="dividir",
                                         operacion2="div"))


def div_num(request, numero):
    try:
        operation = Calculadora.objects.get(operation='div')
        first_number = operation.operator
        operation.delete()
        return dividir(request, first_number, numero)
    except Calculadora.DoesNotExist:
        operation = Calculadora(operation='div', operator=numero)
        operation.save()
        return HttpResponse(PAGE_SAVE.format(operacion='division',
                                             operador=numero))


def dividir(request, numero1, numero2):
    try:
        resultado = float(numero1) / float(numero2)
    except ZeroDivisionError:
        resultado = 'infinito'

    return HttpResponse(PAGE_RESULT.format(operacion='division',
                                           numero1=numero1,
                                           operador='/',
                                           numero2=numero2,
                                           resultado=resultado))


def error(request):
    return HttpResponseNotFound(PAGE_ERROR.format(port=request.META['SERVER_PORT']))
