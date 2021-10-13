
![Crazy Burger](https:/pics-link-here "Crazy Burger")

<span id="index"></span>
## Index
 <a href="#project">Project Idea 💁</a>
1. <a href="#ux">UX 👌</a>
1. <a href="#features">Features 🎮</a>
1. <a href="#technologies">Technologies Used 👉</a>
1. <a href="#testing">Testing 🔧</a>
1. <a href="#deployment">Deployment 💥</a>
1. <a href="#credits">Credits 👋</a>



<span id="project"></span>
# Crazy Burger
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
### Milestone Project 4 - Full Stack Framework with Django
[live website here](https://crazyburger.herokuapp.com/)
--------------------------------------

Fourth Milestone project is focused on creating larger and complex web applications using Django to demonstrate the ability of solving real-world scenarios. Django is powerfull framework for rapid web development emphasizing reusability and use of its components. It contains number of applications, including authentication system, CRUD operations support and administrative interface including security features. 
Most of my professional life I've spent in restaurants so I decided to create web application for take-away restaurant Crazy-Burger. This website will provide all convenient features as browse menu, place an order with payment, create user account for easier ordering or contact restaurant over contact form.

<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy

The goal is to promote local restaurant by creating professional website. Online food ordering services can be quiet expensive for small businesses. Customers bill can easily drop by 20% if they will order directly over the restaurant webpage. However, the webpage must be also attractive, reliable, accesible and easy to use in order to become a success. User stories will help us identify all critical aspects.

### User stories
### Users


| User story | As a/an | I want to be able to | So that I can |
| -----------: | :--------| :--------------------| :------------|
| Viewing and navigation |
| 1 | Shopper | Browse the menu | Compare and order food I want |
| 2 | Shopper | View meal details | See the image, price, alergens |
| 3 | Shopper | See special offers | Get better price and save money |
| 4 | Shopper | See my previous orders | Order easily and control the budget |
| 5 | Shopper | Add special note to order | State important information about my order |
| Registration and User accounts |
| 6 | User | Create an account | Control my deteils |
| 7 | User | Login or logout | Use account funcionality | *social media account
| 8 | User | Recover forgotten password | Get my account back |
| 9 | User | See my personalized profile | See history of my orders and store payment info |
| Sorting and Searching |
| 10 | Shopper | Sort the list of available meals | Identify newest, cheapest |
| 11 | Shopper | Sort a special offers | Identify newest and cheapest products in certain category |
| 12 | Shopper | Search for a meal by name | Find particular food |
| Purchasing and Checkout |
| 13 | Shopper | Easily add meal to basket | So I only add what I want |
| 14 | Shopper | Edit basket | Change items if I change my mind |
| 15 | Shopper | Have my details pre-filled | Easily checkout |
| 16 | Shopper | Get an email confirmation for my order | To double check my order |
| Administration |
| 16 | Owner | Receive feedback | See if customer is not happy |
| 17 | Owner | Add new meal | Inform the customer about new meal |
| 18 | Owner | Edit meal | Change the price when needed |
| 19 | Owner | Delete meal | When product discontinued |

## 1.2 Scope 


Image were edited using Gimp


Hero image was downloaded from pexels.com - Adrian Dorobantu
    https://www.pexels.com/photo/cheeseburger-on-table-2089717/
Food pictures were downloaded from kaggle.com - K Scott Mader
    https://www.kaggle.com/kmader/food41?select=images
Logo was created using Adobe Spark logo maker
    https://www.adobe.com/express/create/logo

    https://stackoverflow.com/questions/44915511/stripe-elements-google-web-font-not-working
    https://stackoverflow.com/questions/46863072/do-not-collect-zip-code-with-stripe
    https://fontawesome.com/v5.15/how-to-use/on-the-web/styling/animating-icons
    https://stackoverflow.com/questions/56028939/bootstrap-toast-remains-on-top-invisible

Product pictures:

beef creole
    https://www.pexels.com/photo/cooked-meat-on-plate-2313686/

blt baguette
    https://www.pexels.com/photo/slices-of-breads-1483769/

cheeseburger
    https://www.pexels.com/photo/bacon-cheeseburger-with-melted-cheese-3052366/

chicken burger
    https://www.pexels.com/photo/meat-sandwich-on-black-surface-236488/

chicken creole
    https://www.pexels.com/photo/bowl-of-meat-3386854/

chicken kebab
    https://pxhere.com/en/photo/830948

chicken wrap
    https://pxhere.com/en/photo/1177202

cookie light
    https://pxhere.com/en/photo/3035

cookie dark
    https://pxhere.com/en/photo/1038105

crepe banana-cereals
    https://pxhere.com/en/photo/1062540

crepe banana-nutella
    https://unsplash.com/photos/s_aGnOcfCq0

crepe nutella and cream
    https://unsplash.com/photos/1ZTccDpF71k

dip bbq, garlic
    https://unsplash.com/photos/CjmlUpo3eAw

dip curry
    https://unsplash.com/photos/e75FKtu30fQ

doner kebab
    https://pxhere.com/en/photo/789784

drink coke
    https://www.pexels.com/photo/coca-cola-zero-bottle-on-white-table-4113616/

drink coke diet
    https://pxhere.com/en/photo/422777

drink coke zero
    https://unsplash.com/photos/RXi9NAlwB00

drink fanta
    https://unsplash.com/photos/nJguJaHo5dg

drink sprite
    https://unsplash.com/photos/4KLT91f3mAM

fish and chips
    https://pxhere.com/en/photo/751570

fries
    https://www.pexels.com/photo/fried-potatoes-1583884/

fries garlic
    https://unsplash.com/photos/PJrRYKdAwlQ

fries taco
    https://www.pexels.com/photo/top-view-of-food-1640772/

hamburger
    https://www.pexels.com/photo/burger-with-lettuce-and-cheese-on-a-white-plate-3738730/

kids cheeseburger
    https://www.pexels.com/photo/btl-burger-with-fries-551991/

kids hamburger
    https://www.pexels.com/photo/burger-with-lettuce-and-tomato-3864682/

kids nuggets
    https://pxhere.com/en/photo/1110920

milkshake chocolate
    https://unsplash.com/photos/7TeR1A1MUpM

milkshake oreo
    https://unsplash.com/photos/xB0Kr0D0C8Y

milkshake strawberry
    https://unsplash.com/photos/X1Wun0nCHOc

milkshake vanilla
    https://unsplash.com/photos/OaGUHIjCdCs

muffin blueberry
    https://www.pexels.com/photo/close-up-photography-of-chocolate-cupcake-90609/

muffin chocolate
    https://www.pexels.com/photo/sweet-homemade-chocolate-dessert-on-tray-4792403/

muffin ferrero
    https://unsplash.com/photos/90HdOlGbjck

pizza hawai
    https://www.pexels.com/photo/dinner-fast-food-lunch-meal-3644/

pizza margharita
    https://pxhere.com/en/photo/716259

pizza meaty
    https://www.pexels.com/photo/pepperoni-pizza-803290/

pizza mexican
    https://www.pexels.com/photo/pizza-on-brown-wooden-board-825661/

pizza pepperoni
    https://www.pexels.com/photo/person-slicing-pizza-on-brown-wooden-table-4004422/

pizza veggie
    https://www.pexels.com/photo/pizza-2619967/

salad caesar
    https://unsplash.com/photos/63mHpYEyjCA

salad thai
    https://pxhere.com/en/photo/1442875

sausages
    https://www.pexels.com/photo/cooked-sausage-929137/

spice bag
    https://pxhere.com/en/photo/1326730

sundae jack
    https://www.pexels.com/photo/ice-cream-with-chocolate-chips-topped-with-melted-chocolate-7144269/

sundae with chocolate and cereals
    https://pxhere.com/en/photo/959889

sundae with strawberries
    https://pxhere.com/en/photo/617596

two burgers
    https://www.pexels.com/photo/two-burgers-with-fries-and-sauce-3738755/

wings bbq
    https://pxhere.com/en/photo/1614160
