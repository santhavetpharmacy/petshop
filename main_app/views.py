from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
# List of products (the same across locations in this example)
PRODUCTS = [
    'Pedigree',
    'Puripet',
    'Chains',
    'Belts',
    'Ropes',
    'Dog Eating Bones',    # Adjust text as needed.
    'Chew Sticks',
    'Dog Body Belts',
    'E Collars for Dogs',
    'Dog Mouth Caps',
    'Dog and Cat Catheter',
    'Fish food',
]

def thiruvarur(request):
    context = {
        'location': 'Thiruvarur',
        'products': PRODUCTS,
    }
    return render(request, 'location_products.html', context)

def thirupur(request):
    context = {
        'location': 'Thirupur',
        'products': PRODUCTS,
    }
    return render(request, 'location_products.html', context)

def trichy(request):
    context = {
        'location': 'Trichy',
        'products': PRODUCTS,
    }
    return render(request, 'location_products.html', context)

def cuddolore(request):
    context = {
        'location': 'Cuddolore',
        'products': PRODUCTS,
    }
    return render(request, 'location_products.html', context)
def results(request, location=None, product=None):
    context = {
        'rows': range(10),  # Renders 10 rows by default
        'location': location or 'Default Location',
        'product': product or 'Default Product'
    }
    return render(request, 'results.html', context)




