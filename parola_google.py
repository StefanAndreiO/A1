import requests
from bs4 import BeautifulSoup
import smtplib


with open(r'C:\Users\Student\Desktop\L1\parola.txt') as fisier:
    parola_google = fisier.read().strip()
    
    
to_addr_list = ['ohescustefan@gmail.com']
cc_addr_list = ['']
sender = 'ohescustefan@gmail.com'
subject = 'A scazut pretul'

#print (parola_google)
def sendmail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'smtp.gmail.com:587'
        header = 'From: %s\n' % sender
        header+= 'To: %s\n' % ','.join(to_addr_list)
        header+= 'Cc: %s\n' % ','.join(cc_addr_list)
        header+= 'Subject: %s\n\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,parola_google)
        problems=server.sendmail(sender,to_addr_list,message)
        server.quit
        return True
    except Exception as e:
        print("A aparut o eroare")
        return False
    
def data_scraping_avansat():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    pret = soup.find('p', attrs={'class' : 'product-new-price'}).text 
    pret = pret[0:5]
    pret = pret.replace(".", "")
    pret = int(pret)
    print(type(pret))
    pret_de_referinta = 7200
    titlu_produsului = data_nume().strip()
    ratingul_produs = rating_produs()
    if pret<pret_de_referinta:
        print("Pretul a scazut")
        mesaj = f"Pretul actual: {pret} RON\n"
        mesaj+= f"Pretul de referinta: {pret_de_referinta} RON\n"
        mesaj+= f"Titlul produsului: {titlu_produsului}\n"
        mesaj+= f"Ratingul produsului: {ratingul_produs}\n"
        sendmail(sender,mesaj,subject,to_addr_list,cc_addr_list=[])
    else:
        print("Pretul este mai mare")
        print(pret)

def data_nume():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    nume_produs = soup.find('h1', attrs={'class' : 'page-title'}).text 
    return nume_produs

def rating_produs():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-16-pro-max-256gb-5g-desert-titanium-mywx3zd-a/pd/DW367LYBM/")
    soup = BeautifulSoup(req.text, "html.parser")
    rating = soup.find('p', attrs={'class' : 'review-rating-data'}).text 
    return rating


recenzie = rating_produs()
print(recenzie)
nume_produsului = data_nume().strip()
print(nume_produsului)
mail = data_scraping_avansat()
print(mail)