from django.contrib import admin

from home.models import Customer, Invoice

    

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'invoice_no', 'trip_starting_date', 'trip_closing_date', 'total_kilometer')
    search_fields = ['invoice_no']
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['total_kilometer','service_tax', 'grand_total', 'amount_payeble_now']
        else:
            return ['total_kilometer','service_tax', 'grand_total', 'amount_payeble_now']
        return []

def get():
    data = Invoice.objects.get(id=1)
    print data

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_type', 'email_id', 'contact_no', 'remaining_balance')
    search_fields = ['name', 'customer_type', 'email_id', 'contact_no']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
