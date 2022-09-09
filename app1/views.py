import datetime
import random
from tally_session.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from calendar import month
from urllib import response
from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from errno import ETIME
from datetime import date
from re import S
from re import A, S
from this import s
from unittest import signals
from webbrowser import get
from django.db.models.functions import Coalesce
from xml.etree.ElementTree import tostring
from django.db.models import Sum
from cgi import print_arguments
from multiprocessing import context
from symtable import Symbol
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models.functions import Extract
from django.db.models import Count
from unittest import TextTestRunner

# Create your views here.

def index1(request):
    comp=Companies.objects.all()
    return render(request,'index1.html',{'comp':comp})

def createcompany(request):
    # st=States.objects.all()
    # country=Countries.objects.all()
    return render(request,'createcompany.html')

def companycreate(request):
    if request.method=='POST':
        n=Companies()
        n.name=request.POST['companyname']
        b=Companies.objects.filter(name=n.name)
        if b:
            messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        n.mailing_name=request.POST['mailing_name']
        n.address=request.POST['address']
        n.state=request.POST['state']
        n.country=request.POST['country']
        n.pincode=request.POST['pincode']
        n.telephone=request.POST['telephone']
        n.mobile=request.POST['mobile']
        n.fax=request.POST['fax']
        n.email=request.POST['email']
        n.website=request.POST['website']
        n.fin_begin=request.POST['fyear']
        n.books_begin=request.POST['byear']
        n.currency_symbol=request.POST['currency']
        n.formal_name=request.POST['formal']
        n.password=random.randint(10000, 99999)
        out=datetime.strptime (n.fin_begin,'%Y-%m-%d')+timedelta (days=364) 
        n.fin_end=out.date()
        n.save()
        subject = 'Welcome Tally Prime'
        message = 'Congratulations,\n' \
        'You have successfully registered with our website.\n' \
        'username :'+str(n.email)+'\n' 'password :'+str(n.password) + \
        '\n' 'WELCOME '
        recepient = str(n.email)
        send_mail(subject, message, EMAIL_HOST_USER,
                [recepient], fail_silently=False)
        msg_success = "Registration successfully Check Your Registered Mail"
        messages.info(request,'Company created successfully(Enable the features as per your business needs)')
        return render(request,'features.html',{'cmp':n,'msg_success':msg_success})
    
    return render(request,'features.html')

def login(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        # user = authenticate(username=email,password=password)
        # if user is not None:
        #     request.session['SAdm_id'] = user.id
        #     return redirect( 'Admin_dashboard')

        if Companies.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
                
                member=Companies.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['t_id'] = member.id 
                tally=Companies.objects.filter(id= member.id)
                
                return render(request,'base.html',{'tally':tally})
    
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'Login.html', context)

    return render(request, 'Login.html')

def logout(request):
    if 't_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def base(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        return render(request, 'base.html',{'tally':tally})
    return redirect("/")

def stock_group(request):
    und=CreateStockGrp.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            # company=Companies.objects.get(id=request.companycreate)
            company=Companies.objects.get(id=t_id)
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            quantities=request.POST['quantities']
            stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities,comp=company)
            stockgrp.save()
            return redirect('stock_group')
        return render(request,'stock_group.html',{'und':und})
    return redirect("/")

def stock_group_secondary(request):
    # company=Companies.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            und=CreateStockGrp.objects.filter(comp=t_id)
        else:
            return redirect('/')
        if request.method=='POST':
            
            # company=Companies.objects.get(id=request.companycreate)
            company=Companies.objects.get(id=t_id)
            name=request.POST['name']
            alias=request.POST['alias']
            under_name=request.POST['under_name']
            quantities=request.POST['quantities']
            stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities,comp=company)
            stockgrp.save()
            return redirect('stock_group')
        return render(request,'stock_group(secondary).html',{'und':und})
    return redirect("/")

def unit_creation(request):
    unit=UnitCrt.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            type=request.POST['type']
            symbol=request.POST['symbol']
            formal_name=request.POST['formal_name']
            crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,comp=company)
            crt.save()
        return render(request,'unit1.html',{'unit':unit})
    return redirect("/")

def unit_creation_secondary(request):
    unit=UnitCrt.objects.all()
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            type=request.POST['type']
            symbol=request.POST['symbol']
            formal_name=request.POST['formal_name']
            crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,comp=company)
            crt.save()
        return render(request,'unit_creation(secondary).html',{'unit':unit})
    return redirect("/")

def createcategory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cat=CreateStockCateg.objects.filter(id=t_id)
        con={'cat':cat} 
        return render(request, 'createcategory.html',con) 
    return redirect("/")

def savestockcategory(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        if request.method=='POST':
            company=Companies.objects.get(id=t_id)
            catname=request.POST['name']
            abr=request.POST['alias']
            cat=request.POST.get('u')
            sc=CreateStockCateg(name=catname,alias=abr,under_name=cat,comp=company)
            sc.save()
        return redirect('catgroupsummary')
    return redirect("/")

def catgroupsummary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            cat=CreateStockCateg.objects.filter(id=t_id)
        else:
            return redirect('/')
        # cat=CreateStockCateg.objects.filter(id=t_id)
        con={'cat':cat} 
        return render(request,'catgroupsummary.html',con)
    return redirect("/")

def liststockgroupviews(request):
    if request.session.has_key('t_id'):
        t_id = request.session['t_id']
        data=CreateStockGrp.objects.filter(comp=t_id)
    else:
        return redirect('/')
    context={'data':data}
    return render(request, 'liststockgroup.html',context)

def stock_items(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        cat=CreateStockCateg.objects.filter(id=t_id)
        # cat=CreateStockCateg.objects.all()
        grp=CreateStockGrp.objects.filter(id=t_id)
        unt=UnitCrt.objects.filter(id=t_id)
        company=Companies.objects.get(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        category=request.POST['category']
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=stock_item_crt(name=name,alias=alias,under=under,category=category,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional,comp=company)
        crt.save()
    return render(request,'stock_items.html',{'cat':cat,'grp':grp,'unt':unt})

def liststockviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            data=stock_item_crt.objects.filter(comp=t_id)
        else:
            return redirect('/')
        # data1=stock_item_crt.objects.all()
        context={'data':data}
        return render(request, 'liststock.html',context)
    return redirect("/")

def godown_secondary(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            gd=stock_item_crt.objects.filter(comp=t_id)
        else:
            return redirect('/')
        # gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        company=Companies.objects.get(id=t_id)   
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name,comp=company)
        gdcrt.save()
    return render(request,'godown(secondary).html',{'gd':gd})

def singlestockgroupanalysisview(request,pk):
    data1=CreateStockGrp.objects.get(id=pk)
    itm=data1.name
    data2=stock_item_crt.objects.get(under = itm)
    data=analysis_view.objects.filter(particular=data2)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    for a in data:
        sum1 += a.iquantity
    for b in data:
        sum2 += b.ieff_rate
    for c in data:
        sum3 += c.ivalue
    for d in data:
        sum4 += d.oquantity
    for e in data:
        sum5 += e.oeff_rate
    for f in data:
        sum6 += f.ovalue
    context={'data':data,'data1':data1,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
    return render(request, 'singlestockgroupanalysis.html',context)

def itemmovementanalysisview(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            data1=purchase_model.objects.filter(comp=t_id)
            data2=sale_model.objects.filter(comp=t_id)
        else:
            return redirect('/')
        # data1=purchase_model.objects.all()
        # data2=sale_model.objects.all()
        context={'data1':data1,'data2':data2}
        return render(request, 'itemmovementanalysis.html',context)
    return redirect("/")

def purchasevoucheranalysisview(request,pk):
    data=purchase_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'purchasevoucheranalysis.html',context)

def salevoucheranalysisview(request,pk):
    data=sale_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'salevoucheranalysis.html',context)

def querystockview(request,pk):
    data=stock_item_crt.objects.get(id=pk)
    ndata=CreateGodown.objects.all()
    # ndata=CreateGodown.objects.filter(under_name=data)
    
    # if data == nddata == ndata:
    total_sum = 0
    # for item in ndata:
    #     total_sum += item.itm.quantity
    # sums=CreateGodown.objects.filter(ndata).sum()
    # purchase=purchase_model.objects.all()
    purchase=purchase_model.objects.filter(itm=data)
    # sale=sale_model.objects.all()
    sale=sale_model.objects.filter(itm=data)
    # cat=CreateStockCateg.objects.all()
    cat=CreateStockCateg.objects.filter(name=data)    
    context={'data':data,'ndata':ndata,'purchase':purchase,'sale':sale,'cat':cat}
    return render(request, 'querystocks.html',context)

def stockgroupanalysisview(request):
    data=analysis_view.objects.all()
    # var1=analysis_view.objects.get(ivalue)
    # list1=list(var1)
    # sums=sum(list1)
    # for ivalue in data:
    #     list1=sum(ivalue)
    #     print(list1)
    # sums=analysis_view.objects.aggregate(Sum('ivalue'))
    # ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
    sum1 = 0
    sum2 = 0
    for a in data:
        sum1 += a.ivalue
    for b in data:
        sum2 += b.ovalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request, 'stockgroupanalysis.html',context)

# noufal

def grouppage(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            data=groupcreatemodel.objects.filter(comp=t_id)
            # data1=purchase_model.objects.filter(comp=t_id)
            # data2=sale_model.objects.filter(comp=t_id)
        else:
            return redirect('/')
    # data=groupcreatemodel.objects.all()
    context={'data':data}
    return render(request,'selectgroup.html',context)

def creategroup(request):
    data=groupcreatemodel.objects.all()
    context={'data':data}
    return render(request,'groupcreate.html',context)

def creategroupviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            gd=stock_item_crt.objects.filter(comp=t_id)
        else:
            return redirect('/')
    if request.method=='POST':
        gpname=request.POST['name']
        gpalias=request.POST['alias']
        gpunder=request.POST['under']
        gpbehaves=request.POST['behaves']
        gpallocate=request.POST['allocate']
        company=Companies.objects.get(id=t_id)  
        data=groupcreatemodel(gname=gpname,galias=gpalias,gunder=gpunder,gbehaves=gpbehaves,gallocate=gpallocate,comp=company)
        data.save()
        return redirect('grouppage')

def groupanalisys(request,pk):
    ndata=groupcreatemodel.objects.get(id=pk)
    data=groupanalysismodel.objects.filter(pert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.pvalue
    for b in data:
        sum2+=b.svalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request,'groupanalisys.html',context)

def groupitem(request,pk):
    ndata=groupanalysismodel.objects.get(id=pk)
    data=purchasevouchermodel.objects.filter(stockitem=ndata)
    sdata=salevouchermodel.objects.filter(stockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.quantity
    for b in data:
        sum2+=b.basicrate
    for c in data:
        sum3+=c.basicvalue
    for d in data:
        sum4+=d.addlcost
    for e in data:
        sum5+=e.totalvalue
    for f in data:
        sum6+=f.efsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.quantity
    for h in sdata:
        sum8+=h.basicrate
    for i in sdata:
        sum9+=i.basicvalue
    for j in sdata:
        sum10+=j.addlcost
    for k in sdata:
        sum11+=k.totalvalue
    for l in sdata:
        sum12+=l.efsrate
    return render(request,'groupitem.html',{'data':data,'ndata':ndata,'sdata':sdata,
                                            'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,
                                            'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,
                                            'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})

def ledgercreate(request):
    data=ledgercreatemodel.objects.all()
    cnt=countrymodel.objects.all()
    st=statemodel.objects.all()
    context={'data':data,'cnt':cnt,'st':st}
    return render(request,'ledgercreate.html',context)

def createledgerviews(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
    if request.method=='POST':
        lpname=request.POST['name']
        lpalias=request.POST['alias']
        lpunder=request.POST['under']
        # under=groupcreatemodel.objects.get(id=lpunder)
        lpmname=request.POST['mname']
        lpaddress=request.POST['address']
        lpstate=request.POST['state']
        lpcountry=request.POST['contry']
        lppincode=request.POST['pincode']
        lpbank=request.POST['bank']
        lppan=request.POST['pan']
        lpreg=request.POST['registrations']
        company=Companies.objects.get(id=t_id) 
        data=ledgercreatemodel(lname=lpname,lalias=lpalias,
                                lunder=lpunder,lmname=lpmname,
                                laddress=lpaddress,lstate=lpstate,
                                lcountry=lpcountry,lpincode=lppincode,
                                lbank=lpbank,lpan=lppan,lreg=lpreg,comp=company)
        data.save()
        return redirect('ledgercreate')

def selectledgerpage(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
            data=ledgercreatemodel.objects.filter(comp=t_id)
        else:
            return redirect('/')
    # data=ledgercreatemodel.objects.all()
    context={'data':data}
    return render(request,'selectledger.html',context)

def ledgerpage(request,pk):
    ndata=ledgercreatemodel.objects.get(id=pk)
    data=ledgeranalysismodel.objects.filter(lpert=ndata)
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.lpvalue
    for b in data:
        sum2+=b.svalue
    return render(request,'ledgeranalisys.html',{'data':data,'sum1':sum1,'sum2':sum2})


def ledgeritem(request,pk):
    ndata=ledgeranalysismodel.objects.get(id=pk)
    data=purchaseledgervouchermodel.objects.filter(lstockitem=ndata)
    sdata=salesledgervouchermodel.objects.filter(lstockitem=ndata)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    for a in data:
        sum1+=a.lquantity
    for b in data:
        sum2+=b.lbasicrate
    for c in data:
        sum3+=c.lbasicvalue
    for d in data:
        sum4+=d.laddlcost
    for e in data:
        sum5+=e.ltotalvalue
    for f in data:
        sum6+=f.lefsrate
    sum7=0
    sum8=0
    sum9=0
    sum10=0
    sum11=0
    sum12=0
    for g in sdata:
        sum7+=g.lquantity
    for h in sdata:
        sum8+=h.lbasicrate
    for i in sdata:
        sum9+=i.lbasicvalue
    for j in sdata:
        sum10+=j.laddlcost
    for k in sdata:
        sum11+=k.ltotalvalue
    for l in sdata:
        sum12+=l.lefsrate
    return render(request,'ledgeritem.html',{'data':data,'ndata':ndata,'sdata':sdata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6,'sum7':sum7,'sum8':sum8,'sum9':sum9,'sum10':sum10,'sum11':sum11,'sum12':sum12})
