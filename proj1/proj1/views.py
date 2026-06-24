from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import userForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def userform(request):
    fn = userForm()
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    output = n1 + n2
    data = {'form': fn,
            'output' : output                     
        }
    # try:
    #     if request.method == "POST":
    #         # n1 = int(request.GET['num1'])
    #         # n2 = int(request.GET['num2'])
    #         output = 0
            
    #         n1 = int(request.POST.get('num1'))
    #         n2 = int(request.POST.get('num2'))
    #         print(n1+n2)
    #         output = n1+n2
    #         data = {
    #             "n1" : n1,
    #             "n2" : n2,
    #             "output" : output
    #         }
    # except Exception:
    #     print(Exception)
    return render(request, 'userform.html', data)

def form2(request):
    data = {}
    output = 0
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        output = n1+n2
        data = {
            "n1" : n1,
            "n2" : n2,
            "output" : output
        }
        url = '/thankyou/?output={}'.format(output)
        return HttpResponseRedirect(url)

    except Exception:
        print(Exception)
    return render(request, 'form2.html', data)

def thankyou(request):
    if request.method == 'GET':
        ans = int(request.GET.get('output'))
    return render(request, 'thankyou.html', {"ans" : ans})

def submitform(request):
    data = {}
    output = 0
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        output = n1+n2
        data = {
            "n1" : n1,
            "n2" : n2,
            "output" : output
        }
        
        return HttpResponse(output)

    except Exception:
        print(Exception)



def calculator(request):
    data = {}
    result = 0
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            ope = request.POST.get('ope')

            if ope == '+':
                result = n1+n2
            elif ope == '-':
                result = n1-n2
            elif ope == '*':
                result = n1*n2
            elif ope == '/':
                result = n1/n2
        data = {
            "output" : result,
            'n1' : n1,
            'n2' : n2 
        }
    except Exception:
        print(Exception)
    return render(request, 'calculator.html', data)


def evenodd(request):
    data= {}
    try:
        if request.method == 'POST':
            value = int(request.POST.get('value'))
            if (value%2 == 0):
                c = 'green'
            else:
                c = 'red'
        print(c)
    
        data = {
            "style" : c,
            'value' : value
        }
    except Exception:
        print(Exception)
    return render(request, 'evenodd.html',data)

def marksheet(request):
    total = 0
    percentage = 0
    data = {}
    bgcolor = ""
    try:
        if request.method == 'POST':
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            total = s1+s2+s3+s4+s5
            percentage = (total/500) * 100
            print(f"Total: {total}, Percentage {percentage}")
            if total >= 400:
                remark = "You are G.O.A.T"
                bgcolor = 'box-green'
            elif total >=300:
                remark = 'Time to become a G.O.A.T'
                bgcolor = 'box-lgreen'
            elif total >= 200:
                remark = 'todaa awrr padahi karlee bhaii'
                bgcolor = 'box-yello'
            elif total >= 100:
                remark = "Need to imporve lot baby"
                bgcolor = 'box-lred'
            else:
                remark = 'Gand marwaa bosdikkkeeeee'
                bgcolor = 'box-red'
            data = {
                "total" : total,
                'percentage' : percentage,
                's1' : s1,
                's2' : s2,
                's3' : s3,
                's4' : s4,
                's5' : s5,
                'remarks' : remark,
                'bgcolor' : bgcolor
            }
            return render(request, 'marksheet.html',data)
    except Exception as e:
        print(e)
    return render(request, 'marksheet.html',data)