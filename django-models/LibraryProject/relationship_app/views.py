from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm   # ✅ THIS LINE IS REQUIRED
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # ✅ Using built-in form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
