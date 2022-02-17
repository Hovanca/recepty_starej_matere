from django import forms

# creating a form
class DifficultyForm(forms.Form):
    CHOICES = (
        ('1', 'Lahke'),
        ('2', 'Stredne'),
        ('3', 'Tazke'),
    )
    difficulty = forms.ChoiceField(choices=CHOICES) # toto tu je sketchy  default = '1')