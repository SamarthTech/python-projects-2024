from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'foody_1'

urlpatterns = [
    url(r"^login/$", auth_views.LoginView.as_view(template_name="foody_1/login.html"),name='login'),
    url(r"^northindian/$", views.NorthIndianView.as_view(), name="northindian"),
    url(r"^southindian/$", views.SouthIndianView.as_view(), name="southindian"),
    url(r"^italian/$", views.ItalianView.as_view(), name="italian"),
    url(r"^chinese/$", views.ChineseView.as_view(), name="chinese"),
    url(r"^continental/$", views.ContinentalView.as_view(), name="continental"),
    url(r"^fastfood/$", views.FastFoodView.as_view(), name="fastfood"),
    url(r"^beverages/$", views.beveragesView.as_view(), name="bev"),
    url(r"^deserts/$", views.desView.as_view(), name="des"),
    url(r"^confused/$", views.ConfusedView.as_view(), name="confused"),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    url(r"^result/$", views.resultpage, name="result"),


    url(r"^confused/happy/$", views.HappyView, name="happy"),
    url(r"^confused/angry/$", views.AngryView, name="angry"),
    url(r"^confused/dehydrate/$", views.DehydrateView, name="dehydrate"),
    url(r"^confused/depress/$", views.DepressiveView, name="depress"),
    url(r"^confused/excite/$", views.ExciteView, name="excite"),
    url(r"^confused/unwell/$", views.UnwellView, name="unwell"),


    url(r"^chinese/noodles/$", views.ChineseNoodlesView, name="noodles"),
    url(r"^chinese/chillyPaneer/$", views.ChineseChillyPaneerView, name="chillyPaneer"),


    url(r"^continental/ham/$", views.ContinentalHamView, name="ham"),
    url(r"^continental/springroll/$", views.ContinentalSpringRollView, name="springroll"),



    url(r"^northindian/chollebature/$", views.NorthIndianCholleView, name="cholle"),
    url(r"^northindian/rajmachawal/$", views.NorthIndianRajmaView, name="rajma"),


    url(r"^southindian/dosa/$", views.SouthIndianDosaView, name="dosa"),
    url(r"^southindian/idli/$", views.SouthIndianIdliView, name="idli"),


    url(r"^italian/garlicbread/$", views.ItalianGarlicView, name="garlic"),
    url(r"^italian/pasta/$", views.ItalianPastaView, name="pasta"),



    url(r"^fastfood/aalootikki/$", views.FastFoodAalooView, name="aalootikki"),
    url(r"^fastfood/vadapao/$", views.FastFoodPaoView, name="vadapao"),


# deserts
    url(r"^deserts/icecream/$", views.IcecreamView, name="icecream"),
    url(r"^deserts/pastries/$", views.PastriesView, name="pastries"),
    url(r"^deserts/chocolates/$", views.ChocolatesView, name="chocolates"),

# beverages
    url(r"^beverages/tea/$", views.TeaView, name="tea"),
    url(r"^beverages/softdrinks/$", views.softdrinksView, name="softdrinks"),
    url(r"^beverages/juices/$", views.juicesView, name="juices"),


    ]
