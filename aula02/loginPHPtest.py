from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8080/MICAEL/Testes-de-Sistemas/aula02/login.html')

def validarCampoEscrito(metodoBusca: str, nomeCampo: str, validacao: str):
    
    match (metodoBusca):
        case 'ID':
            input = driver.find_element(By.ID, nomeCampo)
        case 'CSS_SELECTOR':
            input = driver.find_element(By.CSS_SELECTOR, nomeCampo)
        case _:
            print('\n[ERRO]: Opção de método de busca inválido.\n')

    if (input):
        print(f'\n[SUCESSO]: Campo {nomeCampo} encontrado com sucesso.\n')
        
        input.send_keys(validacao)
        print(f'\n[INFO]: Campo {nomeCampo} preenchido com \"{validacao}\".\n')
        
        time.sleep(1)
    

validarCampoEscrito('ID', 'username', 'Admin')

validarCampoEscrito('ID', 'password', '12345678')

btn_sub = driver.find_element(By.CSS_SELECTOR, '#loginForm>button[type="submit"]')
btn_sub.click()
time.sleep(5) 

if "Home" in driver.title:
    print(f"\n[SUCESSO]: Login concluído e redirecionado para {driver.title}\n")
else:
    print(f"\n[ERRO]: Falha no login/redirecionamento.\n")