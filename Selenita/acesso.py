from selenium import webdriver
from bs4 import BeautifulSoup
from licencaApple import inputsSemCred
class acesso:
    global url
    url = "http://developer.apple.com/account"
    def __init__(self, usr, passw, optd, alias, nCert):
        self.usr   =  usr
        self.pasw  = passw
        self.optd  = optd
        self.alias = alias
        self.nCert = nCert
        self.acessar(self.usr, self.pasw, self.optd, self.alias, self.nCert)

    def acessar(self, email, senha, optd, alias, nCert):
        try:
            # executable_path is the origin of your webdriver, in this case is geckodriver(firefox).
            driver = webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver/0.21.0/bin/geckodriver')
            driver.get(url)
            driver.implicitly_wait(15)
            src = driver.page_source
            html = BeautifulSoup(src, 'html.parser')
            pasw = html.find('input', {'type': 'password'}).get('name')
            usr = html.find('input', {'type': 'text'}).get('name')
            login = driver.find_element_by_name(usr)
            sen = driver.find_element_by_name(pasw)
            button = driver.find_element_by_id("submitButton2")
            login.send_keys(email)
            sen.send_keys(senha)
            button.click()
            driver.implicitly_wait(15)
            cert = driver.find_element_by_partial_link_text("Certificates")
            cert.click()
            driver.implicitly_wait(15)
            if(optd == '3'):
                gId = driver.find_element_by_partial_link_text("App IDs")
                gId.click()
                driver.implicitly_wait(15)
                add = driver.find_element_by_class_name("add")
                add.click()
                driver.implicitly_wait(15)
                inptN = driver.find_element_by_name("appIdName")
                inptN.send_keys(nCert)
                tip = driver.find_element_by_css_selector("input#type-explicit")
                tip.click()
                inptAlias = driver.find_element_by_name("explicitIdentifier")
                inptAlias.send_keys(alias)
                push = driver.find_element_by_id("push")
                push.click()
                subBlue = driver.find_element_by_class_name("blue")
                subBlue.click()
                driver.implicitly_wait(15)
                regClick = driver.find_element_by_xpath("//button[contains(text(), 'Register')]")
                regClick.click()
                driver.implicitly_wait(15)
                done = driver.find_element_by_xpath("//button[contains(text(), 'Done')]")
                done.click()
                print("################# APP ID GERADO COM SUCESSO! #################\n")
                driver.close()
                inputsSemCred(email, senha)
            else:
                if(optd == '1'):
                    dev = driver.find_elements_by_partial_link_text("Development")
                    dev[1].click()
                    cOptTip = "input#type-development"
                elif(optd == '2'):
                    prod = driver.find_element_by_partial_link_text("Distribution")
                    prod.click()
                    cOptTip = "input#type-production"
                driver.implicitly_wait(15)
                add = driver.find_element_by_class_name("add")
                add.click()
                driver.implicitly_wait(15)
                tip = driver.find_element_by_css_selector(cOptTip)
                tip.click()
                cont = driver.find_element_by_partial_link_text("Continue")
                cont.click()
                driver.implicitly_wait(15)
                appId = driver.find_element_by_xpath("//option[contains(text(),'%s')]" % alias)
                appId.click()
                sub = driver.find_element_by_class_name("submit")
                sub.click()
                driver.implicitly_wait(15)
                if (optd == '1'):
                    slc_cert = driver.find_element_by_id("selectAllCId")
                    slc_cert.click()
                    sub_2 = driver.find_element_by_class_name("submit")
                    sub_2.click()
                    driver.implicitly_wait(15)
                    slc_dev = driver.find_element_by_id("selectAllDId")
                    slc_dev.click()
                    sub_3 = driver.find_element_by_class_name("submit")
                    sub_3.click()
                    driver.implicitly_wait(15)
                elif(optd == '2'):
                    slc_cert = driver.find_elements_by_name("certificateIds")
                    if(len(slc_cert) > 1):
                        slc_cert[0].click()
                    else:
                        slc_cert.click()
                    sub_2 = driver.find_element_by_partial_link_text("Continue")
                    sub_2.click()
                prov = driver.find_element_by_name("provisioningProfileName")
                prov.send_keys(nCert)
                sub_4 = driver.find_element_by_class_name("submit")
                sub_4.click()
                driver.implicitly_wait(15)
                down = driver.find_element_by_partial_link_text("Download")
                down.click()
                done = driver.find_element_by_partial_link_text("Done")
                done.click()
                print("################# PROVISIONING FILE GERADO COM SUCESSO! #################\n Visualize seus downloads!")
                driver.close()
                inputsSemCred(email, senha)
        except:
            print("Ocorreu um erro ao acessar o webDrivrer")
            driver.close()
