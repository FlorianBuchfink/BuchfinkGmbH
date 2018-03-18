from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from Website.models import EmailForm, BewerbungForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages





def Mainpage(request):
    return render(request, "Mainpage.html")
    
def Heizungstausch(request):
    return render(request, "Heizungstausch.html")

def Neubausanierung(request):
    return render(request, "NeubauSanierung.html")

def Badsanierung(request):
    return render(request, "Badsanierung.html") 

def Lueftung(request):
    return render(request, "Lueftung.html")    

def Spenglerei(request):
    return render(request, "Spenglerei.html")

def Pool(request):
    return render(request, "Pools.html")

def Anfahrt(request):
    return render(request, "Anfahrt.html")

def Oeffnungszeiten(request):
    return render(request, "Oeffnungszeiten.html")  

def Kontakt(request):
    return render(request, "Kontakt.html")  

def Firmengeschichte(request):
    return render(request, "Firmengeschichte.html")

def Kontaktformular(request): 
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid(): 
            firstname = form.cleaned_data['firstname']
            messageHidden = form.cleaned_data['messageHidden']
            lastname = form.cleaned_data['lastname']
            streetname = form.cleaned_data['streetname']
            plz = form.cleaned_data['plz']
            ort = form.cleaned_data['ort']
            telefon = form.cleaned_data['telefon']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            botcheck = form.cleaned_data['botcheck'].lower()
            message = form.cleaned_data['message']
            if botcheck == 'yes':
                try:
                    subject, from_email, to = subject, firstname + " " + lastname, 'florian@buchfink.de'
                    text_content = ''
                    html_content = '<span>'+'Eine neue Anfrage über Buchfink.de:'+' '+'</br>'+'</br>'+'<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+'</br>'+ '<strong>Kontaktdaten:</strong>'+' '+'</br>'+firstname +' '+ lastname + " "+ '</br>'+ streetname + '</br>' + plz + '</br>'+ ort + '</br>' + telefon + '</br>'+email + '</br>'+ '<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+ '</br>' +'</br>' +'Folgendes wurde ausgewählt: '+'</br'+'</br>'+messageHidden +'</br>'+ '<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+'</br><strong>'+ 'Nachricht von ' + firstname + ' ' + lastname +':</strong>'+ '</br>' + '</br>' +message +'</br>'+ '</span'
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    return HttpResponseRedirect('DankeAnfrage')
                except:
                    messages.warning(request, 'Bitte alle Felder vollständig ausfüllen')
            else:
                messages.warning(request, "Bitte alle Felder vollständig ausfüllen")
        else:
            messages.warning(request, "Bitte alle Felder vollständig ausfüllen")
            
    return render(request, "Kontaktformular.html")


def Danke(request):
    return render(request, "danke.html")

def Mitarbeiter(request):
    if request.method == 'POST':
        form = BewerbungForm(request.POST)
        if form.is_valid(): 
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            streetname = form.cleaned_data['streetname']
            plz = form.cleaned_data['plz']
            ort = form.cleaned_data['ort']
            telefon = form.cleaned_data['telefon']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            botcheck = form.cleaned_data['botcheck'].lower()
            message = form.cleaned_data['message']
            if botcheck == 'yes':
                try:
                    subject, from_email, to = subject, firstname + " " + lastname, 'florian@buchfink.de'
                    text_content = ''
                    html_content = '<span>'+'Eine neue Anfrage über Buchfink.de:'+' '+'</br>'+'</br>'+'<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+'</br>'+ '<strong>Kontaktdaten:</strong>'+' '+'</br>'+firstname +' '+ lastname + " "+ '</br>'+ streetname + '</br>' + plz + '</br>'+ ort + '</br>' + telefon + '</br>'+email + '</br>'+ '<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+ '</br>' +'</br><strong>' +'Folgendes wurde ausgewählt: '+ '</strong></br>'+ subject +'</br>'+ '<div class="div" style="background: #e93b6f; height: 30px; width: 100%"> </div>'+'</br><strong>'+ 'Nachricht von ' + firstname + ' ' + lastname +':</strong>'+ '</br>' + '</br>' +message +'</br>'+ '</span'
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    return HttpResponseRedirect('DankeAnfrage')
                except:
                    messages.warning(request, 'Bitte alle Felder vollständig ausfüllen')
            else:
                messages.warning(request, "Bitte alle Felder vollständig ausfüllen")
        else:
            messages.warning(request, "Bitte alle Felder vollständig ausfüllen")
    
    return render(request, "WirSuchenMitarbeiter.html")

def Datenschutz(request):
    return render(request, "Datenschutz.html")

def Nutzungsbedingungen(request):
    return render(request, "Nutzungsbedingungen.html")


def Impressum(request):
    return render(request, "Impressum.html")



    

