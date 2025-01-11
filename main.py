import requests
from twilio.rest import Client
import os

account_sid = os.getenv("ACCOUNT_SID") 
auth_token = os.getenv("AUTH_TOKEN") 

#Api de Nocticias para estar al tanto de lo que secede con Tesla
def call_apinews():
    url_news = "https://newsapi.org/v2/top-headlines?"
    params_news = {
        "apikey": "0a00f5dff1af4578bbc15036c76e80db",
        "q": "Tesla"
    } 

    r = requests.get(url_news, params_news)
    data = r.json()
    

    title_article = {title['title']: title['description'] for title in data['articles']}

    return title_article

#Api Alpha obtengo datos diarios de los valores en el mercado de Tesla

def call_teslas():
    url_alpha = "https://www.alphavantage.co/query?"
    params = {
        "function":"TIME_SERIES_DAILY",
        "symbol":"TSLA",
        "apikey":"3W2KE0CBA9IQMATP",

    }

     
    response = requests.get(url_alpha,params)
    data = response.json()
    #Obtengo la ultima referencia actualizada desde la API
    today = data["Meta Data"]["3. Last Refreshed"]
    

    #Obtengo el diccionario con los datos mas recientes (Deberian ser los de hoy pero me muestra los datos intradiarios)
    close_tesla = data["Time Series (Daily)"][today]["4. close"]

    yesterday = list(data["Time Series (Daily)"].keys())[1] #obtengo la fecha del dia anterior para conseguir el close
    close_last_day = data["Time Series (Daily)"][yesterday]["4. close"]

    #Obtengo la diferencia positiva de los cierres
    positive_diference = abs(float(close_last_day) - float(close_tesla))
    percent = round((positive_diference / float(close_last_day)) * 100, 2)
    
    if percent > 5:
        return (f"TSLA: 🔺 {percent}")
    else:
        return (f"TSLA: 🔻 {percent}")

#Aqui estoy enviando los mensajes en el formato deseado
def send_messages():

    title_article = call_apinews()
    head_message = call_teslas()

    for i in title_article:
        title = i
        article = title_article[i]

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= (f"{head_message}\n Headline:{title}\n Brief:{article}"),
            from_= "+12695753914",
            to= "+5547991755381"
        )

    message.status


send_messages()



