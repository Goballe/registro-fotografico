from django.db import models

class ReporteFotografico(models.Model):
    proyecto = models.CharField("Proyecto", max_length=200)
    cliente = models.CharField("Cliente", max_length=200)
    contratista = models.CharField("Contratista", max_length=200)
    codigo_proyecto = models.CharField("Código del proyecto", max_length=50)
    version_reporte = models.CharField("Versión del reporte", max_length=10)
    fecha_emision = models.DateField("Fecha de emisión")
    elaborado_por = models.CharField("Elaborado por", max_length=100)
    revisado_por = models.CharField("Revisado por", max_length=100)
    inicio_supervision = models.DateField("Inicio de la Supervisión")
    mes_actual_obra = models.PositiveIntegerField("Mes Actual de Obra")
    reporte_numero = models.PositiveIntegerField("Reporte N°")
    descripcion = models.TextField("Descripción", blank=True, null=True)

    foto1 = models.ImageField("Fotografía 01", upload_to='fotos/', blank=True, null=True)
    foto2 = models.ImageField("Fotografía 02", upload_to='fotos/', blank=True, null=True)
    foto3 = models.ImageField("Fotografía 03", upload_to='fotos/', blank=True, null=True)
    foto4 = models.ImageField("Fotografía 04", upload_to='fotos/', blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.proyecto} - {self.fecha_emision}'