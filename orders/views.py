from django.shortcuts import render
from .models import OrderItem,Order
from cart.cart import Cart
from django.db.models import Q

def order_create(request):
    return render(request,'create.html')


def order_submit(request):
    cart = Cart(request)

    order = Order.objects.create(
            user=request.user,
        )

    for item in cart:
        OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
         )
    cart.clear()
    print("sad")
    context = {
       'order': order,
    }
    return render(request, 'created.html', context)



def allorders(request):
    order = Order.objects.all()
    if(str(request.user) == 'user1'):
        myorders = OrderItem.objects.filter(order__user__name = 'USERBD')
        print(myorders)
    else:
        myorders = OrderItem.objects.filter(order__user=request.user)
        print('abc')
        print(myorders)
    context={
        'myorders':myorders,
    }
    return render(request,'myorders.html',context)