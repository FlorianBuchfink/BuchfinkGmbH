from django.urls import path 
from Website.views import Mainpage, Heizungstausch, Neubausanierung, Badsanierung, Lueftung, Spenglerei, Pool, Anfahrt, Oeffnungszeiten, Kontakt, Firmengeschichte, Kontaktformular, Danke, Mitarbeiter, Datenschutz, Nutzungsbedingungen, Impressum


urlpatterns = [
    path('', Mainpage, name='Mainpage'),
    path('Heizungsmodernisierung/', Heizungstausch , name='Heizungstausch'),
    path('Neubausanierung/', Neubausanierung, name='Neubausanierung'),
    path('Badsanierung/' , Badsanierung, name='Badsanierung'),
    path('Lueftung/' , Lueftung, name='Lueftung'),
    path('Spenglerei/', Spenglerei, name='Spenglerei'),
    path('Pool/', Pool, name='Pool'),
    path('Anfahrt/', Anfahrt, name='Anfahrt'),
    path('Oeffnungszeiten/', Oeffnungszeiten, name='Oeffnungszeiten'),
    path('Kontakt', Kontakt, name='Kontakt'),
    path('Firmengeschichte', Firmengeschichte, name='Firmengeschichte'),
    path('Kontaktformular', Kontaktformular, name='Kontaktformular'),
    path('DankeAnfrage', Danke, name='Danke'),
    path('WirStellenEin', Mitarbeiter, name='WirStellenEin'),
    path('Datenschutz', Datenschutz, name='Datenschutz'),
    path('Nutzungsbedingungen', Nutzungsbedingungen, name='Nutzungsbedingungen'),
    path('Impressum', Impressum, name='Impressum'),
    
]


  
