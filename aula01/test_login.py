from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('file:///C:/Users/micael_junco/Documents/GitHub/Testes-de-Sistemas/aula01/login.html')

time.sleep(1)

# Preenche o campo de usuário:
usuario_input = driver.find_element(By.ID, 'username')
usuario_input.send_keys('admin')
# Preenche o campo de usuário:
senha_input = driver.find_element(By.ID, 'password')
senha_input.send_keys('1234')

botao_subm = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
botao_subm.click()

time.sleep(5)

if "Formulário Básico" in driver.title:
    print(f'[SUCESSO]: Login realizado com sucesso e redirecionado para index.html ({driver.title})\n')
else:
    print('[ERRO]: Falha no login ou redirecionamento.\n')

print('[INFO]: Página atual: '+driver.title)

# Fecha o navegador:
#driver.quit()