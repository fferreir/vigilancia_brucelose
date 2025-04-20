from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from .forms import UserEditForm, PerfilEditForm
from django.contrib import messages
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from conta.serializers import GroupSerializer, UserSerializer

@login_required
def dashboard(request):
    return render(
        request,
        'conta/dashboard.html',
        {'section': 'dashboard'}
    )

@login_required
def editar(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        perfil_form = PerfilEditForm(
            instance=request.user.perfil,
            data=request.POST
        )
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(
                request,
                'Perfil atualizado com sucesso'
            )
        else:
            messages.error(request, 'Erro ao atualizar o perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=request.user.perfil)
    return render(
            request,
            'conta/editar.html',
            {
                'user_form': user_form,
                'perfil_form': perfil_form,
            }
        )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]