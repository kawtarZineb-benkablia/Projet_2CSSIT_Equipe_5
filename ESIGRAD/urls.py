from django.urls import path
from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url('index/', views.index),
    url('upload/',views.upload),
    url('test/',views.test),
    url('ajouterRubrique/',views.créerRub, name="créerub"),
    url('gestionRubrique/',views.GestionRub, name="gestionrub"),
    path('renommer_rub/<str:rub_id>/',views.renommerRub, name='renommerRub'),
    path('supprimer_rub/<int:rub_id>/',views.supprimerRub, name='deleteRub'),
    path('supprimer_rep/<int:rep_id>/',views.supprimerRep, name='deleteRep'),
    url('gestionRepertoire/',views.GestionRep, name="gestionrep"),
    url('ajouterRepertoire/',views.créerRep, name="créerep"),
    url('gestionUser/',views.gestionUser , name="gestionUser"),
    url('ajouterUser/',views.créerUser, name="créerUser"),
    path('supprimer_user/<int:user_id>/<str:type>/',views.supprimerUser, name='deleteUser'),
    path('renommer_rep/<int:rep_id>/',views.renommerRep, name='renommerRep'),
    path('index_user_prem/',views.index_user_1, name='index_user_prem'),
    path('index_user/<int:rub_id>/',views.index_user_2, name='index_user'),
    path('popup_ren/<int:rub_id>/',views.popup_ren, name='popup'),
    path('popup_ren_rep/<int:rep_id>/',views.popup_ren_rep, name='popup_ren_rep'),
    path('popup_del/<int:user_id>/<str:type>/',views.popup_del, name='popup_delete'),
    url('authentification/',views.affich_authentif,name="autho"),
    url('redirectPage/', views.authentification, name="authentification"),
    path('popup_del_rub/<int:rub_id>/',views.popup_del_rub, name='popup_delete_rub'),
    path('popup_del_rep/<int:rep_id>/',views.popup_del_rep, name='popup_delete_rep'),
    path('popup_del_doc/<int:pk>/',views.popup_del_doc, name='popup_delete_doc'),
    path('GestionDocSimple/',views.Liste_doc_simple),
    path('GestionDocPréviligié/<int:pk>/index_userP_Doc',views.Liste_doc_préviligié),
    path('GestionDocPréviligié/Ajouter_document/',views.Ajouter_document,name='Ajouter_document'),
    
    path('GestionDocPréviligié/<int:pk>/',views.delete_Doc,name='delete_Doc'),
    url('GestionDocPréviligié/',views.Liste_doc_préviligié2), 
    path('GestionDocPréviligié/',views.Liste_doc_préviligié2,name='liste_doc_priv'), 
    path('index_user4/<int:rep_id>/',views.Liste_doc_préviligié, name='index_user4'),
    path('index_user2/<int:rub_id>/',views.index_userP_2, name='index_userP'),
    path('index_user_Prev/',views.index_userP_1, name='index_user_Prev'),
    path('index_user3/<int:rep_id>/',views.Liste_doc_simple, name='index_user3'), 
]


