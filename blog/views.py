from django.shortcuts import render
from django.shortcuts import render,render_to_response, get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
# import pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Entry,Category



def index(request):
    posts = Entry.objects.all().order_by('created').reverse()
    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all();



    return render(request, 'index.html', {'posts': posts,'categories': categories})

def view_post(request, slug):
    post = get_object_or_404(Entry, slug=slug)

    return render(request, 'view_post.html', {'post': post})


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'posts': Entry.objects.filter(category=category)[:5]
    })

    return render(request, 'index.html', {'posts': posts,'categories': categories})



def search(request):
    import bleach
    search_string = bleach.clean(request.POST.get('searchString'))

    objects = Entry.objects.all()

    from model_search import model_search
    posts = model_search(search_string, objects, ['title','body'])

    return render(request,'index.html',{'posts' : posts })

