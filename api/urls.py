from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, ClinicaViewSet, DoctorViewSet, DoctorCreateView, DoctorListByClinicaView, FavoritoViewSet, FavoritoCreateView, FavoritoListView, CitaViewSet, CustomTokenObtainPairView, TokenRefreshView, UserRegisterView, ClinicaCreateView, CitaCreateView, CitaListView

router = DefaultRouter()
router.register(r'clinicas', ClinicaViewSet)
router.register(r'doctores', DoctorViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('usuario/registrar/', UserRegisterView.as_view(), name='registrar-usuario'),
    path('usuario/perfil/', UserProfileView.as_view(), name='ver-usuario'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clinicas/crear/',ClinicaCreateView.as_view(), name='crear-clinica'),
    path('doctores/registrar', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctores/clinica/<int:clinica_id>/', DoctorListByClinicaView.as_view(), name='doctores-por-clinica'),
    path('favoritos/agregar/', FavoritoCreateView.as_view(), name='agregar-favorito'),
    path('favoritos/usuario/', FavoritoListView.as_view(), name='listar-favoritos'),
    path('citas/registrar/', CitaCreateView.as_view(), name='registrar-cita'),
    path('citas/usuario/', CitaListView.as_view(), name='listar-citas'),
    path('', include(router.urls)),
]