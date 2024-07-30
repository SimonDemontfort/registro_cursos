from django.shortcuts import render, HttpResponse
from main.services import *
# Create your views here.
def test(req):
   crear_curso('CIN', 'Computación e Informatica', 6)
   crear_profesor('114231-1', 'Aramis', 'Loza')
   crear_estudiante('134457-8', 'Andrea', 'Ramirez', '2006-02-15')
   crear_direccion('AV.Condell','342','Quillota','v','8788346-2')
   agregar_curso_a_estudiante('GIN', '1238765-8')
   agregar_profesor_a_curso('113231-1', 'AGR')
   return HttpResponse('Estamos OK!!!')