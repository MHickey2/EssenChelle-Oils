# EssenChelle Oils: Milestone 5 Project


<p align ="center">      
   <img src="assets/readme/images/essenchelle-responsive.png"  alt="AmIResponsive" />       
</p>
<br/>  

 
# Introduction <a name="introduction"></a>

The EssenChelle Oils site is my 5th Project for the Code Institute and it is a full stack E-commerce site using the Django Framework and it includes Python, JavaScript, CSS and Bootstrap5. It utilizes Stripe payments. It has user authentication and Full CRUD functionality for the products and Blogs for the Superuser. The website deals with the sale of essential oils and their byproducts. The website would appeal to people who use or want to know more about Essential Oils and are interested in buying these products. This website has been built for educational purposes and the payment transactions are purely for demonstration only. If you want to test the payment functionality, you can use: Card number: 4242 4242 4242 4242  Exp: Future Date i.e. 05/25 and CVC can be any 3 numbers.

<br/>

[Visit the EssenChelle Oils Site]() 

[Visit the EssenChelle Repository](https://github.com/MHickey2/EssenChelle-Oils)

<br/> 

# Table of Contents <a name="toc"></a>

- [EssenChelle Oils: Milestone 5 Project](#essenchelle-oils-milestone-5-project)
- [Introduction ](#introduction-)
- [Table of Contents ](#table-of-contents-)
  - [1. UX Strategy ](#1-ux-strategy-)
    - [1. The Business Goals of the Website: ](#1-the-business-goals-of-the-website-)
    - [2. The Target Customer: ](#2-the-target-customer-)
    - [3. Site User Profile](#3-site-user-profile)
    - [4.  Site Goals](#4--site-goals)
      - [Return to Table of Contents](#return-to-table-of-contents)
  - [2. User Stories  ](#2-user-stories--)
      - [As a website User I can...](#as-a-website-user-i-can)
      - [As a logged in User I can... ](#as-a-logged-in-user-i-can-)
      - [As a website superuser, I can …..    ](#as-a-website-superuser-i-can-----)
  - [3. Agile Methodology](#3-agile-methodology)
      - [Return to Table of Contents](#return-to-table-of-contents-1)
  - [4. Design  ](#4-design--)
    - [1. Colour  Scheme  ](#1-colour--scheme--)
    - [2. Typography    ](#2-typography----)
    - [3. Imagery    ](#3-imagery----)
    - [4. Website Structure    ](#4-website-structure----)
    - [5. Wireframes    ](#5-wireframes----)
      - [Return to Table of Contents](#return-to-table-of-contents-2)
  - [5. Web Marketing](#5-web-marketing)
    - [1. E-Commerce Application Type](#1-e-commerce-application-type)
    - [2. Marketing Strategy](#2-marketing-strategy)
      - [**Facebook Page**](#facebook-page)
    - [3. Search Engine Optimization(SEO)](#3-search-engine-optimizationseo)
    - [4. XML Sitemap](#4-xml-sitemap)
    - [5. Robots.Txt File](#5-robotstxt-file)
  - [6. Features  ](#6-features--)
    - [1. Home Page   ](#1-home-page---)
    - [2. Products Page     ](#2-products-page-----)
    - [3. EssenChelle Products Page     ](#3-essenchelle-products-page-----)
    - [4. Product Details Page     ](#4-product-details-page-----)
    - [5. About Page     ](#5-about-page-----)
    - [6. Our Products Page     ](#6-our-products-page-----)
    - [7. Blog Page     ](#7-blog-page-----)
    - [8. Blog Details Page     ](#8-blog-details-page-----)
    - [9. Contact Page     ](#9-contact-page-----)
    - [10. Profile Page    ](#10-profile-page----)
    - [11. Product Favourites Page     ](#11-product-favourites-page-----)
    - [12. Shopping Bag Page     ](#12-shopping-bag-page-----)
    - [13. Checkout Page     ](#13-checkout-page-----)
    - [14. Checkout Success Page     ](#14-checkout-success-page-----)
  - [The following pages are also available, but only to the superuser on the site.](#the-following-pages-are-also-available-but-only-to-the-superuser-on-the-site)
    - [15. Add Product Page     ](#15-add-product-page-----)
    - [16. Edit Product Page     ](#16-edit-product-page-----)
    - [17. Delete Product Page     ](#17-delete-product-page-----)
    - [18. Add Blog Page     ](#18-add-blog-page-----)
    - [19. Edit Blog Page     ](#19-edit-blog-page-----)
    - [20. Delete Blog Page     ](#20-delete-blog-page-----)
    - [21. Signup Page   ](#21-signup-page---)
    - [22. Login Page   ](#22-login-page---)
    - [23. Logout Page   ](#23-logout-page---)
    - [24. Custom Error Pages  ](#24-custom-error-pages--)
    - [25. Admin Panel  ](#25-admin-panel--)
    - [26. Security Measures  ](#26-security-measures--)
      - [Return to Table of Contents](#return-to-table-of-contents-3)
  - [7. Future Implementation  ](#7-future-implementation--)
      - [Return to Table of Contents](#return-to-table-of-contents-4)
  - [8. Tools and Technology  ](#8-tools-and-technology--)
    - [Language Used:](#language-used)
    - [Technology Used:](#technology-used)
    - [Django Packages](#django-packages)
      - [Return to Table of Contents](#return-to-table-of-contents-5)
  - [9. Testing  ](#9-testing--)
      - [Return to Table of Contents](#return-to-table-of-contents-6)
  - [10. Bugs and Issues  ](#10-bugs-and-issues--)
    - [Resolved ](#resolved-)
    - [Unresolved ](#unresolved-)
      - [Return to Table of Contents](#return-to-table-of-contents-7)
  - [11. Deployment ](#11-deployment-)
    - [How to make a local Clone ](#how-to-make-a-local-clone-)
    - [How to fork a GitHub Repository ](#how-to-fork-a-github-repository-)
    - [Student Template ](#student-template-)
    - [Django Framework    ](#django-framework----)
    - [Deploying to Heroku ](#deploying-to-heroku-)
    - [Changes in Heroku  ](#changes-in-heroku--)
    - [Final Deployment](#final-deployment)
      - [Return to Table of Contents](#return-to-table-of-contents-8)
  - [Credits ](#credits-)
      - [Return to Table of Contents](#return-to-table-of-contents-9)
  - [Acknowledgements ](#acknowledgements-)
      - [Return to Table of Contents](#return-to-table-of-contents-10)
  - [Author Info](#author-info)

----

## 1. UX Strategy <a name="uxstrategy"></a>
----

<br/> 

### 1. The Business Goals of the Website: <a name="businessgoals"></a>      

- The website is an E-commerce site so a goal would be be to achieve a commercial success from sales within the site.
- Expand the customer base for the EssenChelle Oil company.
- Promote repeat customers and ensure the present customers have a good user experience.
- Use Social Media to increase awareness of the Site and strategically plan future growth of the Brand.
- Increased customer satisfaction for the site users.
- Improved retention of customers.
- Effective use of discounts and value offers. 
- Create content that will engage the users and encourage them to return for more.
- Make the shopping experience easy to manage for the Shopper.
- Attract visitors and convert them into customers.
- Encourage customers and visitors to communicate with the business and respond effectively to their requests.
- Use customer feedback to address any outstanding shortcomings and use the knowledge gained to possibly expand the current range of products.
  
  <br/> 

### 2. The Target Customer: <a name="targetcustomer"></a>    

- Anyone with an interest in essential oils and their byproducts.
    
- Anyone who wishes to buy EssenChelle Oil Products.  
- Anyone who has interest in joining the EssenCHelle Oil community and wants to learn more about our range of products. 
- anyone who wants to use essential oils in their home and are looking for essential oil burners.  
- anyone who wants to offer massage services or use massage oils for personal use and are looking for specific blends for therapeutic uses.
- anyone who would want to avail of special offer products which are related to essential oils.


 <br/>  

### 3. Site User Profile

The user is really anyone who has an interest in holistic health. They either have had some experience with essential oils or are new to Essential Oils and want to learn more about them and how to integrate them into their lives. They may want to buy products from the site or read blogs that have a focus on the benefits and the uses for the featured oils. They may also be interested in special offers related to essential oils and would like to browse the site for current deals within the site.

<br/>

### 4.  Site Goals

- The theme of the site is easy to understand and it is easy to navigate through the site content easily.
  
- The user will be able to use the search facility to find specific products by category or word search.
- The user will be able to buy Products in the EssenChelle range.
- The user will be able to maintain a profile on the site and can update their Profile details easily.
- The user will be able to avail of discount and offers within the site.
- The user will be able to view blogs and can add comments for individual blogs.
- The user can see full details for individual products and if logged in they can leave reviews.
- The user can contact the site owner with queries and suggestions.
- The user when logged in can choose their favourite products and these can be stored within the site.
- The user will be able to sign up for a regular newsletter. 

<br>

 #### [Return to Table of Contents](#toc)

----

## 2. User Stories  <a name="userstories"></a>

<br>

####  As a website User I can...<a name="websiteuser"></a>

1. Log in and access more features on the site.   
[As a user or staff member I can log in so that I can access the relevant features of the site #1](https://github.com/MHickey2/EssenChelle-Oils/issues/1)

1. Find the purpose of the site easily by reviewing the content.
[As a User I can easily find the site's purpose so that I know whether the site fits my needs #2](https://github.com/MHickey2/EssenChelle-Oils/issues/2)

3. View a collection of Products that are available for sale.
[As a User I can view a selection of Products so that I can choose some to purchase #3](https://github.com/MHickey2/EssenChelle-Oils/issues/3)

4. Select an individual item to see the full details for the product. 
[As a Site User I can choose an individual Product so that I can see required details #4](https://github.com/MHickey2/EssenChelle-Oils/issues/4)

5. View categories aqccording to their category type.
[As a Site User I can view specific categories of Products so that I can easily find the product I am looking for #5](https://github.com/MHickey2/EssenChelle-Oils/issues/5)

6. Easily be able to identify the cheapest or most highly rated products.
[As a Site User I can sort Products so that I can quickly identify the cheapest or most highly rated products within categories #6](https://github.com/MHickey2/EssenChelle-Oils/issues/6)

7. Sort products against a number of sorting critera.
[As a Site User I can sort multiple categories so that I can view all products within a sorting function #7](https://github.com/MHickey2/EssenChelle-Oils/issues/7)

8. Informed about the progress of my actions and interactions within the site.
[The Site User will be updated with messages confirming their actions on the site #12](https://github.com/MHickey2/EssenChelle-Oils/issues/12)

9. Be able to attain and view my profile within in the site.
[As a User, when I register I will have my own Profile which will include all my information #15](https://github.com/MHickey2/EssenChelle-Oils/issues/15)

10. Receive an email when I register for the site.
[When registering a User will receive a welcome email #16](https://github.com/MHickey2/EssenChelle-Oils/issues/16)

11. Will be able to contact the site owner with the contact form.
[User can use the contact form so they can message the site owner with queries or requests #21](https://github.com/MHickey2/EssenChelle-Oils/issues/21)

12.  View a collection of Blogs in the blog Section.
[User can view a selection of blogs with information on the range of products #22](https://github.com/MHickey2/EssenChelle-Oils/issues/22)

13. User can select a blog and see the full details for that individual blog.
[User can select individual blogs and see the full details on the blog details page #24](https://github.com/MHickey2/EssenChelle-Oils/issues/24)

<br>


####  As a logged in User I can... <a name="loggedinuser"></a> 

1. Select products and these will be included in my shopping bag.
[The Shopper will be able to select various products and these will be added to their shopping Bag #8](https://github.com/MHickey2/EssenChelle-Oils/issues/8)

2. View the Total of my purchases on the site.
[The Shopper can view the total of their purchases as they shop on the site #9](https://github.com/MHickey2/EssenChelle-Oils/issues/9)

3. Select products in different sizes where available.
[The Shopper will be able to choose products in a range of sizes #10](https://github.com/MHickey2/EssenChelle-Oils/issues/10)

4. Choose to remove or adjust the items in my shopping bag.
[The Shopper will be able to adjust or remove items from their shopping bag #11](https://github.com/MHickey2/EssenChelle-Oils/issues/11)

5. Checkout the products in my shopping bag.
[The Shopper will be able to checkout the products they have added to their shopping bag #13](https://github.com/MHickey2/EssenChelle-Oils/issues/13)

6. Make a secure payment for my purchases.
[The Shopper will be taken to a secure payment screen so they can safely make their purchase #14](https://github.com/MHickey2/EssenChelle-Oils/issues/14)

7. Add a review for products on the site.
[As a registered User I can add reviews for product available on the site #20](https://github.com/MHickey2/EssenChelle-Oils/issues/20)

8. Select my favourite products on the site and save them to my product favourites.
[As a logged in user I can select my favourite products and be able to see them later #27](https://github.com/MHickey2/EssenChelle-Oils/issues/27)

9. Leave a comment for a blog in the blog section.
[Logged in user can add comments to blogs in the site #28](https://github.com/MHickey2/EssenChelle-Oils/issues/28)

10. Sign up for a newsletter so I can receive special offers and the latest product information.
[User can sign up for the newsletter and receive special offers and the latest information from the site #29](https://github.com/MHickey2/EssenChelle-Oils/issues/29)

 
 <br/>

#### As a website superuser, I can …..    <a name="superuser"></a>

1. Add Products to the Database.
[As an Admin I can add products to the database #17](https://github.com/MHickey2/EssenChelle-Oils/issues/17)

2. Edit Products in the Database.
[The Admin will be able to edit products in the database #18](https://github.com/MHickey2/EssenChelle-Oils/issues/18)

3. Delete Products in the Database.
[The Admin will be able to delete products from the database #19](https://github.com/MHickey2/EssenChelle-Oils/issues/19)

4. Add Blogs to highlight products on the site.
[Superuser can add blogs which will highlight the Essenchelle product range available on the site #23](https://github.com/MHickey2/EssenChelle-Oils/issues/23)

5. Edit Blogs on the site.
[The Superuser can edit existing blogs on the site #25](https://github.com/MHickey2/EssenChelle-Oils/issues/25)

6. Delete Blogs on the site.
[The Superuser can delete existing blogs on the site #26](https://github.com/MHickey2/EssenChelle-Oils/issues/26)

7. Approve reviews for Products and comments for Blogs in the admin Panel


The Admin can do the full range of admin functionality within the admin panel.
User Story Testing can be found in the [TESING.md](TESTING.md)

  <br/> 

## 3. Agile Methodology

The project was developed using Agile Methodology and it was by use of the GitHub Projects functionality within the GitHub Repository. The issues can be found [Here](https://github.com/MHickey2/EssenChelle-Oils/issues) and this is the link for the [Essential Oils Project Board](https://github.com/users/MHickey2/projects/2)

<br/> 

#### [Return to Table of Contents](#toc)  
----

## 4. Design  <a name="design"></a> 

<br/>

### 1. Colour  Scheme  <a name="colourscheme"></a>

The colour scheme was inspired by essential oils, in particular lavender oil, so the website uses a darker shade of this colour throughout the site. The color Lavender represents holistic wellness and it is known for its tranquility and calming effects. Lavender Oil is also one of the most popular oils and very versatile so it made sense to utilize it's popularity and use a colour most holistic users would be familiar with. The background of the site pages are either white or lavendender where suitable. Headings, borders and the footer are purple. In this project I wanted to only have a subtle use of colour, so that there would be little distraction to the user, when making their purchases on the site.

<br>
<p align ="center">      
   <img src="assets/readme/images/colourcombo.png"  alt="Colour Combo" />
        
</p>
<p align ="center">      
   colors=#800080, #E83E86, #9037E4, #E9AFE9, #2D023D
        
</p>


<br/> 

### 2. Typography    <a name="typography"></a>

Google Fonts were used within the website. The 'Roboto' font is the main font used for the whole project.. Sans serif is the fallback font in case the other font is not available. See below for example of font in use on the site. The font color is #313131, which is a good font to help counter eye strain.

<br>
<p align ="center">      
   <img src="assets/readme/images/313131.png"  alt="general font colour for site" />        
</p>

<br>

The main title for the site, the navigaton items and the headings for the site use the Courgette Font, which is a google font. It is a medium-contrast, brushy, italic-script typeface, which has been made for the web. It adds a decorative flair but is also very legible on a screen. 

<br>
<p align ="center">      
   <img src="assets/readme/images/courgettefont.png"  alt="courgette font" />        
</p>

<br>

<p align ="center">      
   <img src="assets/readme/images/"  alt="" />        
</p>

<br>


### 3. Imagery    <a name="imagery"></a>

The Logo was created with [LogoMaker](https://www.logomaker.com/), I used a health and beauty related theme for the logo, as essential oils are synonymous with health and beauty benefits. The logo features a beautiful woman's face which has the EssenChelle Oil Brand prominant in its design. The colour used fits the colours displayed in the website.

The imagery of the site focuses on essential oils and their byproducts, the images were sourced from the Pexels site and supplement the content. The images for the site are hosted in [Cloudinary](https://cloudinary.com/). I had used AWS for a while but was not comfortable using aws, as it was unpredictable in regards to pricing, and I chose to revert to cloudinary as I trusted this platform, from my previous use.

There are also images sporadically placed throughout the site, There is a background image of a massage which highlights the nature of the site on the index page, the product was initially a template with blank packaging detail, so I used photoshop to apply the EssenChelle brand image for the different products in the essential and massage oil range. The aromatherapy burners were sourced on a shopping site platorm, as it did not have to have the essenchelle branding. The Items in the special offer section were also sourced in the Pexels site.

<br>

<p align="center">
  <img src="assets/readme/images/collage.png" width="600" alt="Images for Site"/>
</p>

<br/>

There are also various icons used within the site, the icons were sourced at [Iconify.Design](https://iconify.design/) and font-awesome in some cases, and they were used as a graphical representation for pertinent information on the site, they were used in conjunction with Forms or headings and were a subtle way to incorporate imagery on a limited scale, examples can be found in the image below.

<br>

<p align ="center">      
     <img src="assets/readme/images/icons.png"  alt="icons for Site" />    
</p>

<br/>

I also created the favicon for the site with [Favicon.io](https://favicon.io)

<br>

<p align ="center">      
     <img src="assets/readme/images/android.png" width="100px" alt="Favicon for Site" />    
</p>

<br/>


### 4. Website Structure    <a name="structure"></a>

The website follows the standard website structure. The Logo and the website name are on the left hand side, and the naigation to the right, on the top of all pages. Within the Account Nav top Link the user can either Signup or login to the site. When the user logs in they can see the Profile link, The favourite products and the logout button. The Shopping Bag Link takes the User to the Shopping Bag Page.When the website is on smaller screens, there is a hamburger meu, with dropdown navigation items. The footer element is also available on all pages, with site information, contact details, social media icons and the newsletter sign up form.

The website consists of the following Pages:
 - The Home Page, with a hero image and a button connecting to the Shop. It has a search bar and links to
  all areas in the site. There is is also a profile and shopping back link.
 - The Products page is available in a number of formations, it can be sorted by pricing, ratings and category and you can see all products in the EssenChelle Range.
 - The Essenchelle Products can be configured to show different categories of products. The products include Essential Oils, Massage Oils and Oil Burners, or you can view all categories at once.
 - The Product Details Page, shows the information for individual Products.
 - The Add Product Page, which is a form that allows the superuser to add a Product.
 - The Edit Product Page, which is a form that allows the superuser to edit a Product.
 - The Delete Product Page, which is a form that allows the superuser to delete a Product.
 - The Bag Page which shows the details of the products presently in the Bag.
 - The Checkout Page, which shows the details of an order and the user details form and checkout       submission button.
 - The Checkout Submission page, which shows the order details and price and Thank you message.
 - The About Page, which gives more information on the site 
 - The Our Products Page, with an introduction to EssenChelle Products by category and it includes customer testimonials.
 - The Blog Page with a spotlight on products, it highlights individual products and blogs can only be
  added by the superuser.
 - The Blog Detail Page, that shows the information for individual Blogs.
 - The Add Blog Page, which is a form that allows the superser to add a Blog.
 - The Edit Blog Page, which is a form that allows the superuser to edit a Blog.
 - The Delete Blog Page, which is a form that allows the superuser to delete a Blog.
 - The Profile Page, which contains profile information and  product history for the logged in user.
 - The User Product Favourites Page, which shows the users favourite products.
 - The Sign Up Page, consists of a form where a new user can register for the site.
 - The Login Page, consists of a form where the user can login to the site.
 - The logout Page, consists of a form where the user can logout of the site.
 - There are also custom error pages for errors 403,404,405 and 500.

<br/>

### 5. Wireframes    <a name="wireframes"></a>

The Wireframes for the site were created in Figma, I concentrated on the standard websize and the mobile size. The mid-level sizes were generally in keeping with the main websize but just on a smaller scale. The Wireframes can be found below:

<details><summary>Figma Wireframes</summary>


<details>


  <summary>1. Home Page Wireframes</summary>
  <br/>
  <p align="center">
     <img src="assets/readme/wireframes/home pages.png"  alt="Home Page Wireframes" />    
</p>
</details>

<details>
  <summary>2. Products Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/product pages.png" alt="Product Page Wireframe"/>
</p>
</details>

<details>
  <summary>3. EssenChelle Product Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/essenchelle product pages.png" alt="Essenchelle Product Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Product Details Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/product details page.png" alt="Product Details Page Wireframe" />
</p>
</details>

<details>
  <summary>5. AboutPage</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/about Pages.png" alt="About Page Wireframe" />
</p>
</details>

<details>
  <summary>6. Our Products Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/our products pages.png" alt="Our Products Page Wireframe" />
</p>
</details>

<details>
  <summary>7. Blog Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/blog pages.png" alt="Blog Page Wireframe" />
</p>
</details>

<details>
  <summary>8. Blog Details Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/blogdetails.png" alt="Blog Details Page Wireframe" />
</p>
</details>

<details>
  <summary>9. Contact Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/contact pages.png" alt="Contact Page Wireframe" />
</p>
</details>

<details>
  <summary>10. My Profile Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/my profile pages.png" alt="My Profile Page Wireframe" />
</p>
</details>

<details>
  <summary>11. Favourite Products Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/favourites page.png" alt="Favourites Page Wireframe" />
</p>
</details>

<details>
  <summary>12. Shopping Bag Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/shopping bag pages.png" alt="Shopping Bag Page Wireframe" />
</p>
</details>

<details>
  <summary>13. Checkout Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/checkout pages.png" alt="Checkout Page Wireframe" />
</p>
</details>

<details>
  <summary>14. Checkout Success Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/checkoutsuccess.png" alt="Checkout Success Page Wireframe" />
</p>
</details>

<details>
  <summary>15. Add Products Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/product management pages.png" alt="Product Management Page Wireframe" />
</p>
</details>

<details>
  <summary>16. Edit Product Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/edit product pages.png" alt="Edit Product Page Wireframe" />
</p>
</details>

<details>
  <summary>17. Delete Products Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/delete product pages.png" alt="Delete Product Page Wireframe" />
</p>
</details>

<details>
  <summary>18. Add Blog Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/addblog pages.png" alt="Add Blog Page Wireframe" />
</p>
</details>

<details>
  <summary>19. Edit a Blog Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/edit blog page.png" alt="Edit Blog Page Wireframe" />
</p>
</details>

<details>
  <summary>20. Delete a Blog Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/delete blog pages.png" alt="Delete Blog Page Wireframe" />
</p>
</details>

<details>
  <summary>21. Registration Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/register pages.png" alt="Registration Page Wireframe" />
</p>
</details>

<details>
  <summary>22. Log In Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/login pages.png" alt="Login Page Wireframe" />
</p>
</details>

<details>
  <summary>23. Logout Page</summary>

  <br/>
<p align="center">
  <img src="assets/readme/wireframes/logout pages.png" alt="Logout Page Wireframe" />
</p>
</details>

</details>

<br>

 #### [Return to Table of Contents](#toc)
----

<br>



## 5. Web Marketing

<br>

### 1. E-Commerce Application Type
EssenChelle Oil is a B2C E-Commerce Application. It deal with seling directly to its customer. There is a great emphasis in promoting a good user experience for the customer. The aim is to retain current customers and at the same time grow the customer base by organic means. Because it is online it can reach a wide audience and is not dependent on location. Overhead and operational costs are reduced because there is no physical premises. The Direct to consumer business model has the advantage of being able to charge lower prices, which is a great incentive for customers. The business can run 24 hours a day and this allows flexibility for the business owner as they are not confined to normal business hours.

<br>

### 2. Marketing Strategy
Essenchelle Oils is a fledgling company, with a limited budget for marketing, so decisions need to be cost effective and practical. That being said the company has come up with a range of marketing strategies, ie content marketing, utilizing social media platforms, digital promotions, and highlighting events that will promote the products firsthand. The goal is is to increase project sales, create a following online and concentrate on building brand awareness.

<br>

Social Media will play a big part in the marketing strategy, research into the different platforms has highligted ways that can be cost effective and easy to implement. Facebook is a great way to build up followers and share information with a wide number of customers. A Facebook page was created to share pertinent information with the users, and will be used to promote the latest deals, that should entice new customers to the EssenChelle site. The image below shows the Facebook page, it is active currently but not sure if it will remain so, so have included screencapture below and here is the link: [EssenChelle Oils](https://www.facebook.com/profile.php?id=100090771283240)

#### **Facebook Page**

<br>

<p align="center">
  <img src="assets/readme/images/facebookpage.jpg" alt="EssenChelle Facebook Page" />
</p>

<br>

Content Marketing: the process of publishing written and visual material online with the purpose of attracting more leads to your business is the essence of content marketing. In this case the website has a blog section which highlighs the products in the EssenChelle range. The main focus is on showing the customer the benefits of specific oils to the customers, why they should buy them and how they can use them. This should drive more sales and funnel the user to the products page. Selected blogs can also be shared on various social media channels, furthering the reach of the created content.

<br>

<p align="center">
  <img src="assets/readme/images/blogposts.png" alt="Blog Section" />
</p>

<br>

Google Ads : This option is out of reach at the moment, as the budget is small, but with enough experience and analysis I hope to be able to plan a campaign in the future that will be cost effective and will pay long lasting dividents.

<br>

Events: There is a large industry dealing with essential oils and aromatherapy in Ireland, and indeed worldwide. In this regard you can tap into existing events that are used to promote the industry and that are very accessible to the public. One of the largest event, occurs yearly in the RDS in the Body Mind Spirit fair where a range of companies, mostly smaller companies have the opportunity to highlight their products to a very involved and motivated audience. You have the opporuity to mingle with and sell directly to the public and grow a valuable network which will be a great boost for future business. This would play a major part in growing the brand and linking with a potentially large customer base. But this occurs later in the year, and meantime smaller events, in this vein are held in venues throughtout the country and would be an excellent way to connect with the right clientele. As well as growing a customer base it wold be good to network with other business's and there may be some mutual gains in forging such alliances. The image below shows the Expo details:

<br>

<p align="center">
  <img src="assets/readme/images/bodymindspirit.png" width="700" alt="Body Mind Spirit Expo" />
</p>

<br>

The website itself offers users the chance to sign up for a regular newsletter. This measure allows you communicate directly with your prospects and customers in a personalized way by serving valuable content and relevant promotions straight to their inboxes. This newsletter would be a good way to promote new products, provide articles highlighting the benefits of using certain products, offer special offers and highlight new arrival products. This will be a great way to grow the Essenchelle community and keep the customers in the loop. The newsletter functionality utilizes mailchimp, this service will help keep track of users. Mailchimp offers a number of tools that will be explored further as the company develops.

<br>

<p align="center">
  <img src="assets/readme/images/newsletter.png" alt="Mailchimp Newsletter" />
</p>

<br>


###  3. Search Engine Optimization(SEO)
SEO research will help drive pople to our site more efficiently. Inititally finding the right keywords will help send our site further up in the rankings. Finding the right words involved looking at present sites, previous research finding and analysing which words were suggested when searching for essential oils and aromatherapy in particular. I used [wordtracker.com](https://www.wordtracker.com/) and various other free tools to find keywords, the factors that determined the ones chosen include search volume, relevance and conversion value. I then picked the top words and phrases and integrated them into the site via meta-tags or by ensuring they were included in headings, image names and content. It was important not to overdo the use of these words as this would have been counterproductive to the end goal. The following image shows a sample of the results found and used in the site:

<br>

<p align="center">
  <img src="assets/readme/images/keywordsearches.png" width="700" alt="Keyword Search" />
</p>

<br>

There were also links included for both internal pages and external sites of good standing that are in a similar industry. I have an external link in the blog page in the sidebar, the site is not information heavy so I linked to a reputable site, that had more detailed information on safety precautions. The site used can be found [here](https://www.everydayhealth.com/wellness/what-are-essential-oils-a-complete-guide-on-aromatherapy-and-its-potential-health-benefits/) 

<br>

<p align="center">
  <img src="assets/readme/images/externallinksite.png"  width="600" alt="External Site on Health and Benefits" />
</p>

<br>

### 4. XML Sitemap
Additionally to help the search engines crawl the site, I've added an XML sitemap file to the main root directory. This was generated using [xml-sitemaps](https://www.xml-sitemaps.com/)

<br>

### 5. Robots.Txt File
A robots.txt file has also added to allow the search engine crawlers to know which URLs the crawler can access on this ste, this was used mainly to avoid overloading the site with requests.

<br>

---


## 6. Features  <a name="features"></a>

There are features common to all pages in the site and these are found in the base.html page. These include:

- The Logo and Site Title:
  
The logo was the first asset I created in Logo maker, it depicts a simple female face image using the main colours displayed in the site. The Logo includes the name of the site, so the logo is synonomous with the brand. Using the name in the logo meant I had a readymade image for the packaging of the products in the range. The image relates to the area of health and Beauty, as essential oils are strongly related to the promotion of health and beauty benefits. 

<br>

<p align ="center">      
     <img src="assets/readme/images/essenchelle-logo.png"  alt="Logo with Title" />    
</p>

<br/> 

There is a searchbar, where the user can put in their search criteria term. There is an Account Icon, which contains a dropdown menu:

Account Icon - Register, Log In (Before Log in or registering)
Account Icon - Product Management, My Profile, Product Favourites, Log Out. (If logged in)

Shopping Bag Icon - Takes you to the Shopping Bag Page.

- The Navigation Bar:

The navigation consists of the following options: All Products, EssenChelle Products, Our Story, Special Offers and Contact. Each of these Nav items have dropdown menus:

All Products - By Price, By Rating, By Category and All Products.
EssenChelle Products - Essential Oils, Massage Oils, Oil Burners and All Products.
Our Story - About Us, Our Products and Blog.
Special Offers - New Arrivals, Deals, Clearance and All Specials.
Contact - Contact Form.
  <br>

<p align ="center">      
     <img src="assets/readme/images/navigation.png"  alt="Navbar options" />    
</p>

<br/> 


On smaller screens, there is a hamburger menu where the navigation items appear in a collapsible dropdown menu. The image below shows the collapsible menu for smaller screens.

<br>

<p align ="center">      
     <img src="assets/readme/images/mobile navbar.png"  width="300" height="250" alt="navbar mobile" />    
</p>

<br/> 

- The Footer:
The Footer contains a blurb on the site, some contact details and social media icons, also the copyright information on the EssenChelle Oils site. THe footer also includes a newsletter sign up form provided by mailchimp.

 <br>

<p align ="center">      
     <img src="assets/readme/images/footer.png"  width="600px" alt="footer" />    
</p>

<br>

### 1. Home Page   <a name="homepage"></a>

The home page has a Hero image depicting a massage session, which is a strong indicator to the type of productss available within the site. There is some textual content describing the site purpose. There is also a shop button, that can bring the user directly to the product page, so that the user can begin shopping right away.
There was an issue with getting a screencap of the page, because of the background, so its a little off.(It looks better in real life)
  
<br>

<p align ="center">      
     <img src="assets/readme/images/homepage.png" width="400" alt="Home Page" />    
</p>

<br/> 

### 2. Products Page     <a name="productpage"></a>

The products page shows the the full collection within the EssenChelle range including the special offers. These products can be arranged according to specified criteria, such as by price, by rating and by category. The number of items is shown to the user and the user can further sort the products by means of the sorting bar. Each of the products shows the title, an image, the price, the category, the star rating and will show users if there are any associated reviews for the product.

<br>

<p align ="center">      
     <img src="assets/readme/images/productsPage.png"  width="500"  alt="products page" />    
</p>

<br/> 

### 3. EssenChelle Products Page     <a name="essenchelleproductpage"></a>

<br>
This Page shows products in the category of Essential, Massage and Burners. You can select to see products within just one category by choosing the option in the dropdown menu or by selecting the relevant link at the top of the page. You can view the number of products and there is a facility for sorting at the top of the page. The options for sorting includes price, rating, name and category.

<br>

<p align ="center">      
     <img src="assets/readme/images/essenchelleprod.png" width="500" alt="Essenchelle product Page" />    
</p>

<br>

### 4. Product Details Page     <a name="productdetailspage"></a>
The Page shows the full details of an individual product including an image. There is a review form, where a product user who is logged in can leave a review for others. This review will need to be approved by the superuser before it is published to the review section. the review section shows existing reviews. There is a add to favourites button to the right of the product title, when this is clicked, the product is saved to the user's favourites. Any product which has been selected as a favourite, can be viewed in the product favourites page (can be found using the account icon when user is logged in).

<br>

<p align ="center">      
     <img src="assets/readme/images/proddetailpage.jpg"  width="500"  alt="product detail page" />    
</p>

<br/>

### 5. About Page     <a name="aboutpage"></a>

The About Page provides the background information on the EssenChelle Oil Company, It also features a carousel with information on the different categories of products on offer in the site.

<br>

<p align ="center">      
     <img src="assets/readme/images/aboutpage.jpg"  width="500"  alt="about page" />    
</p>

<br/> 

### 6. Our Products Page     <a name="ourproductpage"></a>

The our products page shows more indepth information on each category in the product range. It also provides customer testimonials on why a potential customer should choose a product in the EssenChelle Product Range.

<br>

<p align ="center">      
     <img src="assets/readme/images/ourprod.jpg"  width="500"  alt="our products page" />    
</p>

<br/> 

### 7. Blog Page     <a name="blogpage"></a>

The Blog Page shows a collection of blogs with a spotlight on products being sold on the site. The sidebar gives a brief introduction to the blogs. There is a link within the sidebar to an accredited site with more comprehensive information on individual essential oils. It also shows the titles for the 5 latest blogs available.

<br>

<p align ="center">      
     <img src="assets/readme/images/blogpage.jpg"  width="500"  alt="blog page" />    
</p>

<br/>

### 8. Blog Details Page     <a name="blogdetailspage"></a>
The Blog Detail page shows the full blog which has information pertaining to selected products on the site. It will either concentrate on an individual oil(lavender oil), or a selection of products(top 5 massage oils), it may also include internal links to the highligted products within the site . There is also a comment form, for logged in users to leave a comment and there is a comment section for existing comments.

<br>

<p align ="center">      
     <img src="assets/readme/images/blogdetail.jpg"  width="500"  alt="blog details page" />    
</p>

<br/>


### 9. Contact Page     <a name="contactpage"></a>
The contact page has a map showing the location of the Company and a contact form so that the user can send a message to the company. This will aid communication between the user and the EssenChelle Oil Co. this could include queries on the sales process, more information on specific properties of products or questions in relation to delivery issues.

<br>

<p align ="center">      
     <img src="assets/readme/images/contactpage.jpg"  width="500"  alt="contact page" />    
</p>

<br/>

### 10. Profile Page    <a name="profile page"></a>
The Profile page contains a form to update the customer's default delivery information and order history. It also allows the user to enter their credit/debit card details and there is a checkbox where the user can tick if they want this information to be saved on the site.
<br>

<p align ="center">      
     <img src="assets/readme/images/myprofile.jpg"  width="500"  alt="profile page" />    
</p>

<br/>

### 11. Product Favourites Page     <a name="favouritespage"></a>
The Page shows a collection of the user's product favourites. The details and image of each product are displayed. There is a button with remove below each product and when this is selected that product will be removed from the user's favourites.

<br>

<p align ="center">      
     <img src="assets/readme/images/productfavourites.jpg"  width="500"  alt="product favourites page" />    
</p>

<br/>

### 12. Shopping Bag Page     <a name="shoppingbagpage"></a>
The Page shows the products that the user has currently in their shopping bag. This will initially display no products, but as products are added, they will be displayed on the page. There is a keep shopping button and this allows the user to return to shop for more products.
<br

<p align ="center">      
     <img src="assets/readme/images/bagpage.jpg"  width="500"  alt="shopping bag page" />    
</p>

<br/>

### 13. Checkout Page     <a name="checkoutpage"></a>
The Checkout Page shows the form to complete the order and the order summary. You can adjust your bag or you can complete your order.
<br>

<p align ="center">      
     <img src="assets/readme/images/checkoutpage.jpg"  width="500"  alt="checkout page" />    
</p>

<br/>

### 14. Checkout Success Page     <a name="checkoutsuccesspage"></a>
The Page is shown to the user when their order has been processed. It contains a Thank you message and includes the order information, order details, delivery details and billing information,  and a link to the new arrival products on the site. There is also a success message displayed advising the user that their order has been processed successfully and a confirmation email will be sent to them.

<br>

<p align ="center">      
     <img src="assets/readme/images/checkoutsuccess.jpg"  width="500"  alt="checkout success page" />    
</p>

<br/>

<p align ="center"> 
  ## The following pages are also available, but only to the superuser on the site. ##
</p>

<br>

### 15. Add Product Page     <a name="addproductpage"></a>
This Page is also the product management page. The superuser can add a product in the frontend as well as in the admin panel. It can be accessed via the account icon or with a button at the left and bottom of the products page.(which I found more intutive to user)

<br>

<p align ="center">      
     <img src="assets/readme/images/addproduct.jpg"  width="500"  alt="add product page" />    
</p>

<br/>

### 16. Edit Product Page     <a name="editproductpage"></a>
The Page has a form which allows the superuser to edit product details for individual products. It can be found below the product details in the products page and on the product detail page.

<br>

<p align ="center">      
     <img src="assets/readme/images/editproduct.jpg"  width="500"  alt="edit product page" />    
</p>

<br/>

### 17. Delete Product Page     <a name="deleteproductpage"></a>
The Page has a form which allows the superuser to delete products. It can be found below the product details in the products page and on the product detail page.
<br>

<p align ="center">      
     <img src="assets/readme/images/deleteproduct.jpg"  width="400"  alt="delete product page" />    
</p>

<br/>

### 18. Add Blog Page     <a name="addblogpage"></a>
The Page has a form which allows the superuser to add a blog to the blog collection. The button is available on the bottom and left of the blog page.

<br>

<p align ="center">      
     <img src="assets/readme/images/addblog.jpg"  width="500" alt="add blog page" />    
</p>

<br/>

### 19. Edit Blog Page     <a name="editblogpage"></a>
The Page has a form which allows the superuser to edit an existing blog. The link to edit a blog can be found at the bottom of individual blogs in the blog page.

<br>

<p align ="center">      
     <img src="assets/readme/images/editblog.jpg"  width="500"  alt="edit blog page" />    
</p>

<br/>

### 20. Delete Blog Page     <a name="deleteblogpage"></a>
The Page has a form which allows the superuser to delete an existing blog. The link is available at the bottom of individual blogs in the blog page.

<br>

<p align ="center">      
     <img src="assets/readme/images/deleteblog.jpg"  width="400"  alt="products page" />    
</p>

<br/>
 

###  21. Signup Page   <a name="signuppage"></a>

On the Signup Page, a new user can sign up for the EssenChelle Oils website by filling out and submitting the form. On registering they will be assigned a Profile for the site. On registering they will be sent an email confirming their registration. 

<br>

<p align ="center">      
     <img src="assets/readme/images/signup.jpg" width="400"  alt="Registration Page" />    
</p>

<br/>

###  22. Login Page   <a name="loginpage"></a>

A registered User can log in to the website by inputting their username and password and they will have full access to all the logged in features within the site. 


<br>

<p align ="center">      
     <img src="assets/readme/images/login.jpg" width="400" alt="Login Page" />    
</p>

<br/> 

###  23. Logout Page   <a name="logoutpage"></a>

In the Logout Page, the User can confirm that they want to exit the website.

<br>

<p align ="center">      
     <img src="assets/readme/images/logout.jpg" width="400"  alt="Logout Page" />    
</p>

<br/> 

### 24. Custom Error Pages  <a name="error pages"></a>

I have included custom Error Pages in the error folder within the templates folder(403,404,405,500), Below is the image from the 404 page, but they all look similar, barring the fault lines.

<br>

<p align ="center">      
     <img src="assets/readme/images/errorpage.png" width="500"  alt="Sample Error Page" />    
</p>

<br/> 

### 25. Admin Panel  <a name="adminpanel"></a>

The admin panel allows the admin/superuser to perform a wide range of functionalities within the site. The admin can add, delete, edit products, blogs, users. The admin can also approve reviews for individual products and comments for individual blogs.

<br>

<p align ="center">      
     <img src="assets/readme/images/adminsignin.png" width="200" alt="Admin sign in" />    
</p>

<br>

<p align ="center">      
     <img src="assets/readme/images/adminpanel.jpg" width="900" alt="Admin Panel" />    
</p>

<br/> 

### 26. Security Measures  <a name="security"></a>

To ensure security on the site, only logged in users can access certain features on the site. A logged in user can add a product review or comment for a blog in the blog section. A superuser can add, updata and delete products within the admin panel. The superuser also has access to add, edit and delete products within the product pages. The superuser can add, edit and delete blogs in the admin panel but they can also access these capabilities within the blog page. Only the Admin/Superuser can access the admin Panel(would need sign in credentials).The Database URL and secret key are stored in the env.py file to prevent unwanted connections to the Database. As I was following the boutique ado walkthrough, I had not realised the secret key was commited in the early stages of the development, after doing my research into the issue and with the advice from CI, I generated a new key, and this was immediately put in the env.py file, making the other key obselete. All secret keys were included in the env.py file. Cross-Site Request Forgery (CSRF) Tokens are used on all Forms within the App for added protection. All keys needed for the inclusion of AWS, CLoudinary and Stripe were concealed for security purposes.

<br>

<p align ="center">      
     <img src="assets/readme/images/security.png"  alt="Can't Access Message" />    
</p>

<br/> 


 #### [Return to Table of Contents](#toc)
----

 ## 7. Future Implementation  <a name="future"></a>

 <br>

 This is my first E-Commerce Site, so the main goal is to have a fully functional site with customised models to expand on the original concept as defined in the Boutique Ado Walkthrough. There were a number of features that I would like to expand upon in the future.

 In relation to the products, I would like to expand the information relating to the product. Besides the description, I would ike to include directions for use and cautions. You could also sort products according to the health conditions that can be addressed by using them i.e. insomnia, anxiety, respiratory issues.

 In regards to the blogs I have just added a few basic blogs, with heavy emphasis on product spotlighting for marketing purposes. These blogs could also be broken down into further categories. I could add a do it yourself section, where you could provide simple instructions for users to use the products in creative ways, this is incorporated into the present blog in a small way, but would be a great way for users to learn to integrate the products into their lives. I would also include a recipe category where you could provide the user with recipes using the essential oils. This could be a good way to get users to interact with the site. you could ask the users to contribute their own recipes via the social media channels or by contacting the company directly with the contact form. User's recipes could then be featured on the site. Healthy Living could also be a category and you could give advice on how to use oils in the home and provide tips for everyday living in relation to EssenChelle Oils. These measures should not only drive sales, but should help to create a a thriving community with a shared interest in essential oil and their byproducts.

 In regard to the profiles, I would customise it more for the user, in the previous project I had an image for the profile user, but would rather ensure I meet all the project criteria first, and if there is time at the end I could explore this possibility, but would hope to introduce this in a future iteration.

 In regard to the review, I had looked into the idea of using the ratings in the reviews in the product rating, again this is still a possibility, but time restraints this may not make this possible at this time. It would be easier at this time to use existing ratings, as it would take time to generate actual ratings and with this restraint new products would not have any rating, and this would not be ideal. i

 In regards to logging in, I would also include logging in from a social network provider like Facebook, Twitter, or Google to facilitate the user further.

 In regards to deals I would introduce deals to encourage the user to buy multiple products at a special rate, from a marketing perspective I feel this would be conducive to more sales. In the long term I would also introduce a loyalty scheme, so that users would be rewarded for their consumer buying behaviour.


 
 <br>

#### [Return to Table of Contents](#toc)
----

 ## 8. Tools and Technology  <a name="technology"></a>

### Language Used:

-   [Python 3.8.10](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)    
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://www.javascript.com/)
-   [Django](https://www.python.org/)

### Technology Used:

-   [Am I Responsive](http://ami.responsivedesign.is/) - was used to create the multi-device mock-up above.
-   [Bootstrap v5.2.3](https://getbootstrap.com/)
-   [Git:](https://git-scm.com/) - used for version control, updated and commited changes (this in turn updated site in Heroku). 
-   [GitHub:](https://github.com/) - is the respository for all the git pushes.
-   [Gitpod](https://gitpod.io/) - was the IDE Editor.
-   [Heroku:](https://heroku.com) - used to deploy the application.
-   [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for Testing Site.
-   [Markdown](https://markdown-guide.readthedocs.io/en/latest/) - Markdown Guide.
-   [Cloudinary](https://cloudinary.com/) - used for images for the site.
-   [Elephant SQL](https://www.elephantsql.com/) – deployed project on Heroku uses an Elephant SQL database. 
-   [Draw.io](https://drawio-app.com/) - used for the database diagram.
-   [Iconify.Design](https://iconify.design/) - Icons used for the site.
-   [LogoMaker](https://www.logomaker.com/) - For creating the Logo for the site.
-   [Favicon.io](https://favicon.io) - for making the site favicon.
-   [tinyPNG](https://tinyjpg.com/) - for image compression.
-   [Figma](https://www.figma.com/) - used for making the wireframes for the site.
-   [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - used to validate Python in Project.
-   [Accesibility Test](https://accessibilitytest.org/) - free accessibility testing tool.
-   [Dr Link Checker](https://www.drlinkcheck.com/) - used in conjunction with manual testing of links.
-   [XML- Sitempap](https://www.xml-sitemaps.com/) - used to create a sitemap for the site.
-   [Diffchecker](https://www.diffchecker.com/) - which was useful for finding coding errors in development.
-   [Temp Email Site](https://temp-mail.org/en/) - used to test emails for registering and purchasing on site.

### Django Packages

* [Gunicorn](https://gunicorn.org/) - As a server for Heroku.
* [Cloudinary](https://cloudinary.com/) - Was used to host the static files and media.
* [Dj_database_url](https://pypi.org/project/dj-database-url/) - To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/) - As an adaptor for Python and PostgreSQL databases.
* [Summernote](https://summernote.org/) - As a text editor for adding content to the site.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - To style the forms used in the site.
 
 <br>

#### [Return to Table of Contents](#toc)
----

## 9. Testing  <a name="testing"></a>

<br>

Go to the [TESTING DOCUMENT](TESTING.md)

#### [Return to Table of Contents](#toc)
----

 ## 10. Bugs and Issues  <a name="bugs"></a>

 There have been a number of issues during development. Initially there was major issues with images, both sourcing assets and resizing them so they are uniform on the site. I wanted the products to carry the brand of the site, so this meant they had to be customised within photoshop. The special offer section are different in that they have a coloured background, but the sizing is the same, so I could live with that.

 
<br>

 ### Resolved <a name="resolved"></a>

 The webhooks were problematic at times mostly in relation to the URLS for the endpoints and making sure the secret keys are in place and the endpoint is activated on the stripe dashboard. Without being able to test with the testhooks earlier it was hard to know why they are not working and how to fix them when they were not working. Again when the project is deploayed going through this procedure again and testing a seperate endpoint. I had thought I had kept the code close to the stripe code in the walkthrough project but did have an issue with the code, I had added an extra return which meant although the order was processing correctly it never triggered the success page or the confirmation email after an order was processed and needed help from tutor support to resolved the issue, which was done with a series of print statements. There was at the same time an issue with an extra blank line in the header of the confirmation_email_subject, when these issues were fixed I finally managed to get the email message confirmation printing in the terminal within gitpod and I received email confirmation with the deployed site.

 There has been an issue with the webhooks in the gitpod site, the address has changed, which means I have been having to update the webhook url at times, when it stops working I review the address, and it usually has just changed by one number, and when it is updated it works ok again, not sure if I can prevent this happening again, but am looking into it. The Heroku webhook has no such problems, so the checkout should work as normal after submission.

 I had an issue when updating the quantity selector so it works on both the desktop and mobile screens, for this I just used the fix advised during the walkthrough video, and although I updated the 3 files, it did not work, used the code diff application and found no difference, but it still did not work, so I got on to tutor support and explaied the issue, by the means of print statements, the problem was found in the script on the bag page, while updating the dollor signs to the euro signs throughout the site, when I wanted the currency to show euros instead of dollars, I had mistakenly added a euro in a query instead of the required dollor, so this had caused a 500 error, which displayed in the termnal, when this was replaced, it started to work as it was supposed to.

 <br>

 ### Unresolved <a name="unresolved"></a>

 There is an issue in regards to sizes of products at the moment you will be offered different sizes within cerain products, which you can select successfully, there is an issue with applying 2 different prices to seperate sizes of the one product, which would need to be addressed. You can have either a small or large essential oil product in some items, but currently both products will be riced the same, now I could content the smaller bottle is of a higher quality and the larger bottle is a weaker solution and this could account for the pricing, but moving forward I would add additional functionality to offer a greater range of sizes for a greater range of products with a differing range of costs.  I really didnt want to deviate too much from the existing scripts, as I felt this might have a detrimental effect on the whole buying procedure and the inclusion of the Stripe functioning, but this would be an area that would need more of a deep dive for building E-Commerce sites in the future.

 <br>

 #### [Return to Table of Contents](#toc)
----


 ## 11. Deployment <a name="deployment"></a>

 The Project used Heroku for deployment. I used GitPod for development within the project and pushed to the GitHub Repository. This in turn updated the Project in Heroku. I used DEBUG = 'DEV' in os.environ, during development and other than when testing, had it configured so that I could work both locally and could also test the deployed Project on an ongoing basis. I added all the config vars for Stripe, AWS, The Database URL, and the creds for email. I had originally has disable collectstatic and the creds for AWS but removed these when I added cloudinary.

 <br>

Github

 ### How to make a local Clone <a name="clone"></a>
1. Navigate to the main page of the repository.
2. Click the green Code Button at top right of the repository.
3. Copy the url for the repository.
4. Open Git Bash and Change the current working directory to where you want the cloned directory.
5. Type git clone, and then paste the URL you previously copied using $ git clone. 
6. Pressing enter will then create your clone.  

<br/>  


### How to fork a GitHub Repository <a name="fork"></a>
1. Log into GitHub and go to the required Repository.
2. The Fork button is found at the top right corner of the page.
3. When you click this button you will have a copy of the repository in your own GitHub account.  


<br> 

More information is available at [https://docs.github.com/en](https://docs.github.com/en), in regards to GitHub and is a great reference point for all GitHub queries.

<br>

Code Institute

 ### Student Template <a name="studenttemplate"></a>
 This Template has been provided by the Code Institute and includes a number of tools to make life easier and has been used within this present site.    

<br/>

### Django Framework    <a name="djangoframework"></a>

I used the Resources and Lessons within the Building an E-Commerce Module to get familiar with the concepts involved in building an Ecommerce site. In particular I did the walkthroughs for 'Boutique Ado' and I covered the E-Commerce Application types, Introduction to Search Engine Optimization and Web Marketing Modules. I also referred back to my previous project and the 'I think therefore I blog' walkthrough. I also referred to the Django documentation for the occasional query.

<br>

Heroku

<br>

### Deploying to Heroku <a name="heroku"></a>
- After registering on the Heroku site, you can see the dashboard. You can select 'New' and then click 'Create new app'. You need to pick a unique name for your app, it will let you know if it is  to available to use.
- Select your region and create your app.
- Go to the settings tab and scroll until you find the config vars section and pick 'Reveal config vars',
in this case I added 'PORT' into the key field and added '8000' into the value field and click 'add'.
- If you have credentials, you must create another config vars called 'CREDS' and you would paste the JSON into the value field.
- You have to to the builldpacks section and click 'add buildpack'.
- In this case I added 'Python' and saved changes.
- Next you go to the Deploy tab and you select 'github' and confirm connection to your GitHub Account.
- You search for your project repository and click to 'connect'.
- Under the deploy options, you can chose automatic deploys, this allow you to automatically deploy each
time you push to your Repository or you can manually deploy which is the option I opted for.
- To deploy, you would choose what branch you want to deploy and click on 'Deploy Branch'.
- It takes a little time to build your app but when it is ready you can open your app by using the link provided.

<br>

### Changes in Heroku  <a name="herokuchanges"></a>

 Because of the changes in Heroku I used Eco Dynos and used ElephantSQL instead of the postgres database which is offered by Heroku. To ensure this was done successfully, I followed the same procedure as I had used in the prior project and referred to the following documents.

[Sign up for ElephantSQL](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up)
  
[Migrating Databases](https://code-institute-students.github.io/deployment-docs/80-migrating-databases-for-heroku/)
 
[Changing Dynos](https://code-institute-students.github.io/deployment-docs/01-heroku-signup/heroku-03-converting-dynos) 

<br>

### Final Deployment 

- When development is complete change the debug setting to: `DEBUG = False` in settings.py
-  In this project the summernote editor was used so for this to work in Heroku, you needed to add: `X_FRAME_OPTIONS = SAMEORIGIN ` to Settings.py.
- In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`, when I was using AWS, I used 2 different settings for gitpod and for the deployed site, to ensure costs were kept low, but nearer the end of the project when I was not using AWS, I did not worry as much about deploying.
- I had automatic deployment chosen originally, but changed this to manual deployment, as I deployed less in this project to keep costs low on AWS.

<br>

#### [Return to Table of Contents](#toc)
----

 ## Credits <a name="credits"></a>

 All images on the site were sourced in Pexels, the initial template for the essential oil and massage oil bottles were sourced in freepics. These templates were used in photoshop in combination with a brand created with [LogoMaker](https://www.logomaker.com/) to create customised images with the essenchelle brand, to add authenticity to the website. The Doterra essential oil images were found on the Pexel's site, but they were referenced in the product description.

 The logo and Favicon were built with the online tools: [LogoMaker](https://www.logomaker.com/) and 
 [Favicon.io](https://favicon.io/)

 he Project began with the basic code used in the 'Boutique Ado' walkthrough Project, but was modified according to my own needs within the Project. As the Project developed, I sought out various Tutorials and consulted documentation for Django and Stripe.

 I also used the following online resources:

- [Code Institute](https://codeinstitute.net/ie/)
- [Slack](https://slack.com/intl/en-ie/) 
- [Stack OverFlow](https://stackoverflow.com)
- [YouTube](https://www.youtube.com/)
- [Card Zoom Hover Effect in cards video on YouTube](https://www.youtube.com/watch?v=KAHjf1Xj0SU)
- [W3Schools.com columns tutorial](https://www.w3schools.com/howto/howto_css_three_columns.asp)
- [Ordinary Coders: Bootstrap Card Hover Effects](https://ordinarycoders.com/blog/article/codepen-bootstrap-card-hovers)
- [Used to test different cards for payment](https://blog.devgenius.io/what-test-cards-can-i-use-to-test-stripe-integration-1252f46b050f)
- [Animated Collapsibles for FAQ sections](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_collapsible_animate) - used for collapsible sections in the FAQ Page

<br>

#### [Return to Table of Contents](#toc)
----
 ## Acknowledgements <a name="acknowledgements"></a>
My link to the external site on the blog page with great information on using Essential Oils 
 [everydayhealth.com](https://www.everydayhealth.com/wellness/what-are-essential-oils-a-complete-guide-on-aromatherapy-and-its-potential-health-benefits/)

Everyone in Code Institute who contributed to my Projects, in particular Ed from Tutor Support, who shared his vast knowledge with me, but also every other Tutor who helped me along the way.

Thank you to my Mentor Brian Macharia for all your help and guidance for all my Projects.
<br>

 #### [Return to Table of Contents](#toc) 
----

## Author Info

Michelle Hickey, Full Stack Software Developer.
- [Linkedin](https://www.linkedin.com/in/michellehickey1/)
- [Portfolio](https://michellehickey.crevado.com/)
- [UX Portfolio](https://www.behance.net/michellehickey2)


[Back to the Top](#table-of-contents)