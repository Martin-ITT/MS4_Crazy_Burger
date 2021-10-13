
![Crazy Burger](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/amIresponsive.JPG "Crazy Burger")

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
Most of my professional life I've spent in restaurants so I decided to create web application for fictive take-away restaurant Crazy-Burger. This website will provide all convenient features as browse menu, place an order with payment, create user account or even use social media login to see or repeat previous orders.

<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy

The goal is to promote local restaurant by creating professional website. Online food ordering services can be quiet expensive for small businesses. Customers bill can easily drop by 20% if they will order directly over the restaurant webpage. However, the webpage must be also attractive, reliable, accesible and easy to use in order to become a success. User stories will help us identify all critical aspects.

### User stories
### Users


| User story | As a/an | I want to be able to | So that I can |
| -----------: | :--------| :--------------------| :------------|
| Viewing and navigation |
| 1 | Shopper | Browse the menu | Select and order food I want |
| 2 | Shopper | View meal details | See the image, price, alergens |
| 3 | Shopper | See special offers | Get better price and save money |
| 4 | Shopper | Responsive design | Order on a mobile device |
| 5 | Shopper | Add special note to order | State important information about my order |
| 6 | Shopper | See shopping bag updates | See the total without accessing the shopping bag |
| Registration and User accounts |
| 7 | User | Create an account | Control my deteils |
| 8 | User | Login or logout | Use account funcionality | 
| 9 | User | Recover forgotten password | Get my account back |
| 10 | User | See my personalized profile | See history of my orders and store payment info |
| 11 | User | Use Social Media account | Login easily with my other accounts |
| Sorting and Searching |
| 12 | Shopper | Sort the list of available meals | Identify cheapest products |
| 13 | Shopper | Search for a meal by name | Find particular food |
| Purchasing and Checkout |
| 14 | Shopper | Easily add meal to basket | Buy that product |
| 15 | Shopper | Edit / remove from basket | Change or remove items if I change my mind |
| 16 | Shopper | Have my details pre-filled | Easily checkout |
| 17 | Shopper | Get an email confirmation for my order | To double check my order |
| Administration |
| 18 | Owner | Add new meal | Inform the customer about new meal |
| 19 | Owner | Edit meal | Change the price when needed |
| 20 | Owner | Delete meal | When product discontinued |
| 21 | Owner | Have order database | See every order once payment is confirmed

## 1.2 Scope 

Based on the User Stories following features and components will be required in order to implement Minimum Viable Product so our app can be deployed.

- Welcoming home page with nice hero image
- Structured menu for navigation with extra links for each category
- Responsive design
- Page to display and sort all/selected category products
- Page to display all product details and option to buy this product 
- Search bar to avail users to find products
- Notification system with shopping bag updates
- Page to display shopping bag and update it
- Checkout page and a checkout confirmation
- Email checkout confirmation
- Register and login page with social media access
- Forgotten password feature
- User profile page and page to display previous order details
- Repeat previous order funcionality
- Page to add and edit products, remove product function
- Database and Media storage

## 1.3 Structure

Project will contain both the Front-End and Back-End code.

Front-End code will be written in HTML5 and styled with CSS3 and Bootstrap4 framework.
JavaScript will enable some Front-End dynamic features and some communication between Front-End and Back-End, e.g. submitting forms.

For progressive development Back-End code will be written in Python3 using Django framework. Django supports SQLite database where our data will be stored. In developments media and static files will be stored locally. For deployed version on Heroku our database will be handled by Postgress and static and media files will be stored with AWS S3.

## 1.4 Skeleton

Our project will be divided into few smaller applications: home, products, bag, checkout, and profiles. Home application will be rendering our main home page. Products application 



To implement the ease of use principles our navbar will be consinstent on all rendered pages. It will only change on smaller devices to achieve responsive design. From home page user can navigate to search and browse the products, register or login. On products page 


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
