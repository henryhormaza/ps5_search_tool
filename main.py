import urllib.request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep

def ps5_encontrada(temp_url="", temp_class=""):
    webhook = open("webhook.txt", "r")
    wh_url = webhook.read()
    requests.get(url = wh_url)
    print("\n\n #################################################found in: \n "+temp_url+"\n\n")
    driver = webdriver.Firefox()
    driver.get(temp_url)
    sleep(1)
    driver.find_element_by_class_name(temp_class).click() 

def check_store(temp_url="", temp_class="", temp_id=""):
    datos = urllib.request.Request(temp_url, headers={'User-Agent': 'Mozilla/5.0'}) 
    web_byte = urllib.request.urlopen(datos).read()
    try:
        webpage = web_byte.decode('utf-8')
    except:
        webpage = web_byte
    soup = BeautifulSoup(webpage)
    results = soup.find_all(temp_id, class_=temp_class)
    return results



for x in range(15):
    try:
        #PS5
        store = "zmart"
        temp_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=79725'
        test_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=79724'
        # temp_url = test_url
        temp_class = 'comprar2015'
        temp_id = 'input'

        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        ps5_encontrada(temp_url,temp_class)
    except:
        print("not found in "+store)
        pass
    try:
        #PS5  
        store = "ripley"  
        temp_url = 'https://simple.ripley.cl/reserva-consola-ps5-digital-edition-2000380458314p'
        test_url = 'https://simple.ripley.cl/control-ps5-dualsense-wireless-2000380632868p?color_80=blanco&cbar_widget_p4=&s=o'
        # temp_url = test_url
        temp_class = 'js-buy-button'
        temp_id = 'button'

        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        if results[0].next == 'Agregar a la bolsa':
            ps5_encontrada(temp_url,temp_class)
        else:
            print("not found in "+store)
    except:
        print("not found in "+store)
    try:
        #PS5   
        store="microplay"
        temp_url = 'https://www.microplay.cl/producto/consola-digital-ps5-sony/'
        test_url = 'https://www.microplay.cl/producto/control-dualsense-ps5-wireless-white-sony/'
        # temp_url = test_url
        temp_class = 'btn-submit'
        temp_id = 'a'
        
        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        ps5_encontrada(temp_url,temp_class)
    except:
        print("not found in "+store)
    # try:
    #     #PS5    
    #     datos = urllib.request.Request('https://store.sony.cl/playstation5-digital/p', headers={'User-Agent': 'Mozilla/5.0'}) 
    #     #datos = urllib.request.Request('https://store.sony.cl/ps5-control-inalambrico-dualsense/p', headers={'User-Agent': 'Mozilla/5.0'}) 
    #     web_byte = urllib.request.urlopen(datos).read()
    #     webpage = web_byte.decode('utf-8')
    #     soup = BeautifulSoup(webpage)
    #     results = soup.find_all('div', class_='box buy')
    #     resultado = results[0]
    #     print(resultado)
    #     requests.get(url = 'https://maker.ifttt.com/trigger/PS5/with/key/FncyI5tezmj4m-Ti7CUPqUcFOqappribX3dZeXAE2g')
    #     print("#################################################found in sony CL")
    # except:
    #     pass
    # try:
    #     #PS5    
    #     datos = urllib.request.Request('https://store.sony.com.co/playstation5/p', headers={'User-Agent': 'Mozilla/5.0'}) 
    #     #datos = urllib.request.Request('https://store.sony.cl/ps5-control-inalambrico-dualsense/p', headers={'User-Agent': 'Mozilla/5.0'}) 
    #     web_byte = urllib.request.urlopen(datos).read()
    #     webpage = web_byte.decode('utf-8')
    #     soup = BeautifulSoup(webpage)
    #     results = soup.find_all('a', class_='buy-button')
    #     resultado = results[0]
    #     print(resultado)
    #     if not(str(resultado.text).find("Producto sin stock")):
    #         requests.get(url = 'https://maker.ifttt.com/trigger/PS5/with/key/FncyI5tezmj4m-Ti7CUPqUcFOqappribX3dZeXAE2g')
    #         print("#################################################found in sony CO")
    # except:
    #     pass
    try:
        #PS5   
        store="falabella Col fisica"
        temp_url = 'https://www.falabella.com.co/falabella-co/product/9440498/ps5-consola-standard/9440498'
        test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
        # temp_url = test_url
        temp_class = 'jsx-1816208196'
        temp_id = 'button'

        
        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        ps5_encontrada(temp_url,temp_class)

    except:
        print("not found in "+store)
    try:
        #PS5    
        store="falabella Col fisica 2 "
        temp_url ='https://www.falabella.com.co/falabella-co/product/9440498/Consola-PlayStation-5-825GB/9440498'
        test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
        # temp_url = test_url
        temp_class = 'jsx-1816208196'
        temp_id = 'button'


        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        ps5_encontrada(temp_url,temp_class)
        
    except:
        print("not found in "+store)
    try:
        #PS5  
        store = "falabella Col digital "
        temp_url ='https://www.falabella.com.co/falabella-co/product/9440499/Consola-PlayStation-5-Digital-Edition-825GB/9440499'
        test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
        # temp_url = test_url
        temp_class = 'jsx-1816208196'
        temp_id = 'button'

        
        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado)
        ps5_encontrada(temp_url,temp_class)
    except:
        print("not found in "+store)
    try:
        #PS5   
        store = "la polar"
        temp_url ='https://www.lapolar.cl/consola-sony-playstation-5/23395401.html'
        test_url = 'https://www.lapolar.cl/control-inalambrico-sony-ps5-dualsense-wireless-controller/23395355.html'
        # temp_url = test_url
        temp_class = 'add-to-cart'
        temp_id = 'button'


        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado.next)
        if str(resultado.next).find("Agregar")>=0:
            ps5_encontrada(temp_url,temp_class)
        else:
            print("not found in "+store)
    except:
        print("not found in "+store)

    try:
        store = "Pepe Ganga"
        temp_url = 'https://www.pepeganga.com/consola-ps5-standard-711719541769/p?uam=true&mobile=4'
        test_url = 'https://www.pepeganga.com/videojuego-ps5-call-of-duty-black-ops-cold-war-047875101142/p?idsku=117943&source_impresee=0a95b19b-d6b1-4260-8606-c08ed12089f3'
        # temp_url = test_url
        temp_class = 'buy-in-page-button'
        temp_id = 'a'


        results = check_store(temp_url,temp_class,temp_id)
        resultado = results[0]
        #print(resultado.next)
        ps5_encontrada(temp_url,temp_class)
    except:
        print("not found in "+store)


   