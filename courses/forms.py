from django import forms 
from django.forms.models import inlineformset_factory 
from .models import Course, Module


#Essa função permite criar um formset de modelo para os objetos #Module relacionados a um objeto Course, dinamicamente.


ModuleFormSet = inlineformset_factory(Course, Module, fields = ['title','description'],
extra=2, #permite definir o número de formulários extras vazios para exibir no formset.
can_delete=True)#se for definido com True, Django incluirá um campo booleano para cada formulário que será renderizado, na forma de uma caixa de seleção.


# ***NOVO CAPITULO RENDERIZANDO E FAZENDO CACHING DE CONTEUDO*** 

