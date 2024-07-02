from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import cv2
from PIL import Image

@csrf_exempt
def index(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        image = Image.open(file)
        image_np = np.array(image)

        colors = extract_colors(image_np)
        color_dict = {categories[i]: [color['r'], color['g'], color['b']] for i, color in enumerate(colors)}
        return JsonResponse(color_dict)

    return render(request, 'strip_analyzer/index.html')

categories = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

def extract_colors(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image_rgb.shape
    colors = []
    for i in range(10):
        x = int(width / 10 * (i + 0.5))
        color = image_rgb[:, x, :].mean(axis=0)
        colors.append({'r': int(color[0]), 'g': int(color[1]), 'b': int(color[2])})
    return colors
