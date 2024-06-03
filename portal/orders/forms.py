from django import forms

from orders.models import Information, Sizes, Order, OrderHistory, HistoryDescription, SourseAssets
from users.models import MarketPlace

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class OrderCreationForm(forms.ModelForm):
    due_by = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "12",
    }))
    font = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Arial",
    }))
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control ",
        'placeholder' : "Love you Mom",
    }))
    instruction_for_worker = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "remove bg",
    }))
    x_size = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "120",
    }))
    y_size = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "144",
    }))
    z_size = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "20",
    }))
    sourse_files = MultipleFileField()



    # def __init__(self, user, *args, **kwargs):
    #     super(OrderCreationForm, self).__init__(*args, **kwargs)
    #     # Фільтрувати queryset для поля marketplace на основі користувача
    #     self.fields['marketplace_id'].queryset = MarketPlace.objects.filter(employer_id__user_id=user.id)

    #     # Використати випадаючий список для поля marketplace
    #     self.fields['marketplace_id'].widget = forms.Select(attrs={'class': 'form-control'})
    #     # Метод save() для збереження даних з усіх моделей

    def save(self, user, order_status_id, files, commit=True):
        order = super().save(commit=False)
        information = Information(
            due_by=self.cleaned_data['due_by'],
            font=self.cleaned_data['font'],
            text=self.cleaned_data['text'],
            instruction_for_worker=self.cleaned_data['instruction_for_worker'],
        )
        size = Sizes(
            x_size=self.cleaned_data['x_size'],
            y_size=self.cleaned_data['y_size'],
            z_size=self.cleaned_data['z_size'],
        )
        orderhistory = OrderHistory(
            order_id = order,
            history_description_id = HistoryDescription.objects.get(id=1),
            description = user.username
        )
      
        if commit:    
            order.marketplace_id = self.cleaned_data['marketplace_id']
            order.order_status_id = order_status_id
            order.save()
            information.order_id = order
            information.save()
            size.order_id = order
            size.save()

            orderhistory.save()
            for sourse in files:
                SourseAssets.objects.create(order_id=order, sourse_files=sourse)
        return order
    
    class Meta:
        model = Order
        fields = ['due_by', 'font', 'text', 'instruction_for_worker', 'x_size', 'y_size', 'z_size', 'marketplace_id', 'sourse_files']

