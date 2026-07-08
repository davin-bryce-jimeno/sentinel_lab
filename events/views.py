# Create your views here.

from rest_framework import viewsets
from .models import LoginEvent
from .serializers import LoginEventSerializer

class LoginEventViewSet(viewsets.ModelViewSet):
    queryset = LoginEvent.objects.all()
    serializer_class = LoginEventSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        status_param = self.request.query_params.get("status")
        if status_param:
            qs = qs.filter(status=status_param.upper())
        return qs
