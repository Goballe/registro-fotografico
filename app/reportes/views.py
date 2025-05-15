from django.shortcuts import render, redirect
from .forms import ReporteForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import ReporteFotografico
import tempfile

def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save()
            return redirect('reporte_pdf', reporte_id=reporte.id)
    else:
        form = ReporteForm()
    return render(request, 'reportes/crear_reporte.html', {'form': form})

def lista_reportes(request):
    reportes = ReporteFotografico.objects.all().order_by('-fecha_emision')
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})

import io

def reporte_pdf(request, reporte_id):
    reporte = ReporteFotografico.objects.get(id=reporte_id)

    # Renderizar la plantilla HTML con datos del reporte
    # Preparar rutas de imágenes con slashes para Windows
    foto1_path_fixed = reporte.foto1.path.replace('\\', '/') if reporte.foto1 else ''
    foto2_path_fixed = reporte.foto2.path.replace('\\', '/') if reporte.foto2 else ''
    foto3_path_fixed = reporte.foto3.path.replace('\\', '/') if reporte.foto3 else ''
    foto4_path_fixed = reporte.foto4.path.replace('\\', '/') if reporte.foto4 else ''

    from django.utils import translation

    # Forzar idioma español en la generación del PDF
    with translation.override('es'):
        context = {
            'reporte': reporte,
            'foto1_path_fixed': foto1_path_fixed,
            'foto2_path_fixed': foto2_path_fixed,
            'foto3_path_fixed': foto3_path_fixed,
            'foto4_path_fixed': foto4_path_fixed,
        }
        html_string = render_to_string('reportes/reporte_pdf.html', context)

        # Generar el PDF en memoria
        pdf_io = io.BytesIO()
        HTML(string=html_string).write_pdf(target=pdf_io)
        pdf_io.seek(0)
        pdf = pdf_io.read()

        # Enviar el PDF como respuesta
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'filename="reporte_{reporte.id}.pdf"'
        return response
    html_string = render_to_string('reportes/reporte_pdf.html', context)

    # Generar el PDF en memoria
    pdf_io = io.BytesIO()
    HTML(string=html_string).write_pdf(target=pdf_io)
    pdf_io.seek(0)
    pdf = pdf_io.read()

    # Enviar el PDF como respuesta
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="reporte_{reporte.id}.pdf"'
    return response