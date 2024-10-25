from rest_framework import serializers
from .models import Clinica, Doctor, Favorito, Cita, CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'tipo_documento', 'numero_documento', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'tipo_documento', 'numero_documento']

class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_clinica(self, value):
        if not Clinica.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La clínica no existe.")
        return value

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['doctor']  # Solo incluye 'doctor'
        read_only_fields = ['usuario']  # Solo de lectura

    def create(self, validated_data):
        print("Validated Data (before):", validated_data)  # Para depurar
        usuario = self.context['request'].user
        
        # Aquí verificamos que no se esté pasando 'usuario' en validated_data
        if 'usuario' in validated_data:
            validated_data.pop('usuario')  # Eliminar usuario si está presente

        # Crear el objeto Favorito
        favorito = Favorito(usuario=usuario, **validated_data)
        favorito.save()
        return favorito

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['doctor', 'horario']

    def create(self, validated_data):
        usuario = self.context['request'].user
        validated_data.pop('usuario', None)
        return Cita.objects.create(usuario=usuario, **validated_data)

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['doctor'] = {
            'id': instance.doctor.id,
            'nombre': instance.doctor.nombre,
            'especialidad': instance.doctor.especialidad,
        }
        return representation