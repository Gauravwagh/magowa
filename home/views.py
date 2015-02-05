from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string

from home.models import Invoice, Customer

@login_required(login_url='/accounts/login/')
def home(requests):
    invoice_list = Invoice.objects.all().order_by('-date')
    return render(requests,'home/home.html', {'invoice_list':invoice_list})

@csrf_exempt
def invoice_generate(request, invid):
    invoice = Invoice.objects.get(id=int(invid))
    invoice.grand_total = float(invoice.pure_amount) + float(invoice.extra_charge)+float(invoice.driver_allownce_charge)+float(invoice.night_hault_charge)+float(invoice.service_tax)+float(invoice.toll_and_parking)
    print invoice.grand_total
    invoice.amount_payeble_now = float(invoice.grand_total)-float(invoice.less_adavance)
    invoice.save()
    html = render_to_string('home/generate_invoice.html',{'invoice':invoice })
    return HttpResponse(html)

@login_required(login_url='/accounts/login/')
def customers(requests):
    customer_list = Customer.objects.all().order_by('-name')
    return render(requests,'home/customer.html', {'customer_list':customer_list})


from reportlab.pdfgen import canvas
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


    