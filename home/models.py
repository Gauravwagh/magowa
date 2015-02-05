from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
#from durationfield.db.models.fields.duration import DurationField
from sorl.thumbnail import ImageField
import string,random,datetime
# Create your models here.

def get_photo_storage_path(photo_obj, filename):     
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        storage_path = 'img/' + random_string + '_' + filename
        return storage_path

def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'ME0001'
    invoice_no = last_invoice.invoice_no
    #print invoice_no
    invoice_int = int(invoice_no.split('ME')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'ME' + str(formatted)
    return new_invoice_no 

class Invoice(models.Model):
    invoice_no = models.CharField(max_length = 500, default = increment_invoice_number, null = True, blank = True)
    name = models.CharField(max_length=300, null=True, blank=True)
    pax_name = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    booked_by = models.CharField(max_length=300, null=True, blank=True)
    vehical_type = models.CharField(max_length=300, null=True, blank=True)
    journy = models.CharField(max_length=300, null=True, blank=True)
    contact_no = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    vehical_no = models.CharField(max_length=500, null=True, blank=True, validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',message='Username must be Alphanumeric',code='invalid_username'),])
    invoice_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    chaffeur = models.CharField(max_length=300, null=True, blank=True)
    starting_kilometer=models.IntegerField(null=True, blank=True)
    ending_kilometer=models.IntegerField(null=True, blank=True)
    total_kilometer = models.IntegerField(null=True, blank=True)
    extra_kilometers = models.IntegerField(null=True, blank=True)
    per_kilometer_charge = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    extra_charge = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    driver_allownce_charge = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    night_hault_charge = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    starting_time = models.CharField(max_length=500, null=True, blank=True)
    closing_time = models.CharField(max_length=500, null=True, blank=True)
    trip_starting_date = models.DateTimeField(null=True, blank=True)
    trip_closing_date = models.DateTimeField(null=True, blank=True)
    total_trip_days = models.IntegerField(null=True, blank=True)
    pure_amount = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    toll_and_parking = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    service_tax = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    less_adavance = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    amount_payeble_now = models.DecimalField(max_digits=10,decimal_places=3, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #duration = DurationField()
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.total_kilometer:
            self.total_kilometer = self.ending_kilometer - self.starting_kilometer
        
        if not self.grand_total:
            self.grand_total = self.pure_amount + self.extra_charge + self.driver_allownce_charge + self.night_hault_charge + self.toll_and_parking
        if not self.service_tax:
            minivl  = float(self.pure_amount) + float(self.extra_charge) + float(self.driver_allownce_charge) + float(self.night_hault_charge)
            tax = float(minivl*4.444)
            self.service_tax = float(tax/100)   
        if not self.amount_payeble_now:
            self.amount_payeble_now = (self.pure_amount + self.extra_charge + self.driver_allownce_charge + self.night_hault_charge + self.toll_and_parking)-self.less_adavance
        return super(Invoice, self).save(*args, **kwargs)
    
    
class Customer(models.Model):
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    customer_type_choice = (
        ('Personal Customer', 'Personal Customer'),
        ('Company Customer', 'Company Customer'),
        ('Vendor', 'Vendor'),
    )
    name= models.CharField(max_length=500, null=True, blank=True)
    customer_type = models.CharField(max_length=1000, choices=customer_type_choice)
    email_id = models.EmailField(null=True, blank=True)
    address= models.CharField(max_length=500, null=True, blank=True)
    gender=models.CharField(max_length=1, choices=gender_choice)
    contact_no=models.BigIntegerField(null=True, blank=True)
    remaining_balance=models.IntegerField(null=True, blank=True)
    image=models.ImageField(upload_to=get_photo_storage_path)
    def __str__(self):
        return self.name

