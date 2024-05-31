from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import requests
import openai
import os

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/index.html'

    
openai.api_key='sk-ZtIuK62G4fb' #앞서 자신이 부여받은 API key를 넣으면 된다. 절대 외부에 공개해서는 안된다.

def get_completion(prompt): 
	print(prompt) 
	query = openai.ChatCompletion.create( 
		model="gpt-3.5-turbo",
		messages=[
        	{'role':'user','content': prompt}
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 
	response = query.choices[0].message["content"]
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 


class HistoryView(TemplateView):
    template_name = 'main/myhistory.html'
