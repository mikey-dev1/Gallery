from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name = 'home'),
 path('create/',views.Create_Team, name ='create'),
 path('Team_Success/',views.Team_success, name = 'team_success'),
 path('book-list/',views.BookListView.as_view(), name = 'book-list'),

 path('book-create/',views.BookCreate.as_view(),name='book-create'),
 path('BookDetail/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),
 path('Book-update/<int:pk>/',views.BookUpdateView.as_view(),name='book-update'),
 path('Book-delete/<int:pk>/',views.BookDeleteView.as_view(),name='book-delete'),

 path('UserProfile/',views.UserProfile,name='UserProfile'),
 path('user-info/',views.UserProfile,name='user-info'),
 path('display/',views.Display_info,name='display'),
 path('signup/',views.SignUp,name='signup'),
 path('login/',views.Login.as_view(),name='login'),
 path('logout/',views.Logout.as_view(),name = 'logout'),

 path('password-reset/',views.PasswordReset.as_view(),name = 'PasswordReset'),
 path('PasswordResetDone/',views.PasswordResetDone.as_view(),name='password_reset_done'),
 path('PasswordResetComplete',views.PasswordResetComplete.as_view(),name='password_reset_complete'),
 path('PasswordResetConfirm/<uidb64>/<token>/',views.PasswordResetConfirm.as_view(),name='password_reset_confirm'),
]
