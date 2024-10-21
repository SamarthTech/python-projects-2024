# MoodieFoodie
*...Food for every Mood*

This is a web application which recommends you food based on your mood using machine learning and delivers it to your doorstep.

We understand that the first thought that comes to our mind when we come across a food suggesting and delivery app, is obviously- "HOW IS THIS SOMETHING NEW?"

We'll explain.
This web application is based on an absolutely new idea and is completely different from the traditional food delivery websites.

Firstly, it suggests a list of restaurants combining three basic parameters i.e cost, user rating and distance, all at the same time. Hence, it offers you the most optimal choice available, saving you the trouble of choosing the best restaurant for you using individual filters on traditional apps. 
The most commonly used apps allow you to choose a restaurant on the basis of only a single critera at a time, but we recommend you the nearest, most affordable and best quality restaurants, thereby catering to all your demands at the same time without having you to compromise on any of them.

Secondly, we understand that there are times when you are unable to decide what to order. Infact, we have personally faced this dilemma a hundred times when we've spent hours scrolling a food delivery app, thinking about the most important question which seems to have been given the least importance uptil now , "WHAT TO EAT?" 
MoodieFoodie helps you to choose a food item for all your moods, be it a happie, a sadie, an angrie, a dehydratie, a depressie, an excitie or an unwellie mood ;")
Whatever be your mood, we can always suggest you food!

The app uses previous user moods and their respective food orders to suggest the best food choice for you.

Thirdly, we offer several other options for food ordering like the list of food items ordered the most at a particular time of the day or the restaurants that can order food in the minimum time if you're really hungry or the top searched food items, etc.

And lastly, this app allows you to order the food items that traditional food delivery apps don't.
You can order tea, juices or even chocolates. For this, we have a separate "Wanna sell on MoodieFoodie" option for small scale sellers like small tea shops, women who make homemade chocolates or other small scale setups who wish to sell online.

## Working and Implementation
<ul>
<li>The major feature of our project which sets it apart from the traditional apps of its kind needs three parameters to order the list of recommended restaurants with the highly recommended restaurant at the top. These three features are the user ratings, cost for two people and the restaurant's distance from the user.
<ul>
<li>Whenever any user orders from a certain restaurant, he/she is asked to rate the restaurant out of 5. The rating of that restaurant is then dynamically updated using the mathematical average of the current rating and the new rating. This computation also requires the storage of the number of ratings for a particular restaurant.
<li>The cost for two people is permanently stored initially when a restaurant is added to the database.
<li>To compute the distance of the user from a restaurant, we have stored the geocode of all the restaurants in the database. We have used the Google Maps API to extract the user's geocode and hence compute his/her distance.</li>
</ul>
A very simple model of machine learning, that is logistic regression is used to implement the same. When the user chooses a certain restaurant among the recommended restaurants, then his/her choice to select a certain restaurant and discard other restaurants is used to train the model which only increases the accuracy of the algorithm.
<li>The USP of our project, which is recommending the users food items based on their mood works on previous users' inputs only. Whenever any user orders from a certain restaurant, he/she is asked to specify what his/her mood was before he/she had ordered. His/Her order and mood is used to train the algorithm which gradually increases its accuracy.
<li>To help small businesses expand their reach by selling on our application, we have simply provided them with a form wherein they can fill out the necessary details.
</ul>

## Installation Requirements

```
Framework : Django, Version : 1.11.8
Language : Python, Version : 3.6.3

To run it, you need to install some packages and libraries as follows:
Bootstrap 3
numpy
sklearn
bcrypt
django[argon]

To install these, write this on the command line terminal:
"pip install package-name"
```

## To run

```

Enter the command: "python manage.py runserver"
Copy the url and paste it in your favourite browser window.
```

