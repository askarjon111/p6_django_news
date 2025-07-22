from django import forms

from news.models import Category, New


class AddNewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=Category.objects.all())

    class Meta:
        model = New
        fields = ['title', 'image', 'content', 'category']

    def form_valid(self, form):
        self.object = form.save()

        # Does not redirect if valid
        #return HttpResponseRedirect(self.get_success_url())

        # Render the template
        # get_context_data populates object in the context 
        # or you also get it with the name you want if you define context_object_name in the class
        return self.render_to_response(self.get_context_data(form=form))