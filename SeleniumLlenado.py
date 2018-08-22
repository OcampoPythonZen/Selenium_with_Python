# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parse import cargar_MA

path="Análisis de la Reforma Educativa FINAL_lleno.xlsx"
respuestas=cargar_MA(path)
ciclos_form=input('¿Cuantas veces deseas repetir el llenado del Formulario...?')
browser=webdriver.Firefox()
contador=0

for value in range(ciclos_form):
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLScxQ4C23V76ZvrjJRht9av3XkEwaPiVvlSPoEMqro7IIAomAA/viewform')
    #Comienzan la secion de preguntas
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_1'])+"]/div/div/div[3]/div").click()
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_2'])+"]/div/div[2]/div/span").click()
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_3'])+"]/div/div/div[3]/div").click()
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div[2]/div/div/div/div[2]/label["+str(respuestas[contador]['respuesta_4'])+"]/div/div/div[2]").click()
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[5]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_5'])+"]/div[2]/div/div[3]/div").click()
    #Pregunta 6 corresponde a la linea 1 del csv
    elem=browser.find_element_by_name("entry.1920169819")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_6'])
    elem=browser.find_element_by_name("entry.2022717484")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_7'])
    elem=browser.find_element_by_name("entry.16071643")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_8'])
    elem=browser.find_element_by_name("entry.165221516")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_9'])
    elem=browser.find_element_by_name("entry.1528781447")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_10'])
    elem=browser.find_element_by_name("entry.107299143")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_11'])
    elem=browser.find_element_by_name("entry.1509909816")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_12'])
    elem=browser.find_element_by_name("entry.1814293369")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_13'])
    # #Sexta seccion del formulario En qué grado ayuda la Reforma Educativa para que tus alumnos se enfrenten a las problemáticas actuales?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[14]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_14'])+"]/div[2]/div/div[3]/div").click()
    elem=browser.find_element_by_name("entry.1760830110")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_15'])
    #¿Qué impacto genera en usted el resultado que obtenga en la evaluación?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[16]/div[2]/div/div/div/div[2]/label["+str(respuestas[contador]['respuesta_16'])+"]").click()
    #¿Qué beneficios consideras que tendrán los resultados de tu evaluación en el aprendizaje de los alumnos?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[17]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_17'])+"]/div/div/div[3]/div").click()
    #¿En qué medida te sientes capacitado para desarrollar competencias en los alumnos?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[18]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_18'])+"]/div[2]/div/div[3]/div").click()
    #¿En qué medida la Reforma Educativa ha impulsado tus competencias laborales?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[19]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_19'])+"]/div[2]/div/div[3]/div").click()
    #¿Consideras que ha incrementado la equidad (igualdad de oportunidades) en el acceso a una educación de calidad?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[20]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_20'])+"]/div[2]/div/div[3]/div").click()
    #¿Consideras que el Servicio Profesional Docente respeta los derechos laborales de los maestros?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[21]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_21'])+"]/div/div/div[3]/div").click()
    elem=browser.find_element_by_name("entry.1168978003")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_22'])
    #¿La Reforma Educativa propicia nuevas oportunidades para el desarrollo profesional de docentes y directivos?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[23]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_23'])+"]/div").click()
    elem=browser.find_element_by_name("entry.1076322982")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_24'])
    #¿En qué medida la Reforma Educativa contribuye a la mejora de la calidad de la educación?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[25]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_25'])+"]/div[2]/div/div[3]/div").click()
    elem=browser.find_element_by_name("entry.1849181866")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_26'])
    #¿En qué medida la Reforma Educativa ha impulsado el desarrollo de los aprendizajes clave para una educación integral de los alumnos?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[27]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_27'])+"]/div[2]/div/div[3]/div").click()
    #¿En qué ves reflejado respecto a la pregunta anterior?
    elem=browser.find_element_by_name("entry.687460884")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_28'])
    #¿En qué medida la Reforma Educativa ha influido en la capacitación en tu desarrollo profesional?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[29]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_29'])+"]/div[2]/div/div[3]").click()
    #¿Consideras que tu escuela está preparada para una educación inclusiva?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[30]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_30'])+"]/div/div/div[3]/div").click()
    #porque
    elem=browser.find_element_by_name("entry.750414666")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_31'])
    #¿En qué ha beneficiado la Reforma Educativa en la infraestructura de la institución en la que laboras
    elem=browser.find_element_by_name("entry.214993482")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_32'])
    #¿Consideras que el gasto en la educación es suficiente?
    browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[33]/div[2]/div/content/div/label["+str(respuestas[contador]['respuesta_33'])+"]/div").click()
    elem=browser.find_element_by_name("entry.1185106134")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_34'])
    elem=browser.find_element_by_name("entry.1445202280")
    elem.clear()
    elem.send_keys(respuestas[contador]['respuesta_35'])
    browser.find_element_by_css_selector("span.quantumWizButtonPaperbuttonLabel.exportLabel").click()
    contador=contador+1
    print contador
browser.quit()
