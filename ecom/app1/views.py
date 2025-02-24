from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from app1.models import reg_form,login,productad,cart,ordermaster,orderchild
import datetime

def home(request):
    template=loader.get_template("home.html")
    context={}
    return HttpResponse(template.render(context,request))
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('passw')
        if login.objects.filter(username=username,passw=passw):
         l=login.objects.get(username=username,passw=passw)
         if l.utype =='user':
          request.session["uid"]=l.uid_id
          return HttpResponse("<script>alert('WELCOME USER');window.location='/userhm';</script>")
         elif l.utype =='admin':
          return HttpResponse("<script>alert('WELCOME ADMIN');window.location='/adminhm';</script>")
         else:
          return HttpResponse("<script>alert('Invalid User Type');window.location='/login';</script>")

        else:
            return HttpResponse("<script>alert('Invalid Username or Password');window.location='/login';</script>")
    else:
       template=loader.get_template("login.html")
       context={}
       return HttpResponse(template.render(context,request))
    
def reg_form_view(request):
    if request.method == 'POST':
        r = reg_form()
        r.name = request.POST.get('name')
        r.gender = request.POST.get('gender')
        r.phone = request.POST.get('phone')
        r.email = request.POST.get('email')
        r.save()
        id = reg_form.objects.latest("id").id
        l = login()
        l.username = request.POST.get("username")
        l.passw = request.POST.get("password")
        l.utype='user'
        l.uid_id=id
        l.save()
        return HttpResponse("<script>alert('Registration Successfull');window.location='/reg_form';</script>")
    else:
        template=loader.get_template("reg_form.html")
        context={}
        return HttpResponse(template.render(context,request))
def adminhm(request):
   template=loader.get_template("adminhm.html")
   context={}
   return HttpResponse(template.render(context,request))
def index(request):
   template=loader.get_template("index.html")
   context={}
   return HttpResponse(template.render(context,request))
def productadd(request):
   if request.method == 'POST':
      p = productad()
      p.prname = request.POST.get('name')
      p.category=request.POST.get('category')
      p.price=request.POST.get('price')
      p.image = request.FILES['image']
      p.description=request.POST.get('description')
      p.save()
      return HttpResponse("<script>alert('Product Added Successfully');window.location='/productadd';</script>")
   else:
    template=loader.get_template("productadd.html")
    context={}
    return HttpResponse(template.render(context,request))

def userhm(request):
    products = productad.objects.all()
    context = {'products': products}
    return render(request, 'userhm.html', context)
def productdet(request,id):
   request.session["pid"]=id 
   v=productad.objects.get(id=id)
   template=loader.get_template('productdet.html')
   context={'product':v}
   return HttpResponse(template.render(context,request))
def carts(request, id):
    if request.method == 'POST':
        c = cart()
        product = productad.objects.get(id=id)
        c.date = datetime.datetime.now()
        c.qty = int(request.POST.get("quantity"))
        c.total = c.qty * float(product.price)
        c.pid = product
        c.uid_id = request.session["uid"]
        c.save()
        return HttpResponse("<script>alert('Item added to cart');window.location='/listcart';</script>")
    return redirect('/productdet')



def listcart(request):
    if request.method == 'POST':
        user_id = request.session.get("uid")
        cart_items = cart.objects.filter(uid_id=user_id)

        if cart_items.exists():

            o = ordermaster()
            o.uid_id = user_id
            o.date = datetime.datetime.now()
            o.total = sum(item.total for item in cart_items) 
            o.save()


            for item in cart_items:
                orderchild.objects.create(
                    oid_id=o.id,
                    pid_id=item.pid_id,
                    qty=item.qty,
                    total=item.total,
                    status='Completed',
                )

            # Clear the cart
            cart_items.delete()

            return HttpResponse("<script>alert('Order placed successfully');window.location='/orderview';</script>")
        else:
            return HttpResponse("<script>alert('Cart is empty!');window.location='/listcart';</script>")
    else:
 
        user_id = request.session.get("uid")
        cart_items = cart.objects.filter(uid_id=user_id)
        total_price = sum(item.total for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }
        return render(request, 'cart.html', context)

def orderview(request):
    user_id = request.session.get('uid')
    orders = ordermaster.objects.filter(uid_id=user_id).order_by('-date')
    for order in orders:
        order.order_children = order.orderchild_set.all()
    context = {
        'orders': orders,
    }
    return render(request, 'order.html', context)


def remove_from_cart(request, item_id):
    item = get_object_or_404(cart, id=item_id)
    item.delete()
    return redirect('listcart')
def delete_order(request, order_child_id):
    if request.method == "POST":
        order_child = get_object_or_404(orderchild, id=order_child_id)
        order_child.delete()
        return redirect('orderview')

