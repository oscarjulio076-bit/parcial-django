
import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

elementos = []
contador = 1

@method_decorator(csrf_exempt, name='dispatch')
class ElementoView(View):

    def get(self, request, pk=None):
        if pk:
            for elemento in elementos:
                if elemento['id'] == pk:
                    return JsonResponse(elemento)
            return JsonResponse({'error': 'No encontrado'}, status=404)

        return JsonResponse(elementos, safe=False)

    def post(self, request, pk=None):
        global contador

        try:
            datos = json.loads(request.body)
            nombre = datos.get('nombre')

            if not nombre:
                return JsonResponse({'error': 'Falta el nombre'}, status=400)

            elemento = {
                'id': contador,
                'nombre': nombre
            }

            elementos.append(elemento)
            contador += 1

            return JsonResponse(elemento, status=201)

        except (json.JSONDecodeError, AttributeError):
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    def put(self, request, pk=None):
        try:
            datos = json.loads(request.body)

            for elemento in elementos:
                if elemento['id'] == pk:
                    elemento['nombre'] = datos.get('nombre', elemento['nombre'])
                    return JsonResponse(elemento)

            return JsonResponse({'error': 'No encontrado'}, status=404)

        except (json.JSONDecodeError, AttributeError):
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    def delete(self, request, pk=None):
        for elemento in elementos:
            if elemento['id'] == pk:
                elementos.remove(elemento)
                return JsonResponse({'mensaje': 'Elemento eliminado'})

        return JsonResponse({'error': 'No encontrado'}, status=404)
