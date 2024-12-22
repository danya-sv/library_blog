from django import forms
from . import models, parsing

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('knigogod', 'knigogod'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type"
        ]

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'knigogod':
            knigogod_file = parsing.parsing()
            for i in knigogod_file:
                models.KnigoGid.objects.create(**i)