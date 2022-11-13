from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def page_login(request):

    return render(request,'../../accounts/templates/login.html')
def create(request):
    return render(request,'../../accounts/templates/create.html')

#Inserção dos dados do usuário no banco

def store(request):
    data ={}
    try:
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2= User.objects.filter(password=request.POST['password'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        query_user=User.objects.get(id=user.id)
        usu= Usuario.objects.create(usuario=query_user,saldo=0)
        data['msg'] = 'Usuário Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'
    return render(request,'../../accounts/templates/login.html', data)
def painel(request):
    return render(request,'../../accounts/templates/painel.html')
#processa login

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        mode_user=User.objects.get(username=user)
        jogador=Usuario.objects.filter(usuario=mode_user.id)
        #print(jogador.saldo)
        login(request, user)
        return redirect('accounts:page_home')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'../../accounts/templates/login.html', data)

#Página inicial do dashboard
@login_required(redirect_field_name='next', login_url='dologing/')
def page_info(request):
    return render(request, '../../accounts/templates/info.html',{})
@login_required(redirect_field_name='next', login_url='dologing/')
def page_home(request):
    return render(request,'../../accounts/templates/home.html',{})
@login_required(redirect_field_name='next', login_url='dologing/')
def dashboard(request,valor):
    return render(request,'../../accounts/templates/dashboard/home.html',{'valor':valor})

#Logout do sistema
@login_required(redirect_field_name='next', login_url='dologing/')
def logouts(request):
    logout(request)
    return redirect('accounts:page_login')

#Alterar senha
@login_required(redirect_field_name='next', login_url='dologing/')
def changepass(request):
    form_senha = PasswordChangeForm(request.user)
    return render(request, '../../accounts/templates/alterar_senha.html',{'form_senha': form_senha})
@login_required(redirect_field_name='next', login_url='dologing/')
#alteração de senha
def changePassword(request):
    #verificação do método do formulário
    if request.method == "POST":
        #buscando dados de usuário e do formulário
        form_senha = PasswordChangeForm(request.user, request.POST)
        #validação do formulário
        if form_senha.is_valid():
            user = form_senha.save()
            #atualização da autenticação de sessão
            update_session_auth_hash(request, user)
            return redirect('accounts:page_home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return redirect('accounts:/changepass/')
    '''senha=request.POST.get("senha_atual")
    print(request.user.id)
    user=request.POST.get("usu")
    u = User.get_user_model(username=user)
    print(request.POST.get("nova_senha"))
    data=[]
    context={}
    if(u is not None):
        u.set_password(request.POST.get("nova_senha"))
        u.save()
        context={
            'msg':"Senha Alterada com Sucesso!",
            'class':"alert-success"
        }
    else:
        context={
            'msg':"Senha Antiga inválida!",
            'class':"alert-danger"
        }
    return reverse('accounts:/changepass/')'''
