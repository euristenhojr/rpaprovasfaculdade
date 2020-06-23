from selenium import webdriver
import time

class Parametros:

    login = ""
    senha = ""


    def criarLogin(self, login):
        self.login = login

    def criarSenha(self, senha):
        self.senha = senha


    def retornalogin(self):
        return self.login

    def retornaSenha(self):
        return self.senha

DadosUser = Parametros()

DadosUser.criarLogin('Apague esse texto e coloque sua matrícula professor')
DadosUser.criarSenha('Apague esse texto e coloque sua senha professor')


driver = webdriver.Chrome("/usr/bin/chromedriver")
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("https://eadsp.unichristus.edu.br/login/index.php")
#driver.get("https://www.google.com")

#driver.find_element_by_id("searchField").send_keys("Movies")
'''
driver.find_element_by_name("q").send_keys("Selenium")
time.sleep(2)
driver.find_element_by_name("btnK").click()
'''
time.sleep(2)
#driver.find_element_by_text("Premium").click()
driver.find_element_by_css_selector("#username").send_keys(DadosUser.retornalogin())
driver.find_element_by_css_selector("#password").send_keys(DadosUser.retornaSenha())
driver.find_element_by_css_selector("#loginbtn").click()
time.sleep(3)
driver.find_element_by_link_text("61082 - Engenharia de Software I - 616N04 - 20.1").click()
time.sleep(3)
#driver.get("https://eadsp.unichristus.edu.br/course/view.php?id=2414&notifyeditingon=1")
#time.sleep(3)
driver.find_element_by_css_selector("#action-menu-toggle-2").click()
time.sleep(5)
driver.find_element_by_link_text('Ativar edição').click()
time.sleep(2)
driver.find_element_by_link_text('PROVA ALIMENTADA POR ROBÔ').click()
time.sleep(2)
driver.find_element_by_link_text('Adicionar uma atividade ou recurso').click()
time.sleep(2)
driver.find_element_by_css_selector("#item_quiz").click()
time.sleep(2)
driver.find_element_by_name('submitbutton').click()
time.sleep(2)
driver.find_element_by_id('id_name').send_keys("Questão do robô")
time.sleep(3)
driver.find_element_by_link_text('Duração').click()
time.sleep(3)
driver.find_element_by_id('id_timeopen_enabled').click()
time.sleep(3)
driver.find_element_by_id('id_timeclose_enabled').click()
time.sleep(3)
driver.find_element_by_id('id_timelimit_enabled').click()
time.sleep(3)
driver.find_element_by_id('id_timelimit_number').send_keys("5")
time.sleep(3)
driver.find_element_by_id('id_submitbutton').click()
