# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

contador=0
ciclos_form=input('¿Cuantas veces deseas repetir el llenado del Formulario...?')
browser=webdriver.Firefox()
for value in range(ciclos_form):
	browser.get('https://docs.google.com/forms/d/1yB200K7BRD4aET-_eKbqZl3UsN6Eh9p64VCAMlnM_so/viewform?edit_requested=true')
	#Comienzan la secion de preguntas
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div/div[2]/div/content/div/label["+str(random.randint(1,4))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/content/div/label["+str(random.randint(1,2))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label["+str(random.randint(1,2))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div[2]/div/content/div/label["+str(random.randint(1,4))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[5]/div[2]/div/content/div/label["+str(random.randint(1,3))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[6]/div[2]/div["+str(random.randint(1,4))+"]/div/label/div/div/div[2]").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[7]/div[2]/div/content/div/label["+str(random.randint(1,5))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[8]/div[2]/div/content/div/label["+str(random.randint(1,4))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[9]/div[2]/div/content/div/label["+str(random.randint(1,4))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[10]/div[2]/div/content/div/label["+str(random.randint(1,3))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[11]/div[2]/div/content/div/label["+str(random.randint(1,5))+"]/div/div/div[3]/div").click()
	browser.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div/content/span").click()
	contador=contador+1
	print contador
browser.quit()
