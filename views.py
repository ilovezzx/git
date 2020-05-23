from django.http import HttpResponse

def index(request):
    return render('index.html')


print(random.randint(1,100))
