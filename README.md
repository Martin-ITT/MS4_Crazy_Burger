# Crazy Burger
![Crazy Burger](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/media/amIresponsive.JPG "Crazy Burger")

<span id="project"></span>
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
#### Milestone Project 4 - Full Stack Framework with Django

#### [live website here](https://crazyburger.herokuapp.com/)
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


<a href="#index">Back to top ☝️ </a>
<span id="features"></span>

# 2. Features 🎮
## 2.1 Implemented features

Home page

The home page is divided into two elements, the header and the hero image. To implement the ease of use principles our header and navbar remains the same on the other pages too. The top left corner displayes CrazyBurger logo which also acts as a home button. There is a search bar in the middle section, and underneath is a dropdown menu divided into few product categories. Top right section contains user icon which provides links to register, login, logout, and also an admin link when admin is currently logged in to add products. Just next to it there is a shopping bag icon which brings users to their shopping bag.
The header and the main section is divided with a banner reminding users of a free delivery option if they spend more than €50.
To attract the visitors the home page contains a large juicy burger and a red button Order Now next to it which directs user to the all food product page. 

Products page

The product page layout remains the same for all products or when a category is selected or the user is searching for particular product. There is a product image, product name and a category displayed. Product image and category serve as a links and will bring user to the product details page or will return category products respectively. For quicker navigation there are extra buttons which group some categories into larger chunks, e.g food products, meals and offers, desserts and other items in the store. Products can be sorted alphabeticaly, by price or category in both directions. 

Product details page

This page is split into two parts, left and right. There is a large product image on the left. The right side provides product name, product price, category, description and allergens. Some products can be bought as a meal deal with a drink or in a small/large sizes. For these products Django will render an extra block underneath allergens and JavaScript will take care of the front-end dynamic part and will adjust the price or add extra text to the product name. Soft drinks are comming in three different sizes - 0.33l, 0.5l and 1.5l. There is quantity selector below so user can easily add required amount of products. Keep Shopping button returns user back to products screen or product can be Added To Bag. For extra user experience, a pop up message is displayed informing user that product has been succesfully added and providing quick view of the shopping bag and total amount, and also how much more needs to be spent to avail of free delivery.

Shopping bag page

After clicking bag icon in header or checkout button in pop up message, a shopping bag page is displayed. It shows order summary, Product image, name, selected options e.g. meal, drink or size, product price, quantity and subtotal for product line. Quantity can be adjusted or product can be removed from the shopping bag. There is bag total at the bottom of the page and another free delivery message. Keep Shopping button provides link back to the product page and Secure Checkout direct user to the checkout page.

Checkout page

The left part of the checkout page contains an order form where users need to fill in their name, email address, phone number and a delivery address. There is a text box if user wants to leave a message with any special request. When user is logged in, there is a checkbox if customer wants to save the order into their order history. Otherwise, there is a reminder of convenient registration for easier checkout. There is a Stripe element at the bottom to type in the credit card details. The right part of the screen displayes another order summary, including delivery charge and a grand total. Adjust bag gives option to return to the shopping bag or user can complete order and make a payment. On smaller screens these parts are stacked on top of each other.

Checkout success

Thank you. Your order information is below. Once payment is proccessed, a checkout success screen is displayed. This contains order number, date and time when order was created, ordered products, delivery address and total amount paid. Button Place New Order will bring customer back to the Product page.  

Login page

Users can log in either by using their Google or Facebook account or by entering their username or email address and a password. This page also contains links to sign up for an account or password recovery.

Registration page
User can sign up for an account by entering email address, username and a password. A confirmation email is sent and must be validated before first login.

Profile Page

Profile page is also split into the left and right part. There is a form on the left side where user can update their name, phone number and their address. This information is pre-filled into the payment form for easier checkout. The right part shows order history, with few order details. Order number can be clicked and more details are shown, same as in checkout success page. There is extra function - Repeat Order to get previous order again with one click.

Admin - Add Product

Admin user can add products by clicking admin option under the user icon in navbar. A product form is displayed. A product category needs to be selected so the product is displayed under the appropriate menu options. Name is a mandatory field limited to 254 characters. Description is also mandatory so the product detail page has can display some additional information. If product contains more allergens, these can be selected while holding the CTRL button down. Price and Size field are mandatory and inform user of the product price at default size, e.g small, 0.33l. Except pizzas and soft drinks, CrazyBurger products come in a single size or as small and large. In this case, price and price large only need to be set, and has sizes checkbox needs to be ticked. Some products can be upgraded to a value meal with a drink. This can be achieved when price_meal is set and no checkbox ticked. Pizzas come in a 9", 12" and 14" size, except margherita which is only available as 12" and 14". Once selecting pizza category, this product is displayed as 9"-12"-14". Price topping medium/large are only effecting margherita pizza, which is already in products. Soft drinks are sold as 0.33l, 0.5l and 1.5l. Size, size_medium and size_large needs to be amended and all thee prices defined accordingly. There are extra links on Products and Product Detail pages which are enabled when admin is logged in and allows to edit or remove products.

## 2.2 To be implemented

Few more features could have been implemented but were not initially required. A nice feature would be simply place the order for collection and the customer not beign charged for delivery even without paying for the order upfront. A feedback contact form and address details with a map on the page would be also appropriate.


<a href="#index">Back to top ☝️ </a>
<span id="technologies"></span>

# 3. Technologies Used 🎡

## 3.1 Languages

- HTML/HTML5
Each web page was built using HTML elements.

- CSS
Some HTML elements were styled using CSS

- JavaScript / Jquery
Interactive web behaviour and form submit.

- Python
This app was build using python based framework Django and its packages.
Crispy Forms - library for python to work fast and efficiently with forms.

## 3.2 Other libraries and frameworks

- Bootstrap 4
Navbar, Footer and some other elements were implemented using this popular library.

## 3.3 IDE, Version control and hosting

- GitPod
Collaborative development environments in browser

- Git and GitHub
Version control and repository

- Heroku
GitHub repository was linked with Heroku and is hosted here

- AWS S3
Static and Media Files of deployed version are stored AWS servers.

Sqlite 
- powerful SQL database engine used in development version

Postgres
- open source RDBMS used in deployed version


## 3.4 Other tools

- Balsamiq was used to create wireframes

- Adobe Color was used to identify the colour scheme

- Am I Responsive was used to create title image for readme.md

- DrawSQL was used to create DB schema

- Chrome Devtools were used to see the behaviour of the elements and their style

<a href="#index">Back to top ☝️ </a>
<span id="testing"></span>

# 4. Testing 💉

## 4.1 Validation

HTML code was checked in W3C validator with no errors - https://validator.w3.org/

CSS code was checked in W3C validator with no errors - https://jigsaw.w3.org/css-validator/

JS code was checked in BeautifyTools with no errors - http://beautifytools.com/javascript-validator.php

JS code was also checked in JSLint with no errors - https://jslint.com/

Python code was checked in pep8 online and errors were fixed. White spaces at the end of lines, and lines with non compliant lenght were the only issues.  - https://pep8online.com/

Responsivness was tested in Chrome and Firefox on Win10 with Devtools, ipad mini 6th gen, onePlus 7pro phone and Am I Responsive website. Iphone 5 was used in Devtools as standard for smallest screen. Bootstrap Display properties, Grid system and CSS media queries were used to adapt responsive layout.

## 4.2 Features testing

Tests were completed on iPhone5, iPad and 1200px screen sizes. 

### Navbar
Navbar links were tested to ensure the user is redirected to appropriate page. Mobile drop-down navbar is displayed on pages under 992px where CrazyBurger logo is replaced with a hamburger button and the search bar is minimized into an icon. Font size had to be adjusted to keep the elements inline. The smallest device was iPhone5 and navbar was displaying correctly. When no user is logged in, there is an option to sign in or register. When user is logged in a profile and log out options are shown. Admin option to add product is only displayed when admin is signed in. All of these are working correctly.

### Toast messages
Toast messages are divided into four categories using levels imported from Django messages framework. A red error messages are displayed when certain action would trigger an error in code. Yellow warning messages display that some funcionality is not working, e.g. Stripe Secret Key is not defined. Green messages indicate a successfull operation, e.g. signing in. When user is not using any profile funcionality a shopping bag is also attached to the message. Blue info messages are letting the user know that some other actions were triggered, e.g. searching for product returned some results or admin user is about to edit a product. All toast messages are working correctly.

### Home app
Views.py contains index function which is rendering home page. Index.html extends the base.html using template tags. This is working correctly.

### Products app

Models

Category, Allergen, Topping and Product models contain `__str__(self)` method which returns a category name when str() funcion is called on object. Category model also contains get_friendly_name() function which returns friendly name of object.

Forms

ProductForm contains all Product fields and follow their set attributes. Submitting an empty product form returns an error stating Name, Description and a Price are required. Entering non number value in price fields returns error to enter a number. Inserting non image file results also in error with a request to recheck and submit a valid form.

Views

All_product view returns all products and renders Products page. This view is also responsible for sorting products, returning products within a category sub-menu and a search query. All categories were rendered corectly upon selection. Searching returns correct results and search query for special characters was also tested to prevent injection attack. Sorting was tested on all products, multiple categories, and search results. Products were correctly sorted by name, price and a category in both directions. JQuery event listener is used to send sorting criterias to back-end. 

Product_detail view renders Product Detail page. There is also a JQuery code which changes behaviour of the pages upon user actions - upgrading to a meal, selecting a size or drink and adding or removing toppings from pizzas. JQuery also disables 9" radio button for Margerita pizza. All these are working correctly.

Add Product view contains ProductForm which was tested separately. @login_required decorator together with "if not request.user.is_superuser:" condition was tested from the browser navbar to access this view. Access was denied when no user was logged in and also when standard user was logged in. On submitting valid form the product was added to the database.

Edit Product view was tested same as Add Product. Submitted valid form has updated the product attributes.

Delete Product view is also only accessible when admin is currently logged in. When admin is logged in, product has been removed from database.

### Bag app

View_bag view is correctly rendering bag.html. JQuery is updating quantity and prevents value to be less than 1 or greater than 99. Another scripts submits updated quantity and removes items from a bag. All these funcionalities work as expected.

Add_to_bag. All 54 products were tested to be added to the bag in various quantities. Test were extended for products which has different attributes, e.g. meal, size, toppings. No problem was found and each item can be added to the bag.

Adjust_bag view was tested after products were added to the bag. I focused on products which can be bought with extra options as I was aware there might be extra challenge. Plus/minus buttons which are handled by JQuery were not working correctly (another product was effected) and were not disabled at specified values. The problem was with dot sign in the constructed id-selector, e.g. "single.meal.fanta". The dots are valid character for HTML ID attribute but it causes problem for JQuery selector. This was replaced and now it works as expected.

Remove from bag view was tested after updating quantity with same focus as Adjust_bag. The bag output was displayed to check if product id's are also removed from the bag.

Context.py was tested throughout the views to see if working correctly. Values for each variable and each condition were printed out in terminal to see their behaviour. No issues were found.

### Checkout App

Models

Order model

Function _generate_order_number() generates random string as order number every time an order is saved (created).

Function update_total() updates total amount when a line item is updated or deleted. The total and also the delivery charge is updated correctly. This also proves that signals in signals.py works correctly.

Function `__str__()` returns the order number when str() is called on the object.

OrdeLineItem

Function save() updates the lineitem_total when called on object.

Function `__str__()` returns product name with appropriate order number.

Views

Cache_checkout_data is working correctly as webhooks are received by Stripe. This can be seen in Stripe developers console.

Checkout view is working correctly, payment_intents are created in Stripe. Orders are correctly saved in database.

Checkout_succes is also working correctly. On succesfull payment order is saved to profile if save_info is True and shopping bag is emptied.

Webhooks were also tested while disabling form submit function in JS part of the payment process. Success checkout was not displayed but the payment was procceses, email was sent and order was created in database.

### Profiles app

Profile view is rendering profile.html page. On POST request valid form updates user details and also saves first_name and last_name if available. On submitting invalid form an error message is returned. This view is protected with @login_required decorator. Error message is returned when no user is logged in and view is called.

Order history renders appropriate past order in checkout_success.html template. Again login is required and this is working correctly.

Repeat order was checked to repeat previous shopping bag to create the same order again. This is working as expected. This view is also wrapped in login required and the behaviour was confirmed.

## Allauth

Registration, login and logout was tested while deveoping this project. No issues were found. Both social media logins are connected and working. Facebook login will display that project is in testing and will only allow registered developers to sign in.

<a href="#index">Back to top ☝️ </a>
<span id="deployment"></span>

# 5. Deployment 🔧

* On Heroku Website https://dashboard.heroku.com/apps , New -> Create New App
* Choose App name and region.
* Use Resources - Addons - Heroku Postgres

* In gitpod:
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt

* In settings.py
- `import dj_database_url`

```
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': dj_database_url.parse('postgress-url-goes-here')
}
```
* NB Get url from Heroku App settings tab / reveal config vars.

* Run migrations again (different database)

* `python3 manage.py showmigrations` Will show none exist

* `python3 manage.py migrate`

* To import product data, use fixtures:
- `python3 manage.py loaddata categories`
- `python3 manage.py loaddata products`
- NB categories must be created first as products depend on them.

* Create superuser account in the new database
- `python3 manage.py createsuperuser`


NB DO NOT COMMIT DATABASE URL TO VERSION CONTROL.

* Update settings.py to connect to a different database depending on if this is deployed or production version:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* `pip3 install gunicorn`
* `pip3 freeze > requirements.txt`
* Create `Procfile` in root folder with the contents `web: gunicorn crazyburger.wsgi:application`

* NB: Check folder for Procfile is correct

* In terminal:
- 'heroku login' or 'heroku login -i'
- `heroku config:set DISABLE_COLLECTSTATIC=1 --app crazyburger`

* In settings.py `ALLOWED_HOSTS = ['crazyburger.herokuapp.com', 'localhost']`
* NB must be wrapped in `` above.

* If the app was created on the heroku website, set the remote repo. `heroku git:remote -a crazyburger`

* to check: `git remote -v`

* The great moment! `git push heroku master`

* To deploy to github automatically:
- In Heroku web interface:
- Deploy -> Github
- Select repo and connect.
- Enable automatic deploys

* https://miniwebtool.com/django-secret-key-generator/ 
- Add this to Heroku -> Config Vars -> Add the secret_key
-  Update settings.py to contain it: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
- Set `DEBUG = 'DEVELOPMENT' in os.environ` in settings.py

## Creating an AWS Account

* Use AWS s3 to store static files.
- Create account at https://aws.amazon.com/
- Account type personal
- Go to AWS Management Console.
- Open s3
- Create new bucket
- In Set Permissions, uncheck Block All Public Access

* Bucket settings:
- Properties -> Static Website Hosting
- Use default values index.html and error.html
- Save
- Permissions:
- CORS Configuration:
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
- Bucket Policy -> Policy Generator
- Policy Type: s3 Bucket Policy
- Principal: *
- Action: GetObject
- Copy ARN from the other tab eg `arn:aws:s3:::crazyburger`
- Add statement
- Generate Policy
- Copy Policy into other tab 'Bucket Policy'
- BEFORE SAVING: add /* into the resource key `"Resource": "arn:aws:s3:::crazyburger/*",`
- Access Control list -> Public Access -> Tick 'List Objects' and save.

* Use AWS service 'IAM' to connect to the bucket
- Go to IAM
- Click Access Management -> Groups
- Create New Group 'manage-crazyburger'
- Click next twice (no policy to attach yet)
- Create Group
- Policies -> Create Policy
- Create Policy
- json tab -> Import managed policy
- Search for s3 and import the s3 Full Access Policy.
- From Bucket Policy in s3, get the arn and edit the json accordingly.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::crazyburger",
                "arn:aws:s3:::crazyburger/*"
                ]
        }
    ]
}
```
- Review Policy
- Add name and description. 
- Create
- Go to Groups -> Select the group -> Permissions tab -> Attach policy -> search and attach.

* users
- Add user
- Include static files access.
- Next: Permisssions
- Add user to group.
- Create user
- ESSENTIAL: Download .csv file.

* Connecting django to Amazon s3.

- `pip3 install boto3`
- `pip3 install django-storages`
- `pip3 freeze > requirements.txt`
- Add 'storages' to installed apps in settings.py

- in settings.py:

```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'crazyburger'
    AWS_S3_REGION_NAME = 'EU (London)'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Add these config vars in Heroku: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS.
- Delete Config Var for DISABLE_COLLECTSTATIC

- create custom_storages.py in main project folder. NB CHECK this location carefully. It should be at the same level as README.md
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
- update EU (London) to eu-west-2 in settings.py

* Add cache control:
```
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```

- Go to s3 and create a new folder called media. Upload all product images.
- Grant public permissions.

* Tidying up

- attempt to log in as admin (causes allauth to attempt to verify)
- in django admin panel, verify email address and make primary for the super user account.

* Stripe
- Add Stripe Keys to heroku config vars.
- Add new Stripe Webhook Endpoint. (Remember to tick viewing test data)
- Configure endpoint as follows:
- https:/crazyburger.herokuapp.com/checkout/wh/
- Select Receive all events.
- Add Endpoint.
- Add signing secret to Heroku Config Vars.
- Should now have: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET - all matched to what exists in settings.py
- send test webhook from Stripe to check.

## Email setup.

* In Gmail:
- Settings (cog)
- Accounts and import
- Other Google Account Settings
- Security
- 2 Step Verification
- Verify
- Turn On
- Under Signing in to Google heading, choose app passwords.
- Create app passwords: Type Mail / Other / enter django in the box.
- Copy the key and enter it in the Heroku app as a config var as EMAIL_HOST_PASS
- Create EMAIL_HOST_USER as the gmail account.

* In settings.py:
```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'crazyburger@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

<a href="#index">Back to top ☝️ </a>
<span id="credits"></span>

# 6. Credits 💳

A big thank belongs to:

- Again, to my family
- Again, to Adegbenga Adeye - my mentor, for guidance and feedback on this project
- Code Institute team
- Chris Zielinski - ckz8780 for Butique Ado tutorial

## 6.1 References

- Butique Ado
    https://github.com/ckz8780/boutique_ado_v1

- Hero image by Adrian Dorobantu was sourced from Pexels:
    https://www.pexels.com/photo/cheeseburger-on-table-2089717/

- Deployment section
    https://github.com/jonburdon/boutique_ado_v1/blob/master/README.md

- Logo was created using Adobe Spark logo maker
    https://www.adobe.com/express/create/logo

- Changing Stripe font
    https://stackoverflow.com/questions/44915511/

- Remove ZIP/Postal code from Stripe element
    https://stackoverflow.com/questions/46863072/do-not-collect-zip-code-with-stripe

- Payment animation
    https://fontawesome.com/v5.15/how-to-use/on-the-web/styling/animating-icons

- Bootstrap toast remains on top (invisible)
    https://stackoverflow.com/questions/56028939/

- [Product pictures](https://github.com/Martin-ITT/MS4_Crazy_Burger/blob/main/pictures.md)
