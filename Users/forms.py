from django import forms


class UploadExcelFileForm(forms.Form):  # форма загрузки ексель-файла
    file = forms.FileField(label='Загрузите excel-файл:',
                           widget=forms.FileInput(attrs={'class': "form-control",
                                                         'type': "file",
                                                         'id': "formFile",
                                                         'name': "file_form"}))

    def clean_file(self):               # валидатор самого файла(не данных в файле!!!)
        file = self.cleaned_data['file']
        print(file)


# class TableForm(forms.Form):
#     req_num = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id': "request_number"}))
#     full_name = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id': "full_name"}))
#     os_name = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"os_name"}))
#     tc_name = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"tc_name"}))
#     tc_pass = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"tc_pass"}))
#     group = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"group"}))
#     role = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"role"}))
#     lic_server = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"lic_server"}))
#     site = forms.CharField(widget=forms.TextInput(attrs={'type': "text",
#                                                             'class': "form-control",
#                                                             'id':"site"}))
#
#     def clean_req_num(self):
#         num = self.cleaned_data['req_num']
#         print(num)