
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("num1")
        n2=from_data.get("num2")
        result=n1+n2
        print(request_body)
        data={
            "sum":result     
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("num1")
        n2=from_data.get("num2")
        result=n1-n2
        print(request_body)
        data={
            "add":result     
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("num1")
        n2=from_data.get("num2")
        result=n1*n2
        print(request_body)
        data={
            "mul":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')    
class DivisionView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("num1")
        n2=from_data.get("num2")
        result=n1/n2  
        data={
            "Div":result
        }
        return JsonResponse(data) 


@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("num1")
        n2=from_data.get("num2")
        result=n1%n2  
        data={
            "Mod":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        n1=from_data.get("obtained_mark")
        n2=from_data.get("total_mark")
        result=(n1/n2)*100  
        data={
            "Percentage":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        w=from_data.get("weight")
        h=from_data.get("height")
        height_in_meters=h/100
        result=w/(height_in_meters*height_in_meters)
        data={
            "BMI":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class TriangleView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        b=from_data.get("base")
        h=from_data.get("height")
        result=1/2*b*h
        data={
            "area":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class AgeCalculateView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        current_year=from_data.get("current_year")
        birth_year=from_data.get("birth_year")  
        result=current_year-birth_year
        data={
            "age":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class simpleInterestView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        p=from_data.get("principal")
        r=from_data.get('rate')
        t=from_data.get('time')
        result=(p*r*t)/100
        data={
            "simple_interest":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ElectricityBillView(View):
    def post(self,request):
        request_body=request.body
        from_data=loads(request_body)
        u=from_data.get('units')
        r=from_data.get('rate')
        result=u*r
        data={
            "bill":result
        }
        return JsonResponse(data)