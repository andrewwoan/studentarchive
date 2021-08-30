from django.urls import path
from . import views

urlpatterns = [
    path('graduateprofiles', views.profiles, name='profiles'),
    path('undergraduateprofiles', views.profiles_undergrad,
         name='profiles_undergrad'),
    path('alumprofiles', views.profiles_alum,
         name='profiles_alum'),
    path('private/<str:username>/', views.userProfile2,
         name='private-profile'),
    path('researchstaffprofiles', views.profiles_res,
         name='profiles_res'),
    path('postdocprofiles', views.profiles_postdocs,
         name='profiles_post'),
    path('publications/', views.publications, name='publications'),
    path('profile/<str:username>/', views.userProfile, name='user-profile'),

    path('your-account/', views.userAccount, name='account'),
    path('edit-your-account/', views.editAccount, name='edit-account'),
    #     path('update-skills/<str:pk>', views.modifySkills, name='modify-skills'),
    path('add-publication/', views.addPublication, name='add-publication'),
    path('update-publication/<str:pk>/',
         views.updatePublication, name='update-publication'),
    path('delete-publication/<str:pk>/',
         views.deletePublication, name='delete-publication'),
    path('add-presentation/', views.addPresentation, name='add-presentation'),
    path('update-presentation/<str:pk>/',
         views.updatePresentation, name='update-presentation'),
    path('delete-presentation/<str:pk>/',
         views.deletePresentation, name='delete-presentation'),



    path('sign-in/', views.signIn, name='login'),
    path('sign-out/', views.signOut, name='logout'),
    path('change-password/', views.changePassword, name='change-password'),
]
