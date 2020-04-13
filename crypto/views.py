from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
    # Graps crypto price
    price_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,TRX,'
        'MIOTA&tsyms=USD')
    price = json.loads(price_request.content)
    # Graps crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    context = {
        'api': api,
        'price': price,
    }
    return render(request, 'index.html', context=context)


def prices(request):
    if request.method == 'Post':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,TRX,'
        'MIOTA&tsyms=USD')
        price = json.loads(crypto_request.content)
        context ={
            'quote': quote,
            'crypto': price,
        }
        return render(request, 'prices.html', context=context)
    else:
        not_found = 'Type currency in search box'
        return render(request, 'prices.html', {'not_found': not_found})
