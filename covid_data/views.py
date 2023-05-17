import json
from django.http import JsonResponse
import requests
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


def covid_data(request):
    if request.method == 'GET':
        response = requests.get('https://api.covidtracking.com/v1/states/az/daily.json')
        data = response.json()
        positive_cases = []
        negative_cases = []
        today = int(datetime.today().strftime('%Y%m%d'))
        last_week = int((datetime.today() - timedelta(days=7)).strftime('%Y%m%d'))
        for each_day in data:
            if today >= int(each_day['date']) >= last_week:
                positive_cases.append(each_day['positiveIncrease'])
                negative_cases.append(each_day['negativeIncrease'])

        if not positive_cases and not negative_cases:
            return JsonResponse({'message': 'Data not available'})
        else:
            return JsonResponse({
                'positive_cases': sum(positive_cases),
                'negative_cases': sum(negative_cases)
            })
    else:
        return JsonResponse({
            'message': 'Error: Invalid request Method'
        })


@csrf_exempt
def covid_data_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        state = data.get('state', 'az')
        start_date = data.get('start_date')
        new_start_date = int(datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y%m%d'))
        end_date = data.get('end_date')
        new_end_date = int(datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y%m%d'))
        url = f'https://api.covidtracking.com/v1/states/{state}/daily.json'
        response = requests.get(url)
        data = response.json()
        positive_cases = []
        negative_cases = []
        for each_day in data:
            if new_start_date >= int(each_day['date']) >= new_end_date:
                positive_cases.append(each_day['positiveIncrease'])
                negative_cases.append(each_day['negativeIncrease'])

        if not positive_cases and not negative_cases:
            return JsonResponse({'message': 'Data not available'})
        else:
            return JsonResponse({
                'positive_cases': sum(positive_cases),
                'negative_cases': sum(negative_cases)
            })
    else:
        return JsonResponse({'message': 'Error: Invalid request method'})

