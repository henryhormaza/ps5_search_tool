import urllib.request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


class ps5_sarch_tool:
    def __init__(self):

        self.temp_url =''
        self.test_url =''
        self.temp_class =''
        self.driver =''
        self.html=''
        self.webpage=''
        self.soup=''
        self.id=''
        self.store=''
        self.price_tag=''
        self.price_id=''
        self.price=''

    def encontrada(self):
        webhook = open("webhook.txt", "r")
        wh_url = webhook.read()        
        if self.price != "$9.999.990":
            requests.get(url = wh_url)
            print("\n\n #################################################found in: "+self.store+"\n "+self.temp_url+"\n\n")    
            #driver = webdriver.Firefox()
            #driver.get(temp_url)
            #sleep(1)
            self.driver.quit()
            self.driver = webdriver.Firefox()
            self.driver.minimize_window()
            self.driver.get(self.temp_url)
            sleep(1)
            try:
                if self.id=='':
                    self.driver.find_element_by_class_name(self.temp_class).click() 
                else:
                    self.driver.find_element_by_id(self.id).click()
            except:
                pass

    def check_store(self):
        #datos = urllib.request.Request(temp_url, headers={'User-Agent': 'Mozilla/5.0'}) 
        #web_byte = urllib.request.urlopen(datos).read()
        
        #self.temp_url = self.test_url

        options = Options()
        options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.temp_url)
        sleep(1)
        self.web_byte = self.driver.page_source
        try:
            self.webpage = self.web_byte.decode('utf-8')
        except:
            self.webpage = self.web_byte
        #self.soup = BeautifulSoup(self.webpage)
        if self.id == '':
            #self.results = self.soup.find_all(self.temp_id, class_=self.temp_class)
            self.driver.find_element_by_class_name(self.temp_class)
        else:
            temp_list=[]
            temp_list.append(ps5.driver.find_element_by_id(self.id))
            self.results = temp_list
    
    def check_price(self):
        #datos = urllib.request.Request(temp_url, headers={'User-Agent': 'Mozilla/5.0'}) 
        #web_byte = urllib.request.urlopen(datos).read()
        
        # self.temp_url = self.test_url
        try:
            #self.price = self.soup.find_all(self.price_id, class_=self.price_tag)[0].next
            self.price = self.driver.find_element_by_class_name(self.price_tag).text
        except:
            pass
        
        

#for x in range(15):
while True:
############################### CL
    if True:
        try:
            ps5 = ps5_sarch_tool()
            ps5.store = "zmart fisica"
            ps5.temp_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=78812'
            ps5.test_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=79739'
            
            ps5.temp_class = 'comprar2015'
            ps5.temp_id = 'input'

            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            
    if True:
        try:
            ps5 = ps5_sarch_tool()
            ps5.store = "zmart digital"
            ps5.temp_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=79725'
            ps5.test_url = 'https://www.zmart.cl/scripts/prodView.asp?idProduct=79739'
            
            ps5.temp_class = 'comprar2015'
            ps5.temp_id = 'input'

            ps5.check_store()
            #ps5.check_price()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            

    if True:
        try:
            ps5 = ps5_sarch_tool()       
            ps5.store = "ripley digital"  
            ps5.temp_url = 'https://simple.ripley.cl/reserva-consola-ps5-digital-edition-2000380458314p'
            ps5.test_url = 'https://simple.ripley.cl/control-ps5-dualsense-wireless-2000380632868p?color_80=blanco&cbar_widget_p4=&s=o'
            # ps5.temp_url = test_url
            ps5.temp_class = 'js-buy-button'
            ps5.price_tag = 'product-price'
            ps5.temp_id = 'button'
            ps5.price_id='span'
            ps5.check_store()
            ps5.check_price()
            #resultado = ps5.results[0]
            #print(resultado)
         
            if ps5.results[0].next == 'Agregar a la bolsa':
                ps5.encontrada()
            else:
                print("not found in "+ps5.store)
                ps5.driver.close()
                ps5.driver.quit()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            
    if True:
        try:
            ps5 = ps5_sarch_tool()       
            ps5.store = "ripley fisico"  
            ps5.temp_url = 'https://simple.ripley.cl/reserva-consola-ps5-2000380458321p?color_80=blanco'
            ps5.test_url = 'https://simple.ripley.cl/control-ps5-dualsense-wireless-2000380632868p?color_80=blanco&cbar_widget_p4=&s=o'
            # ps5.temp_url = test_url
            ps5.temp_class = 'js-buy-button'
            ps5.temp_id = 'button'
            ps5.price_tag = 'product-price'
            ps5.price_id='span'
            ps5.check_store()
            ps5.check_price()
            #resultado = ps5.results[0]
            #print(resultado)
         
            if ps5.results[0].next == 'Agregar a la bolsa':
                ps5.encontrada()
            else:
                print("not found in "+ps5.store)
                ps5.driver.close()
                ps5.driver.quit()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            

    if True:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store="microplay digital"
            ps5.temp_url = 'https://www.microplay.cl/producto/consola-digital-ps5-sony/'
            ps5.test_url = 'https://www.microplay.cl/producto/control-dualsense-ps5-wireless-white-sony/'
            # ps5.temp_url = test_url
            ps5.temp_class = 'btn-submit'
            ps5.temp_id = 'a'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            
    if True:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store="microplay Fisica"
            ps5.temp_url = 'https://www.microplay.cl/producto/consola-ps5-sony/'
            ps5.test_url = 'https://www.microplay.cl/producto/control-dualsense-ps5-wireless-white-sony/'
            # ps5.temp_url = test_url
            ps5.temp_class = 'btn-submit'
            ps5.temp_id = 'a'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
            

    if True:    
        try:
            ps5 = ps5_sarch_tool()   
            ps5.store="Sony CL Digital"
            ps5.temp_url = 'https://store.sony.cl/playstation5-digital/p'
            ps5.test_url = 'https://store.sony.cl/ps5-control-inalambrico-dualsense/p'
            # ps5.temp_url = test_url
            ps5.temp_class = 'new-add-to-cart'
            ps5.temp_id = 'button'
            ps5.check_store()
            
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
    if True:    
        try:
            ps5 = ps5_sarch_tool()   
            ps5.store="Sony CL Fisica"
            ps5.temp_url = 'https://store.sony.cl/playstation5/p'
            ps5.test_url = 'https://store.sony.cl/ps5-control-inalambrico-dualsense/p'
            # ps5.temp_url = test_url
            ps5.temp_class = 'new-add-to-cart'
            ps5.temp_id = 'button'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
    
    if True:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store = "la polar"
            ps5.temp_url ='https://www.lapolar.cl/consola-sony-playstation-5/23395401.html'
            ps5.test_url = 'https://www.lapolar.cl/control-inalambrico-sony-ps5-dualsense-wireless-controller/23395355.html'
            # ps5.temp_url = test_url
            ps5.temp_class = 'add-to-cart'
            ps5.temp_id = 'button'
            ps5.check_store()
            
            #print(resultado)
            if str(ps5.results[0].next).find("Agregar")>=0:
                ps5.encontrada()
            else:
                print("not found in "+ps5.store)
                ps5.driver.close()
                ps5.driver.quit()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
    
    if True:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store = "Lider CL"
            ps5.temp_url = 'https://www.lider.cl/catalogo/product/sku/1086920'
            ps5.test_url = 'https://www.lider.cl/catalogo/product/sku/1086922'
    
            ps5.temp_class = 'walmart-add-cart-blue-button'
            ps5.temp_id = 'div'
            ps5.id='addProductToCart'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
    
    if True:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store = "PC factory"
            ps5.temp_url = 'https://www.pcfactory.cl/producto/39192'
            ps5.test_url = 'https://www.pcfactory.cl/producto/39193-sony-control-dualsense-ps5'
    
            ps5.temp_class = 'agregar_al_carro a_domicilio'
            ps5.temp_id = 'a'
            ps5.id='agrega_carro'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()

    if True:
        try:            
            ps5 = ps5_sarch_tool()  
            ps5.store = "Paris fisica"
            ps5.temp_url = 'https://www.paris.cl/consola-ps5-440437999.html'
            ps5.test_url = 'https://www.paris.cl/control-wireless-dualsense-ps5-440442999.html#q=ps5&start=1'
    
            ps5.temp_class = 'add-to-cart'
            ps5.temp_id = 'button'
            #ps5.id='440442999-add-to-cart'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()
    if True:
        try:            
            ps5 = ps5_sarch_tool()  
            ps5.store = "Paris Digital"
            ps5.temp_url = 'https://www.paris.cl/consola-ps5-edicion-digital-440439999.html'
            ps5.test_url = 'https://www.paris.cl/control-wireless-dualsense-ps5-440442999.html#q=ps5&start=1'
    
            ps5.temp_class = 'add-to-cart'
            ps5.temp_id = 'button'
            #ps5.id='440442999-add-to-cart'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.close()
            ps5.driver.quit()

########################################################################################## CO
    if False:
        try:
            ps5 = ps5_sarch_tool()   
            ps5.store="Sony CO Fisica"
            ps5.temp_url = 'https://ps5.store.sony.com.co/playstation5/p'
            ps5.test_url = 'https://ps5.store.sony.cl/ps5-control-inalambrico-dualsense/p'
            # ps5.temp_url = test_url
            ps5.temp_class = 'button'
            ps5.temp_id = 'new-add-to-cart'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.quit()

    if False:
        try:
            ps5 = ps5_sarch_tool()  
            ps5.store="falabella Col fisica"
            ps5.temp_url = 'https://www.falabella.com.co/falabella-co/product/9440498/ps5-consola-standard/9440498'
            ps5.test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
            # ps5.temp_url = test_url
            ps5.temp_class = 'jsx-1816208196'
            ps5.temp_id = 'button'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.quit()
    
    if False:
        try:
            ps5 = ps5_sarch_tool()   
            ps5.store="falabella Col fisica 2"
            ps5.temp_url ='https://www.falabella.com.co/falabella-co/product/9440498/Consola-PlayStation-5-825GB/9440498'
            ps5.test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
            # ps5.temp_url = test_url
            ps5.temp_class = 'jsx-1816208196'
            ps5.temp_id = 'button'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.quit()
    
    if False:
        try:
            ps5 = ps5_sarch_tool()       
            ps5.store = "falabella Col digital "
            ps5.temp_url ='https://www.falabella.com.co/falabella-co/product/9440499/Consola-PlayStation-5-Digital-Edition-825GB/9440499'
            ps5.test_url = 'https://www.falabella.com.co/falabella-co/product/9440500/Control-PS5-Dual-Sense/9440500'
            # ps5.temp_url = test_url
            ps5.temp_class = 'jsx-1816208196'
            ps5.temp_id = 'button'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.quit()
    
        
    if False:
        try:
            ps5.store = "Pepe Ganga"
            ps5.temp_url = 'https://www.pepeganga.com/consola-ps5-standard-711719541769/p?uam=true&mobile=4'
            ps5.test_url = 'https://www.pepeganga.com/videojuego-ps5-call-of-duty-black-ops-cold-war-047875101142/p?idsku=117943&source_impresee=0a95b19b-d6b1-4260-8606-c08ed12089f3'
            # ps5.temp_url = test_url
            ps5.temp_class = 'buy-in-page-button'
            ps5.temp_id = 'a'
            ps5.check_store()
            resultado = ps5.results[0]
            #print(resultado)
            ps5.encontrada()
        except:
            print("not found in "+ps5.store)
            ps5.driver.quit()
        
    
       


