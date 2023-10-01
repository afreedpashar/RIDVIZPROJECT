from rest_framework import viewsets
from .models import Invoice, InvoiceDetails
from .serializers import InvoiceSerializer,InvoiceDetailsSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
    