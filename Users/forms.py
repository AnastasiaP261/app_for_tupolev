from django import forms


class UploadExcelFileForm(forms.Form):  # форма загрузки ексель-файла
    file = forms.FileField(required=False,
                           label='Загрузите excel-файл:',
                           widget=forms.FileInput(attrs={'class': "form-control",
                                                         'type': "file",
                                                         'id': "formFile",
                                                         'name': "file_form"}))

    def clean_file(self):  # валидатор самого файла(не данных в файле!!!)
        file = self.cleaned_data['file']
        print(file)


class TableForm(forms.Form):
    req_num = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={'type': "text",
                                                            'class': "form-control",
                                                            'id': "request_number",
                                                            'autocomplete': 'off',
                                                            }))
    full_name = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'type': "text",
                                                              'class': "form-control",
                                                              'id': "full_name",
                                                              'onchange': 'os_name_auto_fill(this)',
                                                              'autocomplete': 'off',
                                                              }))
    os_name = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={'type': "text",
                                                            'class': "form-control",
                                                            'id': "os_name",
                                                            'autocomplete': 'off',
                                                            }))
    tc_name = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={'type': "text",
                                                            'class': "form-control",
                                                            'id': "tc_name",
                                                            'placeholder': "авт.",
                                                            'autocomplete': 'off',
                                                            }))
    tc_pass = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={'type': "text",
                                                            'class': "form-control",
                                                            'id': "tc_pass",
                                                            'autocomplete': 'off',
                                                            'placeholder': "авт.",
                                                            }))
    group = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'type': "text",
                                                          'class': "form-control",
                                                          'id': "group",
                                                          'autocomplete': 'off',
                                                          }))
    role = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type': "text",
                                                         'class': "form-control",
                                                         'id': "role",
                                                         'autocomplete': 'off',
                                                         }))
    lic_server = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'type': "text",
                                                               'class': "form-control",
                                                               'id': "lic_server",
                                                               'autocomplete': 'off',
                                                               'placeholder': "начните ввод...",
                                                               'list': "lic_list",
                                                               }))
    site = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'type': "text",
                                                         'class': "form-control",
                                                         'id': "site",
                                                         'autocomplete': 'off',
                                                         'placeholder': "начните ввод...",
                                                         'list': "site_list",
                                                         }))

    def clean_req_num(self):
        num = self.cleaned_data['req_num']
        print(num)


TableFormSet0 = forms.formset_factory(TableForm, max_num=None, extra=0)
TableFormSet1 = forms.formset_factory(TableForm, max_num=None, extra=1)
# параметр extra определяет сколько пустых форм будет выведено, в случае с формой предзаполненной из файла нам не нужны
# пустые формы, а в случае с начальной пустой формой нужна одна
