from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.mensagem = "Olá estou testando o meu bot que fiz com pythom!"
        self.email = "ecaetanocorrea@gmail.com"
        self.senha = "virginia50"
        self.data_cod = "auth_wall_desktop_profile-login-toggle"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        times(3)
        self.driver.get('https://www.linkedin.com/company/dbserver/people/?facetGeoRegion=br%3A6467')
        times(20)


        join_form_form_body = self.driver.find_element_by_class_name('join-form__form-body')
        times(3)
        join_form__form_body_subtext = join_form_form_body.find_element_by_class_name('join-form__form-body-subtext')
        times(3)
        link_entrar = join_form__form_body_subtext.find_element_by_tag_name('a')
        times(3)
        link_entrar.click()

        link_entrar = self.driver.find_element_by_class_name('login-email')
        times(3)
        link_entrar.click()
        times(3)
        link_entrar.send_keys(self.email)

        login_password = self.driver.find_element_by_class_name('login-password')
        times(3)
        login_password.click()
        times(3)
        login_password.send_keys(self.senha)


        login = self.driver.find_element_by_class_name('login')
        times(3)
        login.click()
        times(20)
        
        #artdeco-button
        for x in range(200):
            seguir = self.driver.find_element_by_class_name('artdeco-button__text')
            times(3)
            seguir.click()

        
            
        
        '''for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_bot = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chat_bot.click()
            chat_bot.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(f"//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)'''
def times(n):
            for x in range(n):
                print((x+1),' Segundos')
                time.sleep(1)
                
bot = whatsappbot()
bot.EnviarMensagens()
print("Fim da execução")
