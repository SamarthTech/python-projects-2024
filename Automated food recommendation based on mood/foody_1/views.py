from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from .models import Restaurants,TrainingData,MoodData
import math
import numpy as np

class HomePage(TemplateView):
    template_name = "index.html"

def resultpage(request):
    form=forms.Feedback()
    if request.method=='POST':
        form=forms.Feedback(request.POST)
        if form.is_valid():
            a=form.cleaned_data['Restaurant']
            b=form.cleaned_data['Food']
            c=form.cleaned_data['Mood']
            d=form.cleaned_data['Rating']
            print(a)
            print(b)
            print(c)
            print(d)
            v=Restaurants.objects.filter(name=a).values_list()
            print(v[0])
            f=v[0][4]
            g=v[0][6]
            nv= ((f*g)+d)/(g+1)
            Restaurants.objects.filter(name=a).update(rating=nv)
            Restaurants.objects.filter(name=a).update(count=g+1)
        return render(request,'test.html',{'form':form})
    return render(request,'foody_1/result.html',{'form':form})

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "foody_1/signup.html"

class NorthIndianView(TemplateView):
    template_name = "foody_1/NorthIndian.html"

class SouthIndianView(TemplateView):
    template_name = "foody_1/SouthIndian.html"

class ItalianView(TemplateView):
    template_name = "foody_1/Italian.html"

class ChineseView(TemplateView):
    template_name = "foody_1/Chinese.html"

class ContinentalView(TemplateView):
    template_name = "foody_1/Continental.html"

class FastFoodView(TemplateView):
    template_name = "foody_1/FastFood.html"

class ConfusedView(TemplateView):
    template_name = "foody_1/Confused.html"

class desView(TemplateView):
    template_name = "foody_1/deserts.html"

class beveragesView(TemplateView):
    template_name = "foody_1/beverages.html"

def ChineseNoodlesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][10]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}
    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ChineseDishes/Noodles.html',{'result':result})

def ChineseChillyPaneerView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][11]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ChineseDishes/ChillyPaneer.html',{'result':result})




def ContinentalHamView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][17]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ContinentalDishes/Ham.html',{'result':result})

def ContinentalSpringRollView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][16]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ContinentalDishes/SpringRoll.html',{'result':result})


def NorthIndianCholleView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][6]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/NorthIndianDishes/CholleBature.html',{'result':result})

def NorthIndianRajmaView(request):

    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][7]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/NorthIndianDishes/RajmaChawal.html',{'result':result})





def SouthIndianDosaView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][8]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/SouthIndianDishes/Dosa.html',{'result':result})

def SouthIndianIdliView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][9]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/SouthIndianDishes/Idli.html',{'result':result})




def ItalianGarlicView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][14]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ItalianDishes/GarlicBread.html',{'result':result})


def ItalianPastaView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][15]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/ItalianDishes/Pasta.html',{'result':result})




def FastFoodAalooView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][12]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/FastFoodDishes/AalooTikki.html',{'result':result})

def FastFoodPaoView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][13]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/FastFoodDishes/Wadapao.html',{'result':result})


def IcecreamView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][18]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/deserts/icecream.html',{'result':result})

def PastriesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][19]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/deserts/pastries.html',{'result':result})

def ChocolatesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][20]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/deserts/chocolates.html',{'result':result})

def TeaView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][21]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/beverages/tea.html',{'result':result})

def softdrinksView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][22]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/beverages/softdrinks.html',{'result':result})

def juicesView(request):
    restaurants=Restaurants.objects.all().values('name','latitude','longitude','rating','cost',
    'count','chholebature','rajmachawal','dosa','idli','noodles','chillypaneer','alootikki',
    'vadapao','garlicbread','pasta','springroll','ham','icecream','pastries','chocolates','tea','softdrinks','juices')
    trainingdata=TrainingData.objects.all().values('rating','cost','distance','yesno')
    temp3=list(restaurants)
    n=len(temp3)
    restaurantslist=np.zeros((n,24),np.int64)
    for i in range(n):
        restaurantslist[i][0]=temp3[i]['name']
        restaurantslist[i][1]=temp3[i]['latitude']
        restaurantslist[i][2]=temp3[i]['longitude']
        restaurantslist[i][3]=temp3[i]['rating']
        restaurantslist[i][4]=temp3[i]['cost']
        restaurantslist[i][5]=temp3[i]['count']
        restaurantslist[i][6]=temp3[i]['chholebature']
        restaurantslist[i][7]=temp3[i]['rajmachawal']
        restaurantslist[i][8]=temp3[i]['dosa']
        restaurantslist[i][9]=temp3[i]['idli']
        restaurantslist[i][10]=temp3[i]['noodles']
        restaurantslist[i][11]=temp3[i]['chillypaneer']
        restaurantslist[i][12]=temp3[i]['alootikki']
        restaurantslist[i][13]=temp3[i]['vadapao']
        restaurantslist[i][14]=temp3[i]['garlicbread']
        restaurantslist[i][15]=temp3[i]['pasta']
        restaurantslist[i][16]=temp3[i]['springroll']
        restaurantslist[i][17]=temp3[i]['ham']
        restaurantslist[i][18]=temp3[i]['icecream']
        restaurantslist[i][19]=temp3[i]['pastries']
        restaurantslist[i][20]=temp3[i]['chocolates']
        restaurantslist[i][21]=temp3[i]['tea']
        restaurantslist[i][22]=temp3[i]['softdrinks']
        restaurantslist[i][23]=temp3[i]['juices']
    temp1=np.zeros((n,1),np.int64)
    restaurantslist=np.append(restaurantslist,temp1,1)
    latitude = 10
    longitude = 10
    for i in range(n):
        restaurantslist[i][24]=math.sqrt(((restaurantslist[i][1]-latitude)*(restaurantslist[i][1]-latitude))+((restaurantslist[i][2]-longitude)*(restaurantslist[i][2]-longitude)))
    temp3=list(trainingdata)
    n=len(temp3)
    trainingdatalist=np.zeros((n,4),np.int64)
    for i in range(n):
        trainingdatalist[i][0]=temp3[i]['rating']
        trainingdatalist[i][1]=temp3[i]['cost']
        trainingdatalist[i][2]=temp3[i]['distance']
        trainingdatalist[i][3]=temp3[i]['yesno']
    # cuisine = form.cleaned_data['cuisine']
    X_train = trainingdatalist[:, [0,1,2]]
    y_train = trainingdatalist[:, 3]
    #info = pd.read_csv('BurgerInfo.csv')
    info=np.zeros((1,25),np.int64)
    n=len(restaurantslist)
    for i in range(n):
        if(restaurantslist[i][23]==1):
            info=np.vstack([info, restaurantslist[i]])
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    info=info[1:,:]
    X_test = info[:,[3,4,24]]
    y_pred = classifier.predict_proba(X_test)
    info=np.append(info,y_pred,1)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j][26] > info[j+1][26] :
                temp=np.zeros(27,np.int64)
                for k in range(27):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=[]
    jelly={1:'PizzaHut',2:'Dominos',3:'BeijingStreet',4:'KakeDiHatti',5:'ItalianJoint',6:'ChineseYum',7:'SagarRatna',8:'QDs',9:'DCafe',10:'Tamasha',11:'MasalaTrail'}

    for i in range(n):
        result=np.append(result,jelly[info[i][0]])
    return render(request,'foody_1/beverages/juice.html',{'result':result})







def HappyView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['happie'] > info[j+1]['happie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['CholleBature','GarlicBread']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/happie.html',{'result':result})


def AngryView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['angrie'] > info[j+1]['angrie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['SoftDrinks','Pasta']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/angrie.html',{'result':result})


def DehydrateView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['dehydratie'] > info[j+1]['dehydratie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['SoftDrinks','Juices']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/dehydrated.html',{'result':result})


def DepressiveView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['depressie'] > info[j+1]['depressie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['IceCream','Chocolates']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/depressive.html',{'result':result})


def ExciteView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['excitie'] > info[j+1]['excitie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['Pastries','RajmaChawal']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/excite.html',{'result':result})

def UnwellView(request):
    trainingdata=MoodData.objects.all().values('Dish','happie','angrie','dehydratie','depressie','excitie','unwellie')
    info=list(trainingdata)
    n = len(info)
    for i in range(n-1):
        for j in range(n-1):
            if info[j]['unwellie'] > info[j+1]['unwellie'] :
                temp=np.zeros(7,np.int64)
                for k in range(7):
                    temp[k]=info[j][k]
                info[j]=info[j+1]
                info[j+1]=temp
    result=['Juices','Tea']
    m=0
    if(m<n):
        m=n
    for i in range(m):
        result=np.append(result,info[i]['Dish'])
    return render(request,'foody_1/moods/unwellie.html',{'result':result})

# def index1(request):
#     trainingdata=MoodData.objects.all().values('dish','depressed','happy','sick','dehydrated','dizziness')
#     trainingdatalist=list(trainingdata)
#     n = len(info)
#     for i in range(n-1):
#         for j in range(n-1):
#             if info[j][1] > info[j+1][1] :
#                 temp=np.zeros(6,np.int64)
#                 for k in range(6):
#                     temp[k]=info[j][k]
#                 info[j]=info[j+1]
#                 info[j+1]=temp
#     return render(request,'myapp/index.html',{'form':form ,'result':result})
