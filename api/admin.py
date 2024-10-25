from django.contrib import admin
from .models import Clinica, Doctor, Favorito, Cita

@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'numero_telefono')
    search_fields = ('nombre', 'direccion')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'clinica')
    search_fields = ('nombre', 'especialidad')
    list_filter = ('clinica',)

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'doctor')
    list_filter = ('usuario',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'doctor', 'horario')
    list_filter = ('usuario', 'doctor')

