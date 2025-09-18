from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import permission_required
# Create your views here.
from myapp.models import Flowers, Category,Tag
from myapp.forms import MyForm


def index(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q == "":
        flowers = Flowers.objects.all()
    elif q is not None:
        flowers = Flowers.objects.filter(title__contains=q)
    context = {
        'flowers':flowers
    }
    return render(request, 'myapp/index.html', context)


def tags(request, slug=None):
    flowers = Flowers.objects.filter(tags__slug=slug)
    context = {
        'flowers':flowers,
    }
    return render(request,'myapp/index.html', context)

@permission_required('myapp.add_flower')
def detail_page(request, slug=None):
   
    # if slug is not None:
    #     #print(f'your slug = {slug}')
    #     try:
    #         flower = get_object_or_404(Flowers,slug=slug)
    #         #get flowers from the same category
    #         related_flowers = flower.category.flowers.exclude(id=flower.id)
    #         print(f'related flowers: {related_flowers}')
    #     except Flowers.DoesNotExist:
    #         raise Http404
    #     # except Flowers.MultipleObjectsReturned:
    #     #     flower = Flowers.objects.filter(slug=slug).first()
    #     except:
    #         raise Http404

    flower = get_object_or_404(Flowers, slug=slug)
    #print(f'\n{flower}')
        
        

    context = {
        'flower':flower,
        #'relatd_flowers':related_flowers,
    }
    return render(request, 'myapp/detail.html', context)


# edit page function

def create_page(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyForm()
        return render(request, 'myapp/edit.html', {'form': form})
    return render(request, 'maypp/edit.html', {'form': form})


@permission_required('myapp.change_flower')
def edit_page(request, pk=None):
    flower = get_object_or_404(Flowers, pk=pk)

    if request.method == 'POST':
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyForm(instance=flower)    
        return render(request, 'myapp/edit.html', {
            'flower':flower,
            'form':form,
        })
    
    return render(request, 'myapp/edit.html', {
        'flower':flower,
        'form':form,
    })


@permission_required('myapp.change_delete')
def delete_flower(request, pk=None):
    flower = get_object_or_404(Flowers, pk=pk)
    flower.delete()

    

    return redirect('index')
    