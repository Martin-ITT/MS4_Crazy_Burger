# Crazy Burger
![Crazy Burger](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/amIresponsive.JPG "Crazy Burger")

<span id="project"></span>
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
#### Milestone Project 4 - Full Stack Framework with Django

[live website here](https://crazyburger.herokuapp.com/)
--------------------------------------

<span id="index"></span>
## Index
 <a href="#project">Project Idea 💁</a>
1. <a href="#ux">UX 👌</a>
1. <a href="#features">Features 🎮</a>
1. <a href="#technologies">Technologies Used 👉</a>
1. <a href="#testing">Testing 🔧</a>
1. <a href="#deployment">Deployment 💥</a>
1. <a href="#credits">Credits 👋</a>

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
| 18 | Shopper | Pay for my order | Make cashless payment |
| Administration |
| 19 | Owner | Add new meal | Inform the customer about new meal |
| 20 | Owner | Edit meal | Change the price when needed |
| 21 | Owner | Delete meal | When product discontinued |
| 22 | Owner | Have order database | See every order once payment is confirmed

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

Our project will be divided into few smaller applications: home, products, bag, checkout, and profiles.

Home application will be rendering our main home page.

Products application will contain data models for product Categories, Allergens, Toppings and Products themselves. It will be responsible for rendering the products and the product details pages and it will also serve admin to manage products in the store through Add Product and Edit Product views.

Bag application will provide access to the shopping bag with the funcionality of adding and removing products and also updating their quantity. Communication between the Bag and the other applications will be implemented using context processor.

Once all desired products will be in the bag a Checkout app will take user to the Checkout page to complete the order and make a payment following another page to confirm the order. To create an order from our shopping bag items we will need to attach these as line items using OrderLineItem model and attach it to an Order model.

Profiles application will manage basic information about our users and will allow them to see the Order History and to Repeat those orders with one click. User data will be stored using UserProfile model.

For Login, Logout, Registration and Password Management we will use Django package Allauth. This can also handle Login with Social Media accounts which is one of the requirements for this project.

## Data Modeling

### Products
#### Category

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| name  | CharField  | Generic category name - no white spaces |
| friendly_name  | CharField  | User readable category name |

#### Allergen

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| name  | CharField  | Name of the allergen |

#### Topping

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| name  | CharField | Name of the topping |

#### Product

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| category | ForeignKey | Key reffering to the _id of the Product model |
| name | CharField | Name of the product |
| description | CharField | Product description |
| allergens | ManyToManyField | Relationship between Allergen model and products |
| price | DecimalField | Product price |
| size | CharField | Displayed size at the basic price, e.g. 0.33l, 1/4lb, small... |
| has_sizes | BooleanField | Enables same product to be displayed with different sizes and prices |
| price_medium | DecimalField | Product price if available as medium size |
| size_medium | CharField | Displayed size at the medium price, e.g. 0.5l, medium... |
| price_large | DecimalField | Product price if available as large size |
| size_large | CharField | Displayed size at the large price, e.g. 1.5l, large... |
| price_meal | DecimalField | Price if product is available as a meal deal with a drink |
| has_toppings | BooleanField | Identifies products where toppings can amended. At the time of deploymnet this is only available with pizza category. |
| toppings | ManyToManyField | Relationship between Topping model and products |
| image | ImageField | A field to upload the product image. This is stored in media folder |

### Checkout
#### Order

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| order_number | CharField | Self-generated unique order number |
| user_profile | ForeignKey | Key reffering to the _id in UserProfile model |
| full_name | CharField | Customer's full name |
| email | EmailField | Customer's email address |
| phone_number | CharField | Customer's phone number |
| country | CountryField | Customer's address - coutry |
| postcode | CharField | Customer's address - post code |
| town_or_city | CharField | Customer's address - town or city |
| street_address1 | CharField | Customer's address - line 1 |
| street_address2 | CharField | Customer's address - line 2 |
| county | CharField | Customer's address - county |
| date | DateTimeField | Self generated field with time and date when order was created |
| comment | TextField | Customer's comment to specify any special requests |
| delivery_cost | DecimalField | Cost of delivery charge |
| order_total | DecimalField | Total amount for all product items in order |
| grand_total | DecimalField | Total amount of delivery cost and products in order |
| original_bag | TextField | Copy of a text string which represents items in shopping bag stored in session storage in a browser |
| stripe_pid | CharField | Stripe payment ID for actual order |

#### OrderLineItem

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| order | ForeignKey | Key reffering to the _id in Order model |
| product | ForeignKey | Key reffering to the _id in Product model |
| product_size | CharField | Size of the product ordered, e.g. small, large |
| product_drink | CharField | Drink ordered with the product if any |
| product_toppings | CharField | Toppings ordered with the product if any |
| product_price | DecimalField | Price of the product and related size as ordered |
| quantity | IntegerField | Quantity of product in order |
| lineitem_total | DecimalField | Total price for product-size. Quantity * product_price |

### Profiles
#### UserProfile
| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| user | ForeignKey | Key reffering to the _id in User model in django.contrib.auth |
| first_name | CharField | User's first name |
| last_name | CharField | User's last name |
| default_phone_number | CharField | User's phone number |
| default_street_address1 | CharField | User's address line 1 |
| default_street_address2 | CharField | User's address line 2 |
| default_town_or_city | CharField | User's address - town |
| default_county | CharField | User's address - county |
| default_postcode | CharField | User's address - postcode |
| default_country | CharField | User's address - country |

### django.contrib.auth
#### User

| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | SQLite ID |
| username | CharField | Chosen username at registration |
| first_name | CharField | User's first name |
| last_name | CharField | User's last name |
| email | EmailField | User's email address |
| password | CharField | User's password |
| groups | ManyToManyField | Relationship to Group model |
| user_permissions | ManyToManyField | Relationship to Permission model |
| is_staff | Boolean | Admin site access |
| is_active | Boolean | Recomended to set False instead of deleting user |
| is_superuser | Boolean | All permissions without explicitly assigning them |
| last_login | DateTimeField | Last user's login |
| date_joined | DateTimeField | A datetime when the account was created |

![Data Diagram](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/dataDiagram.JPG "Data Diagram")

## 1.5 Surface

For the design a Bootsrap 4 components and systems will be used. Bootstrap navbar will provide us with a dropdown menu and other navigation links. The main page will display an engaging hero image so the user will proceed to browse the menu. This will be enhanced with appropriate font and a color scheme. 
Pages shall remain responsive on keep the same format on all screen sizes. The only differnence on small and medium screens the header element will transfer to dropdown menu with a hamburger button and a search icon and products and product details will be stacked underneath each other.

#### Font Style - Titillium
Google fonts
![Font Style - Titillium](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/font.JPG "Font Style")

#### Color Scheme
Adobe color tools
![Color Scheme](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/adobecolor.JPG "Color Scheme")

#### Wireframes
Balsamiq wireframes
![Wireframes](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/wireframes.JPG "Wireframes")

# 2. Features 🎮

Home page

The home page is divided into two elements, the header and the hero image. To implement the ease of use principles our header and navbar remains the same on the other pages too. The top left corner displayes CrazyBurger logo which also acts as a home button. There is a search bar in the middle section, and underneath is a dropdown menu divided into few product categories. Top right section contains user icon which provides links to register, login, logout, and also an admin link when admin is currently logged in to add products. Just next to it there is a shopping bag icon which brings users to their shopping bag.
The header and the main section is divided with a banner reminding users of a free delivery option if they spend more than €50.
To attract the visitors the home page contains a large juicy burger and a red button Order Now next to it which directs user to the all food product page. 

Products page

The product page layout remains the same for all products or when a category is selected or the user is searching for particular product. There is a product image, product name and a category displayed. Product image and category serve as a links and will bring user to the product details page or will return category products respectively. For quicker navigation there are extra buttons which group some categories into larger chunks, e.g food products, meals and offers, desserts and other items in the store. Products can be sorted alphabeticaly, by price or category in both directions. 

Product details page

This page is split into two parts, left and right. There is a large product image on the left. The right side provides product name, product price, category, description and allergens. Some products can be bought as a meal deal with a drink or in a larger size. For these products Django will render an extra block underneath allergens and JavaScript will take care of the front-end dynamic part and will adjust the price or add extra text to the product name.




Admin add product
 If the product price_meal is larger than zero Django will render the page with option to upgrade product to a meal with a drink. JavaScript will open the drink section, change the displayed price and add text to the product name. Some other products can be purchased as a small or large. Both prices 
On mobile screens the image part is stacked above the product details section.


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
