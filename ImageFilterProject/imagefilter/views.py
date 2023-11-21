from django.shortcuts import render
from .forms import FilterForm
from PIL import Image, ImageFilter
from django.conf import settings
import os

def apply_filter(image_path, filter_option):
    image = Image.open(image_path)
    if filter_option == 'filter1':
        # Применяем первый фильтр
        image = image.filter(ImageFilter.BLUR)
    elif filter_option == 'filter2':
        # Применяем второй фильтр
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_option == 'filter3':
        # Применяем третий фильтр
        image = image.filter(ImageFilter.SHARPEN)

    # Сохраняем отфильтрованное изображение
    filtered_image_path = os.path.join(settings.MEDIA_ROOT, 'filtered_image.jpg')
    image.save(filtered_image_path)
    return filtered_image_path

def filter_image(request):
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            filter_option = form.cleaned_data['filter_option']
            
            # Получаем загруженное изображение
            uploaded_image = request.FILES['image']
            
            # Сохраняем загруженное изображение в директории media
            uploaded_image_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
            with open(uploaded_image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)
            
            # Применяем фильтр к изображению
            filtered_image_path = apply_filter(uploaded_image_path, filter_option)
            
            
            # Удаляем загруженное изображение после обработки, если это необходимо
            os.remove(uploaded_image_path)

            filtered_image_name = os.path.basename(filtered_image_path)

            # Передаем имя файла в шаблон
            return render(request, 'imagefilter/result.html', {'filtered_image_name': filtered_image_name})
    else:
        form = FilterForm()

    return render(request, 'imagefilter/filter_image.html', {'form': form})
