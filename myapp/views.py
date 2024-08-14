from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse
from .forms import SupportRequestForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Category, Product, Order, contact
from .cart import Cart
from .forms import SignUpForm
import razorpay
from datetime import datetime

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_TEST_KEY_ID, settings.RAZORPAY_TEST_KEY_SECRET))

@login_required
def profile(request):
    return render(request, 'myapp/profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def checkout(request):
    cart = Cart(request)
    return render(request, 'checkout.html', {'cart': cart})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart_detail')

def Outlet(request):
    return render(request, 'Outlet.html')

def Services(request):
    return render(request, 'Services.html')

def stores(request):
    return render(request, 'stores.html')

@login_required
def verify_payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        signature = request.POST.get('razorpay_signature')
        order_id = request.POST.get('razorpay_order_id')
        
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            return redirect('payment_success')
        except Exception as e:
            print(f"Payment verification failed: {e}")
            return redirect('payment_failure')

    return redirect('checkout')

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'results': results})

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact =contact(name=name, email=email, phone=phone, desc=desc, date =datetime.today())
        contact.save()
    return render(request, 'contact.html')

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', {'form': form})




def support_request(request):
    if request.method == "POST":
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('support')
    else:
        form = SupportRequestForm()
    return render(request, 'support.html', {'form': form})




####
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_test_email(request):
    subject = 'Your Purchase Receipt from SHIBATECH'
    # Render the HTML message using a template
    html_message = render_to_string('order_confirmation_email.html', {'message': 'This is a test HTML email sent from Django.'})
    # Create a plain text version of the HTML message
    plain_message = strip_tags(html_message)

    # Recipient email list
    recipient_list = ['rupeshsardar459@gmail.com']  # Replace with your email address

    # Create the email message object
    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list
    )
    # Attach the HTML content to the email
    email.attach_alternative(html_message, "text/html")

    try:
        # Send the email
        email.send()
        return render(request, 'dashboard.html')
    except Exception as e:
        # Handle errors and provide feedback
        return HttpResponse(f'Failed to send email: {str(e)}')