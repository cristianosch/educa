from django.urls import path 
from . import views

urlpatterns = [ 
    path('mine/', views.ManageCourseListView.as_view(),
        name='manage_course_list'),#pode ser a pagina de adiçao de mes

    path('create/', views.CourseCreateView.as_view(),
        name='course_create'),# criaçao de mes

    path('<pk>/edit/', views.CourseUpdateView.as_view(),
        name='course_edit'),# pode ser a pagina de adiçao de paineis

    path('<pk>/delete/',views.CourseDeleteView.as_view(),
        name='course_delete'),
         
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
        name='course_module_update'), #pode ser a pagina de adição de visitas

    path('module/<int:module_id>/content/<model_name>/create/',views.ContentCreateUpdateView.as_view(),
        name='module_content_create'),

    path('module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(),
        name='module_content_update'),

    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(),
        name='module_content_delete'),

    path('module/<int:module_id>/', views.ModuleContentListView.as_view(),
        name='module_content_list'),

    path('module/order/',views.ModuleOrderView.as_view(),
        name='module_order'),

    path('content/order/',views.ContentOrderView.as_view(),
        name='content_order'),

    # ***NOVO CAPITULO RENDERIZANDO E FAZENDO CACHING DE CONTEUDO*** 
    
    path('subject/<slug:subject>/',
         views.CourseListView.as_view(),
         name='course_list_subject'),

    path('<slug:slug>/',
         views.CourseDetailView.as_view(),
         name='course_detail'),
    ]

