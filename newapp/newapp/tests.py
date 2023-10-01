from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetails



class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'date': '2023-09-01',
            'customer_name': 'Test Customer',
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_list(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_invoice(self):
        invoice = Invoice.objects.create(date='2023-09-02', customer_name='Another Customer')
        response = self.client.get(f'/invoices/{invoice.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        invoice = Invoice.objects.create(date='2023-09-03', customer_name='Initial Customer')
        updated_data = {'date': '2023-09-04', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/invoices/{invoice.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Invoice.objects.get(pk=invoice.pk).customer_name, 'Updated Customer')

    def test_delete_invoice(self):
        invoice = Invoice.objects.create(date='2023-09-05', customer_name='Delete Customer')
        response = self.client.delete(f'/invoices/{invoice.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

