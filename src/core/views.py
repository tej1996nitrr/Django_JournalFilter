from django.shortcuts import render
from core.models import Journal,Category
from django.db.models import Q
# Create your views here.
def is_valid_queryparam(param):
    return  param !='' and param is not None 

def BootstrapFilterView(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_author')
    view_count_max = request.GET.get('ViewCountMax')
    view_count_min = request.GET.get('ViewCountMin')
    pDateMin = request.GET.get('pDateMin')
    pDateMax = request.GET.get('pDateMax')
    category = request.GET.get('Category')
    reviewed = request.GET.get('reviewed')
    notreviewed = request.GET.get('notreviewed')


    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)
    elif is_valid_queryparam(title_exact_query):
        qs = qs.filter(id= title_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)|Q(author__name__icontains= title_or_author_query)).distinct()

    if is_valid_queryparam(view_count_min):
         qs = qs.filter(views__gte = view_count_min) #greater than or  equal to
    if is_valid_queryparam(view_count_max):
         qs = qs.filter(views__lt = view_count_max) #less than or equal to
    
    if is_valid_queryparam(pDateMin):
         qs = qs.filter(publish_date__gte = pDateMin )
    if is_valid_queryparam(pDateMax):
         qs = qs.filter(publish_date__lt = pDateMax )
    if is_valid_queryparam(category) and  category!="Choose...":
        qs= qs.filter(categories__name = category)
    if reviewed=='on':
        qs = qs.filter(reviewed=True)
    elif notreviewed=='on':
        qs = qs.filter(reviewed=False)
    
    
    
    context={
        'queryset':qs,
        'categories': categories
    }
    

    return render(request,"Bootstrap_form.html",context)