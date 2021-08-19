from selenium import webdriver
from time import sleep

#Getting the url
driver = webdriver.Chrome(executable_path="E:\\Datos\\Escritorio\\Proyectos\\Proyectos2021\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.reddit.com/r/Unclejokes/")
sleep(3)



# Scrolling down
i=0
for i in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1.5)
    i = i + 1
    print(i)

#asd

#Getting all the jokes

jokes =  driver.find_element_by_css_selector("div.rpBJOHq2PR60pnwJlUyP0").find_elements_by_css_selector("div._1oQyIsiPHYt6nx7VOmd1sz")
print("La cantidad de jokes es")
print(len(jokes))

#Writing each joke in a txt file
i = 0
fileTxt = open("jokes.txt","w+")

for joke in jokes:
    tittle = joke.find_element_by_css_selector("h3._eYtD2XCVieq6emjKBH3m").get_attribute("textContent")
    contenido = joke.find_element_by_css_selector("div.STit0dLageRsa2yR4te_b").get_attribute("textContent")
    i = i + 1
    print(i)
    try:
        fileTxt.write(tittle)
        fileTxt.write("\n")
        fileTxt.write(contenido)
        fileTxt.write("\n \n \n")
    except:
        print("NO anda")


fileTxt.close()


