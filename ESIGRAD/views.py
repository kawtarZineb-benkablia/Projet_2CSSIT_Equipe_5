from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.core.files.storage import FileSystemStorage
from .models import Document
from .models import *
from django.contrib import messages #import messages
from datetime import datetime
from time import strftime
from django.core.mail import send_mail
 
 

# Create your views here.
def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def upload (request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
       # print(uploaded_file.name)
       # print( uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        context['nom'] = name
    return render (request,'upload.html',context)

def documents_list(request):
    documents = Document.objects.all()
    return render(request,'documents_list.html',{'documents':documents})


def upload_documents(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        taille=uploaded_file.size/1000
        doc = Document (nom_doc = uploaded_file.name,taille=taille,propriétaire='aaa',emplacement=context['url'],fichier=uploaded_file)
        doc.save()
       # print(uploaded_file.name)
       # print( uploaded_file.size)
         
       
        return redirect('documents_list.html')
         
    else : 
     return render(request,'upload_documents.html')

# NOUVEAU


def test(request:HttpRequest):
    return render(request,"dialog.html")
 
def Liste_doc_simple(request:HttpRequest,rep_id):
    idRep=rep_id
    rep= Répertoire.objects.get(id=idRep) 
    nom_rep=rep.nom_rep 
    rub_list=Rubrique.objects.all().order_by('id')
    if 'q' in request.GET:
         q=request.GET['q']
         documents = Document.objects.filter(répertoire_id=idRep).filter(nom_doc__icontains=q).order_by('-date_création')
    else:
         documents = Document.objects.filter(répertoire_id=idRep).order_by('-date_création')
    
    return render(request,'index_user_Doc.html',{'documents':documents,'nom_rep':nom_rep,'rub_list':rub_list,'id_us':id_us})

 
def Liste_doc_préviligié(request:HttpRequest,rep_id):
    global idRep 
    idRep=rep_id
    rep= Répertoire.objects.get(id=idRep) 
    rub_list=Rubrique.objects.all().order_by('id')
    nom_rep=rep.nom_rep 
    if 'q' in request.GET:
         q=request.GET['q']
         documents = Document.objects.filter(répertoire_id=idRep).filter(nom_doc__icontains=q).order_by('-date_création')
    else:
         documents = Document.objects.filter(répertoire_id=idRep).order_by('-date_création')
    
    return render(request,'index_userP_Doc.html',{'documents':documents,'nom_rep':nom_rep,'rub_list':rub_list,'id_us':id_us})
def Liste_doc_préviligié2(request:HttpRequest):
    rep= Répertoire.objects.get(id=idRep) 
    nom_rep=rep.nom_rep
    rub_list=Rubrique.objects.all().order_by('id') 
    if 'q' in request.GET:
         q=request.GET['q']
         documents = Document.objects.filter(répertoire_id=idRep).filter(nom_doc__icontains=q).order_by('-date_création')
    else:
         documents = Document.objects.filter(répertoire_id=idRep).order_by('-date_création')
    
    return render(request,'index_userP_Doc.html',{'documents':documents,'nom_rep':nom_rep,'rub_list':rub_list,'id_us':id_us})

def delete_Doc(request,pk):
     if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
        messages.success(request, "Le document a été supprimé avec succes !!")
    
        
     return redirect('/ESIGRAD/GestionDocPréviligié/')
def documents_list(request):
    documents = Document.objects.all()
    return render(request,'index_userP_Doc.html',{'documents':documents})
  
def Ajouter_document(request):  
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        taille=uploaded_file.size/1000
        doc = Document (nom_doc = uploaded_file.name,taille=taille, propriétaire=id_us,emplacement=context['url'],répertoire_id=idRep,fichier=uploaded_file)
        doc.save()
        messages.success(request, "Le document a été ajoutée avec succes !!")
        notif = request.POST['selectReponse']
        if notif=='Oui':
           users = Utilisateur.objects.all()
           for user in users:
               try:
                send_mail('[ESIGRAD]Nouveau document ajouté',"Un nouveau document est ajouté dans ESIGRAD:"+doc.nom_doc,'EsiGradDPGR@gmail.com',[user.email],fail_silently=False)
               except Exception as e:
                   messages.error(request,"Vérifiez votre connexion; l'email de notification n'a pas été envoyé")
        return redirect('index_userP_Doc.html')
        
         
    else : 
     return render(request,'index_userP_Doc.html')
    

def créerRub(request:HttpRequest):
    if request.method == 'POST':
        nom_rub = request.POST['nom_rub']
        if nom_rub=='':
            print("error")
            messages.error(request, "Veuillez donner le nom de la rubrique")
        else:
            if(Rubrique.objects.filter(nom_rub=nom_rub).exists()==True):
                messages.error(request, "Il existe déja une rubrique avec ce nom ")
            else:
                rub= Rubrique(nom_rub=nom_rub)
                rub.save()
                messages.success(request, "La rubrique a été ajoutée avec succes !!")
    return redirect('/ESIGRAD/gestionRubrique/')
#####################################################
def renommerRub(request,rub_id):
    rub_to_rename= Rubrique.objects.get(id=int(rub_id))
    if request.method == 'POST':
        nv_nom_rub = request.POST['nv_nom_rub']
        if (Rubrique.objects.filter(nom_rub=nv_nom_rub).exists()==True  ):
            messages.error(request, "Il existe déja une rubrique ayant ce nom !!") 
        else:
            rub_to_rename.nom_rub = nv_nom_rub
            rub_to_rename.save()
            messages.success(request, "La rubrique a bien été renommée !!") 
    return redirect('/ESIGRAD/gestionRubrique/')
###########################################""
def popup_ren(request,rub_id):
     context= {'rub_list':Rubrique.objects.all().order_by('id'),'rub_id':rub_id}
     return render(request,"index_admin_rub_popup.html",context)
def popup_del(request,user_id,type):
     context= {'user_id':user_id,'type':type}
     return render(request,"index_admin_user_popup_delete.html",context)
def popup_del_rub(request,rub_id):
     context= {'rub_id':rub_id}
     return render(request,"index_admin_rub_popup_delete.html",context)
def popup_del_rep(request,rep_id):
     context= {'rep_id':rep_id}
     return render(request,"index_admin_rep_popup_delete.html",context)
def popup_ren_rep(request,rep_id):
    context= {'rep_id':rep_id}
    return render(request,"index_admin_rep_popup.html",context)
############################################""""""
def supprimerRub(request,rub_id):
    rub_to_delete= Rubrique.objects.get(id=rub_id)
    rub_to_delete.delete()
    messages.success(request, "La rubrique a bien été supprimée !!") 
    return redirect('/ESIGRAD/gestionRubrique/')
    ##################################"
def supprimerRep(request,rep_id):
    rep_to_delete= Répertoire.objects.get(id=rep_id)
    rep_to_delete.delete()
    messages.success(request, "Le répèrtoire a bien été supprimé !!") 
    return redirect('/ESIGRAD/gestionRepertoire/')
def popup_del_doc(request,pk):
     context= {'pk':pk}
     return render(request,"doc_popup_delete.html",context)
#######################################################
def GestionRub(request):
     
    if 'q' in request.GET:
        q=request.GET['q']
        context= {'rub_list':Rubrique.objects.all().filter(nom_rub__icontains=q).order_by('id'),'id_rub':0,'id_us':id_us}
    else:
        context= {'rub_list':Rubrique.objects.all().order_by('id'),'id_rub':0,'id_us':id_us}
    return render(request,'index_admin_Rub.html',context)
#####################################################
def test(request:HttpRequest):
    return render(request,"login.html")
########################Rep##########################
def GestionRep(request):
    if 'q' in request.GET:
        q=request.GET['q']
        context= {'rub_list':Rubrique.objects.all(),'rep_list':Répertoire.objects.all().filter(nom_rep__icontains=q),'id_us':id_us}
    else:
        context= {'rub_list':Rubrique.objects.all(),'rep_list':Répertoire.objects.all(),'id_us':id_us }
    return render(request,'index_admin_Rep.html', context)
###########################################
def créerRep(request:HttpRequest):
    if request.method == 'POST':
        nom_rub_selected = request.POST['selectRub']
        nom_rep = request.POST['nom_rep']
        if (Répertoire.objects.filter(nom_rep=nom_rep,rubrique=Rubrique.objects.get(nom_rub=nom_rub_selected)).exists()==True  ):
            messages.error(request, "Il existe déja un répertoire ayant ce nom dans cette rubrique!!") 
        else:
            
            rub=Rubrique.objects.get(nom_rub=nom_rub_selected)
            rep= Répertoire(nom_rep=nom_rep,rubrique= rub)
            rep.save()
            messages.success(request, "Le répertoire a bien été ajouté!!") 
    return redirect('/ESIGRAD/gestionRepertoire/')
    ######################################""
def renommerRep(request,rep_id):
    rep_to_rename= Répertoire.objects.get(id=rep_id)
    if request.method == 'POST':
        nv_nom_rep = request.POST['nv_nom_rep']
        rep_to_rename.nom_rep = nv_nom_rep
        rep_to_rename.save()
        messages.success(request, "Le répèrtoire a bien été renommé!!") 
    return redirect('/ESIGRAD/gestionRepertoire/')
    ########################################""
def gestionUser(request):
    if 'q' in request.GET:
        q=request.GET['q']
        context= {'user_list_simple':Utilisateur_simple.objects.all().filter(nom_utilisateur__icontains=q).order_by('id'),'user_list_prév':Utilisateur_privilégié.objects.all().filter(nom_utilisateur__icontains=q).order_by('id'),'id_us':id_us}
    else:
        context= {'user_list_simple':Utilisateur_simple.objects.all().order_by('id'),'user_list_prév':Utilisateur_privilégié.objects.all().order_by('id'),'id_us':id_us}
    return render(request,'index_admin_User.html',context)
    #############################################
def créerUser(request:HttpRequest):
    if request.method == 'POST':
        nom_utilisateur = request.POST['nom_utilisateur']
        mdp =  request.POST['mdp']
        email =  request.POST['mail']
        type =  request.POST['type']
        if nom_utilisateur=='' or mdp=='' or email=='' :
            print("error")
            messages.error(request, "Veuillez renseigner tous les champs")
        else:
            try:
                send_mail('[ESIGRAD] Ajout de votre compte',"Votre compte a été ajouté dans l'application ESIGRAD, vous pouvez y connecter maintenant avec votre adresse email et avec le mot de passe suivant:"+mdp,'EsiGradDPGR@gmail.com',[email],fail_silently=False)
                if (Utilisateur_privilégié.objects.filter(email=email).exists()==True  ) or (Utilisateur_simple.objects.filter(email=email).exists()==True  ) :
                    messages.error(request, "Il existe déja un utilisateur possédant cet email")
                else:
                    if type=="simple" :
                        user= Utilisateur_simple(nom_utilisateur=nom_utilisateur,mot_de_passe=mdp , email=email, status="Utilisateur simple",adresse="ldkfkdfldflkk")
                        user.save()
                        messages.success(request, "L'utilisateur a bien été ajouté!!") 
                    else:
                        user= Utilisateur_privilégié(nom_utilisateur=nom_utilisateur,mot_de_passe=mdp , email=email, status="Utilisateur préviligié",adresse="ldkfkdfldflkk")
                        user.save()
                        messages.success(request, "L'utilisateur a bien été ajouté!!")
            except Exception as e:
                messages.error(request,e)
             
            
             
    return redirect('/ESIGRAD/gestionUser/')

    #############################################
def supprimerUser(request,user_id,type):
    if type=="Utilisateur simple":
        user_to_delete= Utilisateur_simple.objects.get(id=user_id)
        user_to_delete.delete()
        messages.success(request, "L'utilisateur a bien été supprimé!!") 
    else:
        user_to_delete= Utilisateur_privilégié.objects.get(id=user_id)
        user_to_delete.delete()
        messages.success(request, "L'utilisateur a bien été supprimé!!")
    return redirect('/ESIGRAD/gestionUser/')
    ######################################
def index_user_1(request:HttpRequest):
    
    rub1=Rubrique.objects.first()
    if 'q' in request.GET:
        q=request.GET['q']
        context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub1).filter(nom_rep__icontains=q,),'id_us':id_us}
    else:
        context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub1),'id_us':id_us}

    return render(request,"index_user.html",context )
    #########################################
def index_user_2(request:HttpRequest,rub_id):
    rub1=Rubrique.objects.first()
    rub=Rubrique.objects.get(id=rub_id)
    if 'q' in request.GET:
        q=request.GET['q']
        context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub).filter(nom_rep__icontains=q),'id_us':id_us}
    else:
        context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub),'id_us':id_us}

    return render(request,"index_user.html",context )

def récupererId(request, rub_id):
    context={'id_rub':rub_id}
    print("rub_id")
    return render(request,"index_admin_Rub.html",context )
    ########################
    
def affich_authentif(request):
    return render(request,"authentification.html")
    ####################################
 
def authentification(request):
    global id_us 
    if request.method == 'POST':
        mdp =  request.POST['mdp']
        email =  request.POST['email']
        if (mdp=="" or email==""):
            messages.error(request, "veuillez donner l'mail et le mot de passe")
        else:
            if (Utilisateur_simple.objects.filter(email=email).exists()==True):
                user=Utilisateur_simple.objects.get(email=email)
                id_us=user.nom_utilisateur
                if(user.mot_de_passe==mdp):
                    context={'auth':True,'mail':email}
                    return redirect('/ESIGRAD/index_user_prem/',context)
                else:
                    messages.error(request, "Mot de passe incorrect")
                    return redirect('/ESIGRAD/authentification/')
            else:
                if (Utilisateur_privilégié.objects.filter(email=email).exists()==True):
                    userP=Utilisateur_privilégié.objects.get(email=email)
                    id_us=userP.nom_utilisateur
                    if(userP.mot_de_passe==mdp):
                        context={'auth':True,'mail':email}
                        return redirect('/ESIGRAD/index_user_Prev/',context)
                    else:
                        messages.error(request, "Mot de passe incorrect")
                        return redirect('/ESIGRAD/authentification/')
                else:
                    if (Utilisateur_admin.objects.filter(email=email).exists()==True):
                        userP=Utilisateur_admin.objects.get(email=email)
                        id_us=userP.nom_utilisateur
                        if(userP.mot_de_passe==mdp):
                            context={'auth':True,'mail':email}
                            return redirect('/ESIGRAD/gestionUser/',context)
                        else:
                            messages.error(request, "Mot de passe incorrect")
                            return redirect('/ESIGRAD/authentification/')
                        
                    else:
                        messages.error(request, "Ce compte n'existe pas")
                        return redirect('/ESIGRAD/authentification/')


def index_userP_1(request:HttpRequest):
    rub1=Rubrique.objects.first()
    if 'q' in request.GET:
         q=request.GET['q']
         context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub1).filter(nom_rep__icontains=q),'id_us':id_us}
    else:
         context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub1),'id_us':id_us}
    return render(request,"index_userP.html",context )

def index_userP_2(request:HttpRequest,rub_id):
    rub1=Rubrique.objects.first()
    rub=Rubrique.objects.get(id=rub_id)
    if 'q' in request.GET:
         q=request.GET['q']
         context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub).filter(nom_rep__icontains=q),'id_us':id_us}
    else:
         context= {'rub_list':Rubrique.objects.all(),'rub1':rub1,'rep_list':Répertoire.objects.filter(rubrique=rub),'id_us':id_us}
    return render(request,"index_userP.html",context )


