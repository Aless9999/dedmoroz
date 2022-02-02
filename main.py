
from bs4 import BeautifulSoup
import smtplib
import time
from config import mail, token, chat_id, sword
import requests

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) firefox/92.0.4515.159 Safari/537.36'}


name=[]


class Fox:
    def __init__(self):
        url = 'https://www.avito.ru/rossiya?p=1&q=%D0%B4%D0%B5%D0%B4+%D0%BC%D0%BE%D1%80%D0%BE%D0%B7+%D0%B3%D0%B8%D0%BF%D1%81&s=104'
             
        self.get_html(url)



    def get_html(self, url):
        self.html = (requests.get(url, headers=headers)).text
        self.work(self.html)


    def work(self, html):
        global name
        
        
        soup = BeautifulSoup(html, 'lxml') 
        items = soup.find_all('div', class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-ratingsRedesign-ydZfp items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
        for self.i in items:
            new_name = self.i.find('a', class_="link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH").text
            
            if 'мороз' in new_name:
                 
                
                if  name != new_name:
                    name = new_name                    
                    href = self.get_href()
                    print('Что-то новенькое!')
                    self.send_bot(new_name)
                    self.send_mail(href)
                    
                    break
                print('Ничего нового.')                
                break
                 
            

    def get_href(self):
        href ='https://www.avito.ru' +  self.i.find(class_="link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH").get('href')
        return href

        

    def send_mail(self, href):
        global sword
        sender = mail
        sword = sword

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(sender, sword)
            server.sendmail(sender, 'oksanaivano820@gmail.com', f"Subject:New!!!{href}")
            return "The message send successfully!"

        except Exception as ex:
            return f"{ex}\n Check your login or passeword please." 

    def send_bot(self,message):
        try:
            URL = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
            r = requests.get(URL)
            return "The message to Bot successfully!"
        except Exception as f:
            return f'{f} the wrong!'    
        
            

        






def main():
    while True:

        b = Fox()
        
        time.sleep(60)
    





if __name__ == '__main__':
    main()



   