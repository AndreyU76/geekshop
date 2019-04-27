from django.shortcuts import render

def main(request):
    context = {'name':  'Андрей'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

