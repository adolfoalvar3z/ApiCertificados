from django.contrib import admin
from .models import Respuesta
from .models import Certificado
from .models import Pregunta

# Register your models here.
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_respuesta', 'respuesta', 'pregunta')
    readonly_fields = ('respuesta', 'pregunta', 'user', 'fecha_respuesta')
    pass


class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_certificado')
    readonly_fields = ('user', 'fecha_certificado')
    pass


class PreguntaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
