from django.shortcuts import render
from .models import Candidate, StudentProfile
from django.contrib.auth.models import User
from .models import Union, UnionForm
from .forms import UnionRegisteration

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def createUnion(request):

    if request.method == 'POST':
        form = UnionRegisteration(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
            return render(request, 'invalidlogin.html',{'r':2})
        else:
            print(form.errors)
            return render(request, 'invalidlogin.html',{'r':1})
    else:
        form = UnionRegisteration()
        return render(request, 'createUnion.html',{'form':form})

def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('capp:userLogin'))
            else:
                return render(request, 'notactive.html')
        else:
            print('Someone tried to login')
            print('username: {} password: {}'.format(username,password))
            return render(request, 'invalidlogin.html',{'r':1})
    else:
         return render(request, 'login.html')

@login_required
def userLogout(request):

    logout(request)
    return HttpResponseRedirect(reverse('capp:userLogin'))

@login_required
def userInfo(request):

    a=StudentProfile.objects.order_by('S_ID')
    username = request.user.username
    u = str(username)
    dic={}
    for i in a:
        b=i.user
        c=str(b)
        if c == u:
            std=i
            dic = {'std':std}
    
    return render(request,'userInfo.html',context=dic)

def approve(request):
    if request.method == 'POST':
        ufid = request.POST.get('union_id')
        ufname = request.POST.get('union_name')
        ufhead = request.POST.get('head')
        ufm1 = request.POST.get('m1')
        if ufm1:
            try :
                std = StudentProfile.objects.get(S_ID=ufm1)
                # print(std.S_NAME)
            except:
                return render(request, 'invalidlogin.html',{'r':1})
        ufm2 = request.POST.get('m2')
        if ufm2:
            try :
                std = StudentProfile.objects.get(S_ID=ufm2)
                # print(std.S_NAME)
            except:
                return render(request, 'invalidlogin.html',{'r':1})
        ufm3 = request.POST.get('m3')
        if ufm3:
            try :
                std = StudentProfile.objects.get(S_ID=ufm3)
                # print(std.S_NAME)
            except:
                return render(request, 'invalidlogin.html',{'r':1})
        ufm4 = request.POST.get('m4')
        if ufm4:
            try :
                std = StudentProfile.objects.get(S_ID=ufm4)
                # print(std.S_NAME)
            except:
                return render(request, 'invalidlogin.html',{'r':1})
        ufm5 = request.POST.get('m5')
        if ufm5:
            try :
                std = StudentProfile.objects.get(S_ID=ufm5)
                # print(std.S_NAME)
            except:
                return render(request, 'invalidlogin.html',{'r':1})
        
        std = StudentProfile.objects.get(S_ID = ufhead)
        u=Union(head=std,UNION_ID=ufid,UNION_NAME=ufname)
        u_saved = u.save()
        un = Union.objects.get(UNION_ID=ufid)
        print(un.UNION_ID)
        head_cand = Candidate(USN = std,U_NAME=ufname)
        head_cand_saved = head_cand.save()
        
        std1 = StudentProfile.objects.get(S_ID = ufm1)
        cand1 = Candidate(USN=std1, U_NAME=ufname)
        cand1_save=cand1.save()

        std2 = StudentProfile.objects.get(S_ID = ufm2)
        cand2 = Candidate(USN=std2, U_NAME=ufname)
        cand2_save=cand2.save()
        
        std3 = StudentProfile.objects.get(S_ID = ufm3)
        cand3 = Candidate(USN=std3, U_NAME=ufname)
        cand3_save=cand3.save()
        
        std4 = StudentProfile.objects.get(S_ID = ufm4)
        cand4 = Candidate(USN=std4, U_NAME=ufname)
        cand4_save=cand4.save()
        
        std5 = StudentProfile.objects.get(S_ID = ufm5)
        cand5 = Candidate(USN=std5, U_NAME=ufname)
        cand5_save=cand5.save()

        x = UnionForm.objects.filter(UNION_ID=ufid)
        x.delete()


        
        newUnionForm = UnionForm.objects.filter()
        return render (request, 'approve.html', {'unions':newUnionForm})
    
        
    else:    
    
        unionForm = UnionForm.objects.filter()   
        return render (request, 'approve.html', {'unions':unionForm})

def unionView(request):

    u = Union.objects.order_by('UNION_ID')
    c = Candidate.objects.order_by('USN')
    return render(request, 'union.html',{'union':u, 'candidate':c})

def students(request):

    x = StudentProfile.objects.order_by('S_ID')
    y = Union.objects.order_by('UNION_ID')
    z = Candidate.objects.order_by('USN')
    return render(request, 'student.html', {'student':x, 'union':y, 'cand':z})

def rules(request):
    return render(request, 'rules.html')

def vote(request):
    return render(request, 'vote.html')

def viewVote(request):
    return render(request, 'viewVote.html')

