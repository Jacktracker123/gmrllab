from django.urls import path
from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('package/', views.package,name='package'),
    path('package_view/<str:name>', views.packages_view, name='packages_view'),
    path("package_view/<str:name>/payment/", views.order_payment, name="payment"),
    path("razorpay/callback/", views.callback, name="callback"),
    path('blog/', views.blog,name='blog'),
    path('branch/', views.branches,name='branch'),
    path('branches_view/<str:name>', views.branches_view,name='branches_view'),
    path('branch_packages/<str:name>', views.branch_packages,name='branch_packages'),
    path('branch_package_view/<str:name>', views.branches_package_view,name='branch_package_view'),
    path('gallery/', views.gallery,name='gallery'),
    path('moleculor-biology/', views.moleculor_biology,name='moleculor-biology'),
    path('radiology/', views.radiology,name='radiology'),
    path('test/', views.test,name='test'),
    path('contact-us/', views.contact,name='contact-us'),
    path('appointment/', views.appointment,name='appointment'),
    path('department/', views.department,name='department'),
    path('privacy-policy/', views.privacy_policy,name='privacy-policy'),
    path('terms&conditions/', views.terms_conditions,name='terms&conditions'),
    path('testimonials/', views.testimonials,name='testimonials'),
    path('register/', views.register,name='register'),
    path('accounts/login/', views.login, name='login'),
    path('logout/', views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('admin_page/', views.admin_page,name='admin_page'),
    path('admin_branches/', views.admin_branches, name='admin_branches'),
    path('admin_branch_view/<str:name>', views.admin_branch_view, name='admin_branch_view'),
    path('admin_packages/', views.admin_packages,name='admin_packages'),
    path('admin_packages_add/', views.admin_package_add,name='admin_packages_add'),
    path('admin_packages_update/', views.admin_package_update,name='admin_packages_update'),
    path('admin_appointments_view/', views.admin_appointments_view,name='admin_appointments_view'),
    path('admin_package_view/<str:name>', views.admin_package_view, name='admin_package_view'),
     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
 path('profile_update/',views.profile_update,name="profile_update"),
path('orders/',views.order,name="orders"),

    
    


    

    

  



   

















]