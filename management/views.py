from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from database.models import Album, Transaction
from .forms import UserForm

# Create your views here.
class CreateAlbumView(TemplateView):
    model = Album

class ViewTransactionsView(ListView):
    model = Transaction

class CreateClientView(TemplateView):
    # def get_success_url(self):
    #     return ('settings:settings')
    #
    def post(self, request):
        uf = UserForm(request.POST, prefix='user')
        if uf.is_valid():  # check if both forms are valid
            user = uf.save()
            username = user.username
            password = request.POST['user-password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('settings:settings') #Redirect to user's general settings after sign up
        else:
            print uf.errors
            print pf.errors
            return self.render_to_response({'userform': uf, 'profileform': pf, 'view': self})
    #
    # def get(self, request):
    #     uf = UserForm(prefix='user')
    #     pf = ProfileForm(prefix='profile')
    #     return render_to_response(UserSignUpView.template_name,
    #                               dict(userform=uf,
    #                                    profileform=pf),
    #                               context_instance=RequestContext(request))

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(request=self.request, template=self.template_name, context=context, using=None, **response_kwargs)

class ViewAlbumsView(ListView):
    model = Album



