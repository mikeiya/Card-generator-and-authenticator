from django.http import HttpResponse, JsonResponse
from .card_functions import card_is_valid,get_card_info,generate_card

def authenticator(request):
    card = {}
    if 'card_number' in request.GET:
        card_number = str(request.GET['card_number'])
        #uses sessions as a cache
        is_cached = (card_number in request.session)
        if not is_cached:
            valid_card,check_digit = card_is_valid(card_number)
            if  valid_card:
                get_card_info(card,card_number)
                card['check_digit'] = check_digit
            else:
                card = {card_number:'Invalid card'}
            request.session['card_number'] = card
    else:
    	return JsonResponse({'status':'missing card_number in the request'},status=404)
    return JsonResponse(request.session['card_number'])

def generator(request):
	card = {}
	if 'visa' in request.GET:
		try:
			count = int(request.GET['visa'])
		except:
			return JsonResponse({'status':'invalid number of visa cards to generate'},status=404)
		card['card_numbers'] = list(generate_card('visa') for i in range(count))
		card['type'] = 'visa'
	elif 'mastercard' in request.GET:
		try:
			count = int(request.GET['mastercard'])
		except:
			return JsonResponse({'status':'invalid number of mastercard cards to generate'},status=404)
		card['card_numbers'] = list(generate_card('mastercard') for i in range(count))
		card['type'] = 'mastercard'
	elif 'amex' in request.GET:
		try:
			count = int(request.GET['amex'])
		except:
			return JsonResponse({'status':'invalid number of amex cards to generate'},status=404)
		card['card_numbers'] = list(generate_card('amex') for i in range(count))
		card['type'] = 'amex'
	else:
		card['card_number'] = generate_card()
	return JsonResponse(card)

