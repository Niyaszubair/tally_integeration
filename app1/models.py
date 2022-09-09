from django.db import models

# Create your models here.

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)

class CreateStockGrp(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)
    
class CreateStockCateg(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class UnitCrt(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    type=models.CharField(max_length=100,null=True)
    symbol=models.CharField(max_length=20,null=True)
    formal_name=models.CharField(max_length=50,null=True)

class stock_item_crt(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    additional=models.CharField(max_length=100,null=True)
    gst=models.CharField(max_length=100,default="")
    supply=models.CharField(max_length=100,default="")
    rduty=models.CharField(max_length=100,default="")

class CreateGodown(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class analysis_view(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    particular=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    iquantity=models.IntegerField(null=True)
    ieff_rate=models.IntegerField(null=True)
    ivalue=models.IntegerField(null=True)
    oquantity=models.IntegerField(null=True)
    oeff_rate=models.IntegerField(null=True)
    ovalue=models.IntegerField(null=True)

class purchase_model(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

class sale_model(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    itm=models.ForeignKey(stock_item_crt,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

# noufal

class countrymodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

class statemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    cname=models.ForeignKey(countrymodel,on_delete=models.CASCADE)
    sname=models.CharField(max_length=250)

class groupcreatemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    gname=models.CharField(max_length=250)
    galias=models.CharField(max_length=250)
    gunder=models.CharField(max_length=250)
    gbehaves=models.CharField(max_length=250)
    gallocate=models.CharField(max_length=250)

class groupanalysismodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    pert=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    perticular=models.CharField(max_length=250)
    pquatity=models.IntegerField()
    prate=models.IntegerField()
    pvalue=models.IntegerField()
    squatity=models.IntegerField()
    srate=models.IntegerField()
    svalue=models.IntegerField()

class purchasevouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()

class salevouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    stockitem=models.ForeignKey(groupanalysismodel,on_delete=models.CASCADE)
    udergroup=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=250)
    quantity=models.IntegerField()
    basicrate=models.IntegerField()
    basicvalue=models.IntegerField()
    addlcost=models.IntegerField()
    totalvalue=models.IntegerField()
    efsrate=models.IntegerField()

class ledgercreatemodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lname=models.CharField(max_length=250)
    lalias=models.CharField(max_length=250)
    # lunder=models.ForeignKey(groupcreatemodel,on_delete=models.CASCADE)
    lunder=models.CharField(max_length=250)
    lmname=models.CharField(max_length=250)
    laddress=models.CharField(max_length=250)
    lstate=models.CharField(max_length=250)
    lcountry=models.CharField(max_length=250)
    lpincode=models.CharField(max_length=250)
    lbank=models.CharField(max_length=250)
    lpan=models.CharField(max_length=250)
    lreg=models.CharField(max_length=250)

class ledgeranalysismodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lpert=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    lperticular=models.CharField(max_length=250)
    lpquatity=models.IntegerField()
    lprate=models.IntegerField()
    lpvalue=models.IntegerField()
    lsquatity=models.IntegerField()
    lsrate=models.IntegerField()
    svalue=models.IntegerField()

class purchaseledgervouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()

class salesledgervouchermodel(models.Model):
    comp=models.ForeignKey(Companies,on_delete=models.CASCADE)
    lstockitem=models.ForeignKey(ledgeranalysismodel,on_delete=models.CASCADE)
    ludergroup=models.ForeignKey(ledgercreatemodel,on_delete=models.CASCADE)
    ldate=models.DateField(auto_now_add=True)
    # lperticular=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    lquantity=models.IntegerField()
    lbasicrate=models.IntegerField()
    lbasicvalue=models.IntegerField()
    laddlcost=models.IntegerField()
    ltotalvalue=models.IntegerField()
    lefsrate=models.IntegerField()