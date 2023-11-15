from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, UserWallet
from library.models import Purchases, Files
from django.conf import settings
from accounts.models import User

def initiate_payment(request):

    if request.method == "GET":
        book_id = request.session.get('selected_book_id')
        book = get_object_or_404(Files, pk = book_id) # Replace book_id with the book's primary key.
        amount = float(book.price) 
        email = email = request.user.email

        pk = settings.PAYSTACK_PUBLIC_KEY

        payments = Payment.objects.filter(email = email, verified=False)
        if payments:
           payments.delete()
           
        payment = Payment.objects.create(amount=amount, email=email, user=request.user)
        payment.save()

        context = {
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': pk,
            'amount_value': payment.amount_value(),
            'book': book
        }
        return render(request, 'payment.html', context)
        # return render(request, 'make_payment.html', context)
    
    else:
       
        return render(request, 'payment.html', context={'book': book})
    
        
    


def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    if verified:
        # user_wallet = UserWallet.objects.get(user=request.user)
        # user_wallet.balance += payment.amount
        # user_wallet.save()
        
        #  # Assuming you have the user and book objects.
        user = request.user
        book_id = request.session.get('selected_book_id')
        book = get_object_or_404(Files, pk = book_id) # Replace book_id with the book's primary key.

        # Create a purchase record
        purchase = Purchases(user=user, book=book)
        purchase.save()
        
        return redirect('mylibrary')
    return render(request, "success.html")