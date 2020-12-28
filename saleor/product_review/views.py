from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductReview


# Create your views here.
def index(request):
    x = []
    for i in range(10):
        x.append(i)
    print(request.GET.keys())
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x)+ str(request.POST.keys()))


# class ReviewsList(ListView):
#     model = ProductReview

# class ReviewView(DetailView):
#     model = ProductReview

# class ProductReviewCreate(CreateView):
#     model = ProductReview
#     fields = ['name', 'pages']
#     success_url = reverse_lazy('book_list')

# class ProductReviewUpdate(UpdateView):
#     model = ProductReview
#     fields = ['name', 'pages']
#     success_url = reverse_lazy('book_list')

# class ProductReviewDelete(DeleteView):
#     model = ProductReview
#     success_url = reverse_lazy('book_list')