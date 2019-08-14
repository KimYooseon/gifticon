from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UploadFileForm
from .models import UploadFileModel
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import mainapp.views
from mainapp.models import category 
from django.core.paginator import Paginator
from django.utils import timezone



@login_required
def upload_file(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            categorys = category.objects.all()

            post = form.save(commit=False)
            post.user_id = request.user.username
            post.pub_date=timezone.datetime.now()
            post.productimg_name = str(post.pbrand)+''+str(post.pitem)

            for ctg in categorys:
                if(ctg.brand == post.pbrand):
                    if(ctg.item == post.pitem):
                        post.originalprice = ctg.originalprice
                        post.productimg = ctg.file
            post.save()
            ufl = UploadFileModel.objects

            product_list = UploadFileModel.objects.all()
            paginator = Paginator(product_list, 6)
            page = request.GET.get('page')
            posts = paginator.get_page(page)
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
