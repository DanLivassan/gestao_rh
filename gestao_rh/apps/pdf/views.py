from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
import io


class PdfListFuncionario(View):

    def get(self, request):
        params = {
            'nome': 'Danilo Santana',
            'empresa': 'DaniloXcode',
            'data': '24/07/2020 - 21:30',
            'horas_extra': [
                dict({'motivo': 'Partida do óico', 'horas': 10.0}),
                dict({'motivo': 'Parada do NBA', 'horas': 62.0})
            ],
            'departamentos': '',
            'request': request,
        }
        return Render.render('funcionarios/report_list.html', params, 'myfile')


class Render:

    @staticmethod
    def render(path: str, params:dict, filename:str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response
        )

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(),
                content_type="application/pdf"
            )

            #response['Content-Disposition'] = "attachment;filename=%s.pdf" % filename
            return response
        else:
            return HttpResponse("Error rendering the pdf", status=400)