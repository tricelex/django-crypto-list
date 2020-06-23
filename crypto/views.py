from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    import requests
    import json

    # grab crypto price data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP,BCH,BSV,LTC,BNB,EOS,"
        "CRO&tsyms=USD")
    price = json.loads(price_request.content)

    # grab crypto news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'crypto/home.html', {'api': api, 'price': price})


def about(request):
    return HttpResponse('Hello About Page')


def prices(request):
    if request.method == 'POST':

        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()
        # grab crypto quote data
        crypto_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD')
        crypto = json.loads(crypto_request.content)

        return render(request, 'crypto/prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a cryptocurrency in the form above!"
        return render(request, 'crypto/prices.html', {'notfound': notfound})
