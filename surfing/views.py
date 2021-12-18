from django.conf.urls import url
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as b

def index(request):
    return render(request , 'index.html')


def search(request):
    if request.method=='POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q='+search
        resp = requests.get(url)
        soup=b(resp.text , 'lxml')
        
        result = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        
        finalresult =[]
        for results in result:
            result_title = results.find(class_='PartialSearchResults-item-title').text
            result_url = results.find('a').get('href')
            result_desc = results.find(class_='PartialSearchResults-item-abstract').text
            
            finalresult.append((result_title, result_url, result_desc))
            
        context = {'finalresult':finalresult}
        
        
        
        return render(request , 'surfing.html', context)
    
    else:
        return render(request , 'surfing.html')



    