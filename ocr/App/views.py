from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from cnocr import CnOcr
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

def aaa(request):
    if request.method=='GET':
        return render(request,'aaa.html')
    file=request.FILES.get('file')
    b=b''
    for c in file.chunks():
        b+=c
    try:
        ocr = CnOcr()
    except:
        pass
    sep = ','
    img_data = plt.imread(BytesIO(b), "png")
    # print(type(img_data))
    # print(img_data.shape)
    image = img_data[:, :, :3]
    # print(image.shape)
    image = (image * 255).astype(np.int)
    try:
        res = ocr.ocr_for_single_line(image)
        msg=sep.join(res).replace(',', '')
        data={
            'code':200,
            'msg':msg
        }
        return JsonResponse(data)
    except:
        msg='图片名含有非转义字符，建议使用数字字母的形式'
        data={
            'code':400,
            'msg':msg
        }
        return JsonResponse(data)