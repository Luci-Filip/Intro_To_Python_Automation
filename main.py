'''
Tema 8 - SELECTORS
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
s = Service(ChromeDriverManager().install())    # initializam chrome
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

by_id = 0
chrome.get("https://formy-project.herokuapp.com/form")
sleep(3)
chrome.find_element(By.ID,"first-name").send_keys('Test_1_BY_ID')
by_id += 1
chrome.find_element(By.ID,'last-name').send_keys('Test_2_BY_ID')
by_id += 1
chrome.find_element(By.ID,'job-title').send_keys('Test_3_BY_ID')
by_id += 1
sleep(3)
chrome.find_element(By.ID,'radio-button-2').click()
by_id += 1
sleep(3)
chrome.find_element(By.ID,'checkbox-3').click()
by_id += 1
experience = chrome.find_element(By.ID,'select-menu')
by_id += 1
experience.click()
sleep(3)
experience.send_keys('5-9')
sleep(3)
chrome.find_element(By.ID,'datepicker').click()
by_id += 1
sleep(3)
chrome.find_element(By.XPATH,"//tr/td[@class='today day']").click()
sleep(3)
submit = chrome.find_element(By.CSS_SELECTOR,'a.btn')
submit.click()
sleep(3)
extract_the_text = chrome.find_element(By.XPATH,'/html/body/div[1]/div').text
sleep(3)
original_text = "The form was successfully submitted!"
assert original_text == extract_the_text
print(f'The extracted text "{extract_the_text}" is equivalent to the original text "{original_text}" ')
chrome.quit()
'''
● Link text
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
by_link_text = 0
chrome.find_element(By.LINK_TEXT,'Buttons').click()
by_link_text += 1
sleep(3)
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
chrome.find_element(By.LINK_TEXT,'Checkbox').click()
by_link_text += 1
sleep(3)
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
chrome.find_element(By.LINK_TEXT,'Datepicker').click()
by_link_text += 1
sleep(3)
chrome.quit()
'''
● Parțial link text
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
by_partial_link_text = 0
chrome.find_element(By.PARTIAL_LINK_TEXT,'Drag and').click()
by_partial_link_text += 1
sleep(3)
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT,'File').click()
by_partial_link_text += 1
sleep(3)
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/")
sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT,'Key and').click()
by_partial_link_text += 1
sleep(3)
chrome.quit()
'''
● Name
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/forgot_password")
sleep(3)
by_name = 0
chrome.find_element(By.NAME,'email').click()
by_name += 1
sleep(3)
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
sleep(6)
chrome.find_element(By.NAME,"firstname").send_keys("Test-first-name")
by_name += 1
chrome.quit()

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
sleep(5)
chrome.find_element(By.NAME,"lastname").send_keys('Test-last-name')
by_name += 1
sleep(5)
chrome.quit()
'''
● Tag*
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
sleep(3)
by_tag = 0
the_tag = chrome.find_elements(By.TAG_NAME,'input')
the_tag[0].send_keys("First-Name")
by_tag += 1
the_tag[1].send_keys("Last-Name")
by_tag += 1
the_tag[2].send_keys("I am learning to use the selectors")
by_tag += 1
sleep(3)
chrome.quit()
'''
● Class name*
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
sleep(3)
by_class_name = 0
class_name = chrome.find_elements(By.CLASS_NAME,"form-control")
class_name[0].send_keys("test_1")
by_class_name += 1
class_name[1].send_keys("test_2")
by_class_name += 1
class_name[2].send_keys("test_3")
by_class_name += 1
sleep(3)
chrome.quit()
'''
'''
print(f'The number of elements identified "by ID" are: {by_id}')
print(f'The number of elements identified "by LINK_TEXT" are: {by_link_text}')
print(f'The number of elements identified "by Partial_Link_Text" are: {by_partial_link_text}')
print(f'The number of elements identified "by NAME" are: {by_name}')
print(f'The number of elements identified "by TAG NAME" are: {by_tag}')
print(f'The number of elements identified "by CLASS NAME" are: {by_class_name}')
'''
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
sleep(3)
# css selector by id
chrome.find_element(By.CSS_SELECTOR,'input#job-title').send_keys("css_test-id")
sleep(3)
# css selector by class
chrome.find_element(By.CSS_SELECTOR,'input.form-control').send_keys("css-test-class")
sleep(3)
# css selector by attribute value
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("css-attribut-value")
sleep(3)
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").clear()
# css selector by attribute partial value
chrome.find_element(By.CSS_SELECTOR,"div input[placeholder*='last']").send_keys("attribut-partial value")
sleep(3)
chrome.quit()
print("The css selectors worked fine!")
'''
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH,'//input[@id="first-name"]').send_keys("Xpath-attribut-value-1")
sleep(3)
chrome.find_element(By.XPATH,'//input[@id="last-name"]').send_keys("Xpath-attribut-value-2")
sleep(3)
chrome.find_element(By.XPATH,'//input[@id="job-title"]').send_keys("Xpath-attribut-value-3")
sleep(3)
chrome.quit()
print("The Xpath selectors by attribut = value, worked well!")
'''
● 3 după textul de pe element
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
chrome.find_element(By.XPATH,'//a[@class="nav-link dropdown-toggle"]').click()
sleep(8)
chrome.find_element(By.XPATH,'//a[text()="Autocomplete"]').click()
sleep(8)
chrome.find_element(By.XPATH,'//a[@class="nav-link dropdown-toggle"]').click()
sleep(8)
chrome.find_element(By.XPATH,'//a[text()="Buttons"]').click()
sleep(8)
chrome.find_element(By.XPATH,'//a[@class="nav-link dropdown-toggle"]').click()
sleep(8)
chrome.find_element(By.XPATH,"//div/a[text()='Checkbox']").click()
sleep(8)
chrome.quit()
print("The Xpath selector by text after element, worked fine!")
'''
● 1 după parțial text
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
chrome.find_element(By.XPATH,"//div/li/a[contains(text(),'Key and')]").click()
sleep(8)
chrome.quit()
print("The Xpath element identified after partial text!")
'''
● 1 cu SAU, folosind pipe |
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
sleep(3)
form = chrome.find_element(By.XPATH,'//input[@id="last-name"] | //input[@id="first-name"]')
sleep(3)
form.send_keys("Bravo")
sleep(5)
form.clear()
sleep(3)
form.send_keys("Again a Bravo!")
sleep(3)
'''
● 1 cu *
'''
chrome.find_element(By.XPATH,'//*[@id="last-name"]').send_keys("OK!!!")
sleep(3)
chrome.quit()
print("I went through all the selectors!")
'''
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
sleep(3)
id_list = chrome.find_elements(By.XPATH,"//*[@id]")
for i in id_list:
    print(i.get_attribute('id'))
chrome.quit()
'''
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
# //a[@href='#']//parent::li/div/a[5]/preceding-sibling::a[1]/following-sibling::a[3]
# Identific elementul inspectat in mod unic,apoi navighez catre parinte <li>
# apoi navighez catre copilul lui <li>,adica <div> si apoi catre al 5-lea copil lui <div> care este <a>[5]
# din <a>[5] merg in fratele anterior, la <a>[4]
# apoi merg din <a>[4] in urmatorul frate cu <a>[3],cu 3 frati mai in fata si ajung la <a>[7]

● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/autocomplete')
sleep(3)

def formy_input_by_placeholder(placeholder_text, input_value):
    my_input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter address', 'Eola Lake')
formy_input_by_placeholder('Street address', 'Main street number 2')
formy_input_by_placeholder('Street address 2', 'J.F.Kennedy street number 7')
formy_input_by_placeholder('City', 'Orlando')
formy_input_by_placeholder('State', 'Florida')
formy_input_by_placeholder('Zip code', '47^45')
formy_input_by_placeholder('Country', 'USA')
sleep(3)
chrome.quit()
'''

Exerciții extra - Opțional
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
eet/
'''
