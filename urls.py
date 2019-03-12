from django.conf.urls import url,include
from .views import KartView
from .views import UserView
from .views import OTPView
from .views import TokenView
from .views import EntryView,AuthView
app_name = 'dashkart'
urlpatterns = [
url(r'^dashkart/',KartView.as_view()),
url(r'^verifyOTP/',UserView.as_view()),
url(r'^requestOTP/',OTPView.as_view()),
url(r'^getAccessToken/',TokenView.as_view()),
url(r'^requestEntry/',EntryView.as_view()),
url(r'^gainEntry/',AuthView.as_view()),
]
