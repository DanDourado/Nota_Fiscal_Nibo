from selenium import webdriver 
#importa o selenium
import time
#para adicionar delay entre as açoes necessaria

         #linha faz parte do processo  de adicionar atributos para nossa classe 
SITE_LINK ="https://www.nibo.com.br/"
         #site que queremos utilizar a automatização
SITE_MAP = {} 
        #Sera um dicionario com o local aonde se encontra os objetos que serão automatizado 
driver = webdriver.Chrome(executable_path ="C:\\chromedriver_win32\\chromedriver.exe") 
        #instacia o driver do selenium para podemos fazer a automação, copiar o caminho do executave que foi baixado
driver.maximize_window()
def abrir_site():
        time.sleep(2)
        driver.get(SITE_LINK)
        time.sleep(50)
        
def clicar_no_cnpj():
        pass

abrir_site()