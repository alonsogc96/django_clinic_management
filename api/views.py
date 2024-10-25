from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Clinica, Doctor, Favorito, Cita, CustomUser
from .serializers import ClinicaSerializer, DoctorSerializer, FavoritoSerializer, CitaSerializer, UserRegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega los datos adicionales al token
        token['username'] = user.username
        token['tipo_documento'] = user.tipo_documento
        token['numero_documento'] = user.numero_documento

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    # Puedes personalizar el comportamiento aquí si es necesario
    pass

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ClinicaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer

class ClinicaCreateView(generics.CreateAPIView):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes agregar lógica adicional, como asociar la clínica al usuario si es necesario
        serializer.save()

class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorListByClinicaView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        clinica_id = self.kwargs['clinica_id']
        return Doctor.objects.filter(clinica_id=clinica_id)

class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes agregar lógica adicional, como asociar la clínica al usuario si es necesario
        serializer.save()

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class FavoritoCreateView(generics.CreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class FavoritoListView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtén los favoritos del usuario autenticado
        return Doctor.objects.filter(favorito__usuario=self.request.user)

class CitaViewSet(viewsets.ModelViewSet):

    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaCreateView(generics.CreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CitaListView(generics.ListAPIView):
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra las citas por el usuario autenticado
        return Cita.objects.filter(usuario=self.request.user)