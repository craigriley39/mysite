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

    posts =  Entry.objects.filter(category=category)

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

    categories = Category.objects.all()

    return render(request, 'index.html', {'posts': posts, 'categories': categories})





def search(request):
    import bleach
    search_string = bleach.clean(request.POST.get('searchString'))

    objects = Entry.objects.all()

    from model_search import model_search
    posts = model_search(search_string, objects, ['title','body'])

    return render(request,'index.html',{'posts' : posts })



## Form views

# myblog/views.py
from .forms import EntryModelForm

    # id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=255)
    # body = models.TextField()
    # slug = models.SlugField()
    # image = models.ImageField(null=True,blank=True,upload_to='static/images/')
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # objects = SearchManager(['title','body'])

def add_entry(request):
    if request.method == 'GET':
        form = EntryModelForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = EntryModelForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():

            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            slug = form.cleaned_data['slug']
            #created = form.cleaned_data['created']
            created_by = form.cleaned_data['created_by']
            post = Entry.objects.create(title=title,body=body,image=image,category=category,created_by=created_by)
            #return HttpResponseRedirect(reverse(', kwargs={'post_id': post.id}))
            return redirect('/blog')

    return render(request, 'create_blog.html', {
        'form': form,
    })

def error_404(request):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)

