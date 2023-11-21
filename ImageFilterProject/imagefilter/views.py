from django.shortcuts import render
from .forms import FilterForm
from PIL import Image, ImageFilter
from django.conf import settings
import os
import cv2
import numpy as np

def apply_filter(image_path, filter_option):
    image = cv2.imread(image_path)

    if filter_option == 'gray':
        filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_option == 'blur':
        filtered_image = cv2.GaussianBlur(image, (15, 15), 0)
    elif filter_option == 'edge':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_option == 'sharpen':
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        filtered_image = cv2.filter2D(image, -1, kernel)
    elif filter_option == 'emboss':
        
        kernel = np.array([[-2, -1, 0],
                           [-1,  1, 1],
                           [ 0,  1, 2]])
        filtered_image = cv2.filter2D(image, -1, kernel)
    else:
        
        filtered_image = image



    filtered_image_path = os.path.join(settings.MEDIA_ROOT, 'filtered_image.jpg')
    cv2.imwrite(filtered_image_path, filtered_image)

    return filtered_image_path

def filter_image(request):
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            filter_option = form.cleaned_data['filter_option']
            
           
            uploaded_image = request.FILES['image']
            
            
            uploaded_image_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
            with open(uploaded_image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)
            
            
            filtered_image_path = apply_filter(uploaded_image_path, filter_option)
            
            
            
            os.remove(uploaded_image_path)

            filtered_image_name = os.path.basename(filtered_image_path)

            return render(request, 'imagefilter/result.html', {'filtered_image_name': filtered_image_name})
    else:
        form = FilterForm()

    return render(request, 'imagefilter/filter_image.html', {'form': form})
