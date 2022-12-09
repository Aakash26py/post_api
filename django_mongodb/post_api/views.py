from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import xlwt

from django.http import HttpResponse
from xlutils.copy import copy
from xlrd import open_workbook 

import os
# Create your views here.

class PersonAPI(APIView):
    def post(self, request, format=None):
        serializer= PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "sucess"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"status": "Failed"}, status = status.HTTP_400_BAD_REQUEST)

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'dob', 'country']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Person.objects.all().values_list('name', 'dob', 'country')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response