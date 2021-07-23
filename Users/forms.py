from django import forms


class UploadExcelFileForm(forms.Form):
    file = forms.FileField(label='Загрузите excel-файл:',
                           widget=forms.FileInput(attrs={'class': "form-control",
                                                         'type': "file",
                                                         'id': "formFile",
                                                         'name': "file_form"}))

    def clean_file(self):
        file = self.cleaned_data['file']
