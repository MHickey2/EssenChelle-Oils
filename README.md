# EssenChelle Oils: Milestone 5 Project


<p align ="center">      
   <img src="assets/readme/images/amiresponsive.png"  alt="AmIResponsive" />       
</p>
<br/>  

 
# Introduction <a name="introduction"></a>

The EssenChelle Oils site is my 5th Project for the Code Institute and it is a full stack E-commerce site using the Django Framework, it includes Python, JavaScript, CSS and Bootstrap5. It utilizes Stripe payments. It has user authentication and Full CRUD functionality for the products and Blogs for the Superuser. The website deals with the sale of essential oils and associated products. The website would appeal to people who use or want to know more about Essential Oils and are interested in buying these products. This website has been built for educational purposes and the payment transactions are purely for demonstration only. If you want to test the payment functionality, you can use: 

<p align ="center"> 
<mark>Card number: 4242 4242 4242 4242  Exp: Future Date i.e. 05/25 and CVC can be any 3 numbers.</mark>
</p>

<br/>

[Visit the EssenChelle Oils Site](https://essenchelle-oils.herokuapp.com/) 

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
      - [Return to Table of Contents](#return-to-table-of-contents-1)
  - [3. Agile Methodology](#3-agile-methodology)
      - [Return to Table of Contents](#return-to-table-of-contents-2)
  - [4. Design  ](#4-design--)
    - [1. Colour  Scheme  ](#1-colour--scheme--)
    - [2. Typography    ](#2-typography----)
    - [3. Imagery    ](#3-imagery----)
    - [4. Website Structure    ](#4-website-structure----)
    - [5. Wireframes    ](#5-wireframes----)
      - [Return to Table of Contents](#return-to-table-of-contents-3)
  - [5. Data Model    ](#5-data-model----)
      - [Return to Table of Contents](#return-to-table-of-contents-4)
  - [6. Web Marketing](#6-web-marketing)
    - [1. E-Commerce Application Type](#1-e-commerce-application-type)
    - [2. Marketing Strategy](#2-marketing-strategy)
      - [**Facebook Page**](#facebook-page)
    - [3. Search Engine Optimization(SEO)](#3-search-engine-optimizationseo)
    - [4. XML Sitemap](#4-xml-sitemap)
    - [5. Robots.Txt File](#5-robotstxt-file)
      - [Return to Table of Contents](#return-to-table-of-contents-5)
  - [7. Features  ](#7-features--)
    - [1. Home Page   ](#1-home-page---)
    - [2. Products Page     ](#2-products-page-----)
    - [3. EssenChelle Products Page     ](#3-essenchelle-products-page-----)
    - [4. Product Details Page     ](#4-product-details-page-----)
    - [5. About Us Page     ](#5-about-us-page-----)
    - [6. Our Products Page     ](#6-our-products-page-----)
    - [7. Blog Page     ](#7-blog-page-----)
    - [8. Blog Details Page     ](#8-blog-details-page-----)
    - [9. Contact Page     ](#9-contact-page-----)
    - [10. Profile Page    ](#10-profile-page----)
    - [11. Product Favourites Page     ](#11-product-favourites-page-----)
    - [12. FAQ Page     ](#12-faq-page-----)
    - [13. Privacy Policy Page    ](#13-privacy-policy-page----)
    - [14. Copyright Page    ](#14-copyright-page----)
    - [15. Special Offers Page   ](#15-special-offers-page---)
    - [16. Shopping Bag Page     ](#16-shopping-bag-page-----)
    - [17. Checkout Page     ](#17-checkout-page-----)
    - [18. Checkout Success Page     ](#18-checkout-success-page-----)
  - [The following pages are also available, but only to the superuser on the site.](#the-following-pages-are-also-available-but-only-to-the-superuser-on-the-site)
    - [19. Add Product Page     ](#19-add-product-page-----)
    - [20. Edit Product Page     ](#20-edit-product-page-----)
    - [21. Delete Product Page     ](#21-delete-product-page-----)
    - [22. Add Blog Page     ](#22-add-blog-page-----)
    - [23. Edit Blog Page     ](#23-edit-blog-page-----)
    - [24. Delete Blog Page     ](#24-delete-blog-page-----)
    - [25. Signup Page   ](#25-signup-page---)
    - [26. Login Page   ](#26-login-page---)
    - [27. Logout Page   ](#27-logout-page---)
    - [28. Custom Error Pages  ](#28-custom-error-pages--)
    - [29. Admin Panel  ](#29-admin-panel--)
    - [30. Security Measures  ](#30-security-measures--)
      - [Return to Table of Contents](#return-to-table-of-contents-6)
  - [8. Future Implementation  ](#8-future-implementation--)
      - [Return to Table of Contents](#return-to-table-of-contents-7)
  - [9. Tools and Technology  ](#9-tools-and-technology--)
    - [Language Used:](#language-used)
    - [Technology Used:](#technology-used)
    - [Django Packages](#django-packages)
      - [Return to Table of Contents](#return-to-table-of-contents-8)
  - [10. Testing  ](#10-testing--)
      - [Return to Table of Contents](#return-to-table-of-contents-9)
  - [11. Bugs and Issues  ](#11-bugs-and-issues--)
    - [Resolved ](#resolved-)
    - [Unresolved ](#unresolved-)
      - [Return to Table of Contents](#return-to-table-of-contents-10)
  - [12. Deployment ](#12-deployment-)
    - [How to make a local Clone ](#how-to-make-a-local-clone-)
    - [How to fork a GitHub Repository ](#how-to-fork-a-github-repository-)
    - [Student Template ](#student-template-)
    - [Django Framework    ](#django-framework----)
    - [Deploying to Heroku ](#deploying-to-heroku-)
    - [Changes in Heroku  ](#changes-in-heroku--)
    - [Cloudinary for Images](#cloudinary-for-images)
    - [Add Stripe keys to Heroku](#add-stripe-keys-to-heroku)
    - [Final Deployment](#final-deployment)
      - [Return to Table of Contents](#return-to-table-of-contents-11)
  - [Credits ](#credits-)
      - [Return to Table of Contents](#return-to-table-of-contents-12)
  - [Acknowledgements ](#acknowledgements-)
      - [Return to Table of Contents](#return-to-table-of-contents-13)
  - [Author Info](#author-info)

----

## 1. UX Strategy <a name="uxstrategy"></a>
----

<br/> 

### 1. The Business Goals of the Website: <a name="businessgoals"></a>      

- The website is an E-commerce site so one goal would be be to achieve a commercial success from sales within the site.
- Expand the customer base for the EssenChelle Oil company.
- Promote repeat customers and ensure the present customers have a good user experience.
- Use Social Media to increase awareness of the Site and strategically plan future growth for the Brand.
- High customer satisfaction for the site users.
- Content and the service provided ensures retention of customers.
- Effective use of discounts and value offers. 
- Create content that will engage the users and encourage them to return for more.
- Make the shopping experience easy to manage for the Shopper.
- Attract visitors and convert them into customers.
- Encourage customers and visitors to communicate with the Business and respond effectively to their requests.
- Use customer feedback to address any perceived shortcomings and use the knowledge gained to possibly expand the current range of products.
  
  <br/> 

### 2. The Target Customer: <a name="targetcustomer"></a>    

- Anyone with an interest in essential oils and their byproducts.
    
- Anyone who wishes to buy EssenChelle Oil products.  
- Anyone who has interest in joining the EssenChelle Oil community and wants to learn more about our range of products. 
- Anyone who wants to experience essential oils in their home and are looking for essential oil burners.  
- Anyone who wants to offer massages or use massage oils for personal use and are looking for specific blends for therapeutic uses.
- Anyone who would want to avail of special offers on products related to essential oils.

 <br/>  

### 3. Site User Profile

The user is really anyone who has an interest in holistic health. They either have had some experience with essential oils or are new to Essential Oils and want to learn more about them and how to integrate them into their lives. They may want to buy products from the site or read blogs that have a focus on the benefits and the uses for featured oils. They may also be interested in special offers related to essential oils and would like to browse the site for the current deals within the site.

<br/>

### 4.  Site Goals

- The theme of the site is easy to understand and it is easy to navigate through the site content easily.
  
- The user will be able to use the search facility to find specific products by category/word search.
- The user will be able to buy all Products available on the site.
- The user will be able to maintain a profile on the site and can update their Profile details easily.
- The user will be able to avail of discount and offers within the site.
- The user will be able to view blogs and can add comments for individual blogs.
- The user can see full details for individual products and if logged in they can leave reviews.
- The user can contact the site owner with queries and suggestions.
- The user when logged in can choose their favourite products and these can be stored within their favourite products page.
- The user will be able to sign up for a regular newsletter. 

<br>

 #### [Return to Table of Contents](#toc)

----

## 2. User Stories  <a name="userstories"></a>

<br>

###  As a website User I can...<a name="websiteuser"></a>

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

###  As a logged in User I can... <a name="loggedinuser"></a> 

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

### As a website superuser, I can …..    <a name="superuser"></a>

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
[As a staff member I can log in so that I can access the relevant features of the site #1](https://github.com/MHickey2/EssenChelle-Oils/issues/1)


User Story Testing can be found in the [TESING.md Document](TESTING.md)  

  <br/>   

 #### [Return to Table of Contents](#toc)

## 3. Agile Methodology

The project was developed using Agile Methodology by using the GitHub Projects functionality within the GitHub Repository. Each issue has a defined acceptance criteria and includes tasks needed to accomplish the goals. The 29 issues can be found [Here](https://github.com/MHickey2/EssenChelle-Oils/issues) and this is the link for the [Essential Oils Project Board](https://github.com/users/MHickey2/projects/2)

<br/> 

#### [Return to Table of Contents](#toc)  
----

## 4. Design  <a name="design"></a> 

<br/>

### 1. Colour  Scheme  <a name="colourscheme"></a>

The colour scheme was inspired by essential oils, in particular lavender oil, so the website uses a darker shade of this colour throughout the site. The color Lavender represents holistic wellness and it is known for its tranquility and calming effects. Lavender Oil is also one of the most popular oils and very versatile so it made sense to capitalize on it's popularity by using a colour most holistic people would be familiar with. The background colour for the site is white and this provides a good contrast for the content. Headings, borders and the footer are mostly purple. In this project I wanted to only have a subtle use of colour, so that there would be little distraction to the user, when making their purchases on the site. The following image shows the most prominent colours used in the site, this was made with [Colour Combos](https://www.colorcombos.com/):

<br>
<p align ="center">      
   <img src="assets/readme/images/colourcombo.png"  alt="Colour Combo" />        
</p>
<p align ="center">      
   <mark style="background-color:white">colours: #800080, #E83E86, #9037E4, #E9AFE9, #2D023D</mark>        
</p>

<br/> 

The branding is an aspect of the overall design and it used in conjunction with the marketing strategy. It consists of the logo, the colour scheme, the font and the buttons, and this would be used in social media, packaging, brochures, the stationary and the advertising materials. The brand(logo) has been included in the EssenChelle range of Essential and Massage Oils. I took the blank bottle templates and added the logo and identifying information to all the bottles featured in the EssenChelle Oil range. This is a simple mood board for EssenChelle Oils branding, highlighting the main characterics featured:

<br>

<p align ="center">      
     <img src="assets/readme/images/branding.png" width="550" alt="Branding" />     
</p>

<br/> 

### 2. Typography    <a name="typography"></a>

Google Fonts were used within the website. The 'Roboto' font is the main font used for the whole project. Sans serif is the fallback font in case the other font is not available. See below for examples of fonts in use on the site. The font color is #313131, which is a good font to help counter eye strain, and I usually try to include it in all of my projects. THe following are details for this font:

<br>
<p align ="center">      
   <img src="assets/readme/images/313131.png"  width="350" alt="general font colour for site" />        
</p>

<br>

The main title for the site, the navigation items and the headings for the site use the Courgette Font, which is a google font. It is a medium-contrast, brushy, italic-script typeface, which has been made for the web. It adds a decorative flair but is also very legible on a screen. The following are examples of the courgettefont in use:

<br>
<p align ="center">      
   <img src="assets/readme/images/courgettefont.png" width="400" alt="courgette font" />        
</p>

<br>

### 3. Imagery    <a name="imagery"></a>

The Logo was created with [LogoMaker](https://www.logomaker.com/), I used a health and beauty related theme for the logo, as essential oils are synonymous with health and beauty benefits. The logo features a beautiful woman's face which has the EssenChelle Oil Title prominent in its design. The colours included fit the colours displayed in the website, to ensure brand conformity across the site.

The images in the site focuses on essential oils and related products, the images were sourced from the [Pexels site](https://www.pexels.com/) and supplement the site's overall theme. The images for the site are hosted in [Cloudinary](https://cloudinary.com/). I had used AWS for a while but was not comfortable using AWS, as it was unpredictable in regards to pricing, and I chose to revert to cloudinary as I trusted this platform, from my previous project. I did have the experience of setting up the Bucket in S3 and uploading the images and having them show on the site, so I can say I have used the platform, and I may apply what I have learned in future projects going forward. 

There are also images sporadically placed throughout the site, There is a background image of a massage which highlights the nature of the site on the index page, the product was initially a template with blank packaging detail, so I used photoshop to apply the EssenChelle brand image for the different products in the essential and massage oil range. The aromatherapy burners were sourced on a shopping site platorm, as they did not have to have the essenchelle branding. The Items in the special offer section were also sourced in the Pexels site. The following image show a sample of the images contained on the site:

<br>

<p align="center">
  <img src="assets/readme/images/collage.png" width="600" alt="Images for Site"/>
</p>

<br/>

There are also various icons used within the site, the icons were sourced at [Iconify.Design](https://iconify.design/) and font-awesome in some cases, and they were used as a graphical representation for pertinent information on the site, they were used in conjunction with identifying icons such as the account and shopping icons as well as the social media icons within the footer, and their use was a subtle way to incorporate imagery on a limited scale, examples can be found in the image below:

<br>

<p align ="center">      
     <img src="assets/readme/images/icons.png"  width="400" alt="icons for Site" />    
</p>

<br/>

I also created the favicon for the site with [Favicon.io](https://favicon.io). These were just smaller versions of the logo in various sizes, they are another form of branding for your website. Its main purpose is to help visitors locate your page easier when they have multiple tabs open. The following image shows a favicon for an android.

<br>

<p align ="center">      
     <img src="assets/readme/images/android.png" width="100px" alt="Favicon for Site" />    
</p>

<br/>

### 4. Website Structure    <a name="structure"></a>

The website follows the standard website structure. The Logo and the website name are on the left hand side, and the naigation to the right, on the top of all pages. Within the Account Nav top Link the user can either Signup or login to the site. When the user logs in they can see the Profile link, The favourite products and the logout button. If they are a superuser they can also see product and blog management options. The Shopping Bag Link takes the User to the Shopping Bag Page. When the website is on smaller screens, there is a hamburger meu, with the navigation items in a dropdown menu. The footer element is also available on all pages, with site information, contact details, social media icons and the newsletter sign up form.

The website consists of the following Pages:
 - The Home Page, with a hero image and a button connecting to the Shop. It has a search bar and links to all areas in the site. There is is also a profile and shopping bag link.
 - The Products page is available in a number of formations, it can be sorted by pricing, ratings and category and you can see all products from all categories.
 - The Essenchelle Products can be configured to show the different categories within the EssenChelle range of products. The products include Essential Oils, Massage Oils and Oil Burners, or you can view all categories at once.
 - The Product Details Page, shows the information for individual Products.
 - The Add Product Page, which is a form that allows the superuser to add a Product.
 - The Edit Product Page, which is a form that allows the superuser to edit a Product.
 - The Delete Product Page, which is a form that allows the superuser to delete a Product.
 - The Bag Page which shows the details of the products presently in the Bag.
 - The Checkout Page, which shows the details of their order and the user details form and the checkout submission button.
 - The Checkout Success page, which shows the order details and price and the Thank you message.
 - The About Page, which gives more information on the site 
 - The Our Products Page, with an introduction to the EssenChelle Products by category and it includes customer testimonials who have bought products on the site.
 - The Blog Page with a spotlight on products, it highlights individual products and the blogs can only be
  added by the superuser.
 - The Blog Detail Page, that shows the information for individual Blogs.
 - The Add Blog Page, which is a form that allows the superser to add a Blog.
 - The Edit Blog Page, which is a form that allows the superuser to edit an existing Blog.
 - The Delete Blog Page, which is a form that allows the superuser to delete a Blog.
 - The Profile Page, which contains profile information and the product history for the logged in user.
 - The User Product Favourites Page, which shows the user's favourite products.
 - The Sign Up Page, consists of a form where a new user can register for the site.
 - The Login Page, consists of a form where the user can login to the site.
 - The logout Page, consists of a form where the user can logout of the site.
 - There are also custom error pages for errors 403,404,405 and 500.
 - The Product Favourites page which shows the logged in user all their favourite products.
 - The Special Offer pages can be configured to show the different categories within the Special Offers. The special offers include new arrivals, deals and clearance items or you can view all categories at once.
 - The Contact Us page which has a contact form, a location map and details.
 - There is a FAQ page with answers to questions Customers may have about the site.
 - There is a Privacy Policy Page which can be accessed in the footer.
 - There is a Copyright Page with copyright information which can be accesed in the footer.

<br/>

### 5. Wireframes    <a name="wireframes"></a>

The Wireframes for the site were created in Figma, I concentrated on the standard websize and the mobile size. The mid-level sizes were generally in keeping with the main websize but just on a smaller scale. There have been modifications and changes since the initial wireframes design. Some of the pages introduced at the later stages of development may not be included, as there had been no plan to include them in the project initially. The Wireframes can be found below:

<details><summary>Figma Wireframes</summary>

<br>

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


## 5. Data Model    <a name="datamodel"></a>

<br>

<details>
  <summary>Database ER Diagram</summary>

<br>

<p align ="center">      
     <img src="assets/readme/images/database.png"  alt="Database ER diagram" />    
</p>
</details>

<br/> 

 #### [Return to Table of Contents](#toc)
----

<br>

## 6. Web Marketing

<br>

### 1. E-Commerce Application Type
EssenChelle Oil is a B2C E-Commerce Application. It deals with selling directly to it's customer. There is a great emphasis in promoting a good user experience for the customer. The aim is to retain the current customers and at the same time grow the customer base by organic means. Because it is online it can reach a wide audience and is not dependent on location. Overhead and operational costs are reduced because there is no physical premises. The Direct to consumer business model has the advantage of being able to charge lower prices, which is a great incentive for customers. The business can run 24 hours a day and this allows flexibility for the business owner as they are not confined to normal business hours.

<br>

### 2. Marketing Strategy
Essenchelle Oils is a fledgling company, with a limited budget for marketing, so decisions need to be cost effective and practical. That being said the company has come up with a range of marketing strategies, ie content marketing, utilizing social media platforms, digital promotions, and highlighting events that will promote the products firsthand. The goal is is to increase project sales, create a following online and concentrate on building brand awareness.

<br>

Social Media will play a big part in the marketing strategy, research into the different platforms has highligted ways that can be cost effective and easy to implement. Facebook is a great way to build up followers and share information with a wide number of customers. A Facebook page was created to share pertinent information with the users, and will be used to promote the latest deals, that should entice new customers to the EssenChelle site. The image below shows the Facebook page, it is active currently but not sure if it will remain so, so have included a screencapture below and here is the live link: [EssenChelle Oils](https://www.facebook.com/profile.php?id=100090771283240)

#### **Facebook Page**

<br>

<p align="center">
  <img src="assets/readme/images/facebookpage.jpg" width="800" alt="EssenChelle Facebook Page" />
</p>

<br>

Content Marketing: the process of publishing written and visual material online with the purpose of attracting more leads to your business is the essence of content marketing. In this case the website has a blog section which highlighs the products in the EssenChelle range. The main focus is on showing the customer the benefits of specific oils to the customers, why they should buy them and how they can use them. This should drive more sales and funnel the user to the products page. Selected blogs can also be shared on various social media channels, furthering the reach of the created content.

<br>

<p align="center">
  <img src="assets/readme/images/blogposts.png" width="500" alt="Blog Section" />
</p>

<br>

Google Ads : This option is out of reach at the moment, as the budget is small, but with enough experience and analysis I hope to be able to plan a campaign in the future that will be cost effective and will pay long lasting dividents.

<br>

Events: There is a large industry dealing with essential oils and aromatherapy in Ireland, and indeed worldwide. In this regard you can tap into existing events that are used to promote the industry and that are very accessible to the public. One of the largest event, occurs yearly in the RDS in the Body Mind Spirit fair where a range of companies, mostly smaller companies have the opportunity to highlight their products to a very involved and motivated audience. You have the opporuity to mingle with and sell directly to the public and grow a valuable network which will be a great boost for future business. This would play a major part in growing the brand and linking with a potentially large customer base. But this occurs later in the year, and meantime smaller events, in this vein are held in venues throughtout the country and would be an excellent way to connect with the right clientele. As well as growing a customer base it would be good to network with other business's and there may be some mutual gains in forging such alliances. The image below shows the Expo details:

<br>

<p align="center">
  <img src="assets/readme/images/bodymindspirit.png" width="900" alt="Body Mind Spirit Expo" />
</p>

<br>

The website itself offers users the chance to sign up for a regular newsletter. This measure allows you communicate directly with your prospects and customers in a personalized way by serving valuable content and relevant promotions straight to their inboxes. This newsletter would be a good way to promote new products, provide articles highlighting the benefits of using certain products, offer special offers and highlight new arrival products. This will be a great way to grow the Essenchelle community and keep the customers in the loop. The newsletter functionality utilizes mailchimp, this service will help keep track of users. Mailchimp offers a number of tools that will be explored further as the company develops. You can visit the mailchimp dashboard to find user emails that have been added to your subsciber list. The newsletter itself would include the latest articles, special promotional offers and promotional deals. Sending a newsletter on a regular basis will build brand awareness and should lead to more purchases on the site.

<br>

<p align="center">
  <img src="assets/readme/images/newsletter.png"  width="300" alt="Mailchimp Newsletter" />
</p>

<br>

<p align="center">
  <img src="assets/readme/images/subscribers.png" alt="subscribers list" />
</p>

<br>


###  3. Search Engine Optimization(SEO)
SEO research will help drive people to our site more efficiently. Inititally finding the right keywords will help send our site further up in the rankings. Finding the right words involved looking at present sites, previous research finding and analysing which words were suggested when searching for essential oils and aromatherapy in particular in google searches. I used [wordtracker.com](https://www.wordtracker.com/) and various other free tools to find keywords, the factors that determined the ones chosen include search volume, relevance and conversion value. I then picked the top words and phrases and integrated them into the site via meta-tags or by ensuring they were included in headings, image names and content. It was important not to overdo the use of these words as this would have been counterproductive to the end goal. The following image shows a sample of the research findings and that were used to devise the keywords used in the site:

<br>

<p align="center">
  <img src="assets/readme/images/googlekeywords.png" width="650" alt="Keyword Search" />
</p>

<br>

<p align="center">
  <img src="assets/readme/images/ukbusinessdirectory.png" width="400" alt="Keyword Search2" />
</p>

<br>

There were also links included for internal pages and a link to an external site of good standing that are in a similar industry. I have an external link in the blog page in the sidebar, the site is not information heavy so I linked to a reputable site, that had more detailed information on safety precautions. The site used can be found [here](https://www.everydayhealth.com/wellness/what-are-essential-oils-a-complete-guide-on-aromatherapy-and-its-potential-health-benefits/). The following is a heading from the site used: 

<br>

<p align="center">
  <img src="assets/readme/images/externallinksite.png"  width="600" alt="External Site on Health and Benefits" />
</p>

<br>

### 4. XML Sitemap
 I've added an XML sitemap file to the main root directory, this is used to help search engines understand your website structure. It also enables Google to crawl every important page of your website. Sitemaps in general enhance the ranking of your website in search engine results, thus in turn will boost your SEO efforts. Besides being a requirement for the project, it was a good idea to add a sitemap when your site is new and has few external links. Googlebot and other web crawlers crawl the web by following links from one page to another. As a result, Googlebot might not discover your pages if no other sites links to your site. This page was generated using [xml-sitemaps](https://www.xml-sitemaps.com/)

<br>

### 5. Robots.Txt File
A robots.txt file has also added to allow the search engine crawlers to know which URLs the crawler can access on this site, this was used to avoid overloading the site with requests.

<br>

#### [Return to Table of Contents](#toc)
----

## 7. Features  <a name="features"></a>

There are features common to all pages in the site. These include:

- The Logo and Site Title:
  
The logo was the first asset I created in Logo maker, it depicts a simple female face image using the main colours displayed in the site. The Logo includes the name of the site, so the logo is synonomous with the brand. Using the name in the logo meant I had a readymade image for the packaging of the products in the range. The image relates to the area of health and Beauty, as essential oils are strongly related to the promotion of health and beauty benefits. The below image shows the logo image:

<br>

<p align ="center">      
     <img src="assets/readme/images/essenchelle-logo.png" width="200" alt="Logo with Title" />    
</p>

<br/> 

There is a search bar, where the user can search for products by name or keyword. There is an Account Icon, which contains a dropdown menu:

Account Icon - Register, Log In. (Before Log in or registering)
Account Icon - Add a Product, Add a Blog, My Profile, Product Favourites, Log Out. (If logged in and Superuser)
Account Icon - My Profile, Product Favourites, Log Out (If logged in and ordinary User)

Shopping Bag Icon - Takes you to the Shopping Bag Page.

- The Navigation Bar:

The navigation consists of the following options: All Products, EssenChelle Products, Our Story, Special Offers and Contact. Each of these Nav items have dropdown menus:

All Products - By Price, By Rating, By Category and All Products.
EssenChelle Products - Essential Oils, Massage Oils, Oil Burners and All Products.
Our Story - About Us, Our Products and Blog and FAQ.
Special Offers - New Arrivals, Deals, Clearance and All Specials.
Contact - Contact Us.

  <br>

<p align ="center">      
     <img src="assets/readme/images/navigation.png" width="800px" alt="Navbar options" />    
</p>

<br/> 

On smaller screens, there is a hamburger menu where the navigation items appear in a collapsible dropdown menu. The image below shows the collapsible menu for smaller screens:

<br>

<p align ="center">      
     <img src="assets/readme/images/mobile navbar.png"  width="300"  alt="navbar mobile" />    
</p>

<br/> 

- The Footer:
The Footer contains a blurb on the site, some contact details and social media icons, also the copyright information, the privacy policy and the faq for the EssenChelle Oils site. The footer also includes a newsletter sign up form provided by mailchimp.

 <br>

<p align ="center">      
     <img src="assets/readme/images/footer.png"  width="600px" alt="footer" />    
</p>

<br>

### 1. Home Page   <a name="homepage"></a>

The home page has a Hero image depicting a massage session, which is a strong indicator of the type of products available within the site. There is some textual content describing the site's purpose. There is also a call to action button(shop button), that will take the user directly to the product page, so that the user can begin shopping right away. 
  
<br>

<p align ="center">      
     <img src="assets/readme/images/homepage.png" width="500" alt="Home Page" />    
</p>

<br/> 

### 2. Products Page     <a name="productpage"></a>

The products page shows the the full collection within the EssenChelle range including the special offers. These products can be arranged according to specified criteria, such as by price, by rating or by category. The number of all items available is shown to the user and the user can further sort the products by means of the sorting bar on the right of the screen. Each of the products shows the title, an image, the price, the category and the star rating and it will also show users if there are any associated reviews for the product. The image below shows the full product range available in the products page.

<br>

<p align ="center">      
     <img src="assets/readme/images/productsPage.png"  width="500"  alt="products page" />    
</p>

<br/> 

### 3. EssenChelle Products Page     <a name="essenchelleproductpage"></a>

This Page shows products in the category of Essential, Massage and Oil Burners. You can select to see products within just one category by choosing the option in the dropdown menu or by selecting the relevant badges at the top of the page. You can view the number of products and there is a facility for sorting at the top of the page. The options for sorting includes price, rating, name and category.

<br>

<p align ="center">      
     <img src="assets/readme/images/essenchelleprod.png" width="500" alt="Essenchelle product Page" />    
</p>

<br>

### 4. Product Details Page     <a name="productdetailspage"></a>
The Page shows the full details of an individual product including the image. There is a review form, where a product user who is logged in can leave a review for a product. This review will need to be approved by the superuser before it is published to the review section. The review section shows existing reviews. There is an add to favourites button to the right of the product title, when this is clicked, the product is saved to the user's favourites. Any product which has been selected as a favourite, can be viewed in the product favourites page (can be found in the dropdown menu within the account icon when the user is logged in).

<br>

<p align ="center">      
     <img src="assets/readme/images/proddetailpage.jpg"  width="500"  alt="product detail page" />    
</p>

<br/>

### 5. About Us Page     <a name="aboutpage"></a>

The About Us Page provides the background information on the EssenChelle Oil Company, It also features a carousel with information on the different categories of products on offer within the site. This feature is hidden in smaller screens.

<br>

<p align ="center">      
     <img src="assets/readme/images/aboutpage.jpg"  width="500"  alt="about page" />    
</p>

<br/> 

### 6. Our Products Page     <a name="ourproductpage"></a>

The our products page shows more in-depth information on each category in the product range. It also provides customer testimonials on why a potential customer should choose a product in the EssenChelle Product Range. This also plays a part in the marketing strategy, as it uses client recommendations to promote the brand. (this adds a personal touch and helps user relate to existing customers, it helps the user to visualise how buying a product will have a positive impact on their own lives).

<br>

<p align ="center">      
     <img src="assets/readme/images/ourprod.jpg"  width="500"  alt="our products page" />    
</p>

<br/> 

### 7. Blog Page     <a name="blogpage"></a>

The Blog Page shows a collection of blogs with a spotlight on products being sold on the site. This would hopefully encourage readers to view and potentially buy products from the products page (using the content to drive sales, which is a part of the marketing strategy). The sidebar gives a brief introduction to the blogs. There is a link within the sidebar to an accredited site with more comprehensive information on individual essential oils. It also shows the titles for the latest available Blogs.

<br>

<p align ="center">      
     <img src="assets/readme/images/blogpage.jpg"  width="500"  alt="blog page" />    
</p>

<br/>

### 8. Blog Details Page     <a name="blogdetailspage"></a>
The Blog Detail page shows the full blog which has information pertaining to selected products on the site. It will either concentrate on an individual oil(The Benefits of Lavender oil), or a selection of products(Our Top 5 best Massage Oils), it may also include internal links to the highligted products within the site . For logged in users there is a comment form, for users to leave a comment. When a comment is added, it need's to be approved by a superuser before it will be published in the comment section. There is a comment section for existing comments.

<br>

<p align ="center">      
     <img src="assets/readme/images/blogdetail.jpg"  width="500"  alt="blog details page" />    
</p>

<br/>


### 9. Contact Page     <a name="contactpage"></a>
 A contact form is included so that the user can send a message to the company. This will aid communication between the user and the EssenChelle Oil Co. this could include queries on the sales process, more information on specific properties of products or questions in relation to delivery issues. When a message is sent a confirmation email will be sent to the message sender. You do not have to be a logged in user to make an enquiry, as an unregistered user who wishes to send a message could be a potential customer and it would be important to ensure the communication lines are open for everyone. The contact page has a map showing the location of the Company(which is a fictional address. Although it is an ecommerce business, this map allows customers to know their proximity to the base of operations, and it may be useful later on for special events organised by the company ie market research activities) It will also help customers to determine the cost of delivery, as some of the cost will be effected by the distance for delivery. Although contact details can be found in the footer, it is also included on the contact page for convenience sake.

<br>

<p align ="center">      
     <img src="assets/readme/images/contactpage.jpg"  width="500"  alt="contact page" />    
</p>

<br/>

### 10. Profile Page    <a name="profile page"></a>
The Profile page contains a form to update the customer's default delivery information and it will also show the user's order history. It also allows the user to enter their credit/debit card details and there is a checkbox where the user can tick if they want this information to be saved on the site. The user needs to be logged in in order to save this information to their account.
<br>

<p align ="center">      
     <img src="assets/readme/images/myprofile.jpg"  width="500"  alt="profile page" />    
</p>

<br/>

### 11. Product Favourites Page     <a name="favouritespage"></a>
The Page shows a collection of the user's product favourites. The user can add their favourites by using the 'add to favourites button' above the product in the product details page. The details and image of each product are displayed. There is a remove button below each product and when this is selected the product will be removed from the user's favourites.

<br>

<p align ="center">      
     <img src="assets/readme/images/productfavourites.jpg"  width="500"  alt="product favourites page" />    
</p>

<br/>

### 12. FAQ Page     <a name="faqpage"></a>
The page gives a brief introduction to the content of the page and the rest of the information is broken down into 3 main sections: Ordering, Dispatch and Delivery and Returns and Refunds. Each section shows frequently asked questions and answers. It can be accessed in the dropdown menu for the our story link, but also can be accessed by a link in the footer. I purposely did this as I wanted the user find the information easily within the nav, but adding it into the footer seemed to be appropriate as well as the company information documents are grouped together in a logical sequence under the blurb on the company.

<br>

<p align ="center">      
     <img src="assets/readme/images/faq.jpg"  width="500"  alt="product favourites page" />    
</p>

<br/>

### 13. Privacy Policy Page    <a name="privacypolicypage"></a>
This page shows the Privacy Policy for the EssenChelle Oil Company. The link to the page can be found in the footer section. The Privacy Policy was generated with [The Privacy Policy Generator](https://www.privacypolicygenerator.info/)

<br>

<p align ="center">      
     <img src="assets/readme/images/privacypolicy.jpg"  width="500"  alt="product favourites page" />    
</p>

<br/>

### 14. Copyright Page    <a name="copyrightpage"></a>
This page shows the copyright information for the EssenChelle Oil Company. The link to the page can be found in the footer section. When used it will open the page in a new tab. The Copyright Page was created with [EasyLegalDocs.com](https://easylegaldocs.com/templates/notices/copyright-notice/)

<br>

<p align ="center">      
     <img src="assets/readme/images/copyright.jpg"  width="500"  alt="product favourites page" />    
</p>

<br/>

### 15. Special Offers Page   <a name="specialofferspage"></a>
This Page shows products in the category of New Arrivals, Deals and Clearance Items. You can select to see products within just one category by choosing the option in the dropdown menu or by selecting the relevant badge at the top of the page. You can view the number of products and there is a facility for sorting at the top of the page. The options for sorting includes price, rating, name and category.

<br>

<p align ="center">      
     <img src="assets/readme/images/specialoffers.jpg"  width="500"  alt="special offers page" />    
</p>

<br/>

### 16. Shopping Bag Page     <a name="shoppingbagpage"></a>
The Page shows the products that the user has currently in their shopping bag. This will initially display no products, but as products are added, they will be displayed on the page. Any products displayed will show an image, the price, a quantity selector for the number of items and the total price for all products in the bag. You can update the number of items or remove an item if neccessary. If the product amount exceeds 50 there is no delivery cost, but if it is lower a delivery cost will be applied. There is a keep shopping button and this allows the user to return to shop for more products. There is also a 'Go to secure checkout button' and this will send the user to the checkout page where they can complete the purchasing process.

<br>

<p align ="center">      
     <img src="assets/readme/images/bagpage.jpg"  width="500"  alt="shopping bag page" />    
</p>

<br/>

### 17. Checkout Page     <a name="checkoutpage"></a>
The Checkout Page shows the form to complete the order and the order summary. If you have previously clicked to save your delivery information on profile, this information will be already filled in. You can adjust your bag or you can complete your order. When the user has successfully entered all their details correctly, a spinner feature will show while the purchase is being processed. In some cases a popup will be shown to allow the user to authenthicate their card. With Stripe there is added validation to ensure the card details have been entered correctly.

<br>

<p align ="center">      
     <img src="assets/readme/images/checkoutpage.jpg"  width="500"  alt="checkout page" />    
</p>

<br/>

### 18. Checkout Success Page     <a name="checkoutsuccesspage"></a>
The Page is shown to the user when their order has been processed. It contains a Thank you message and includes the order information, order details, delivery details and billing information, and there is a link to the latest deals page on the site. There is also a success message displayed(toast) advising the user that their order has been processed successfully and a confirmation email will be sent to them.

<br>

<p align ="center">      
     <img src="assets/readme/images/checkoutsuccess.jpg"  width="500"  alt="checkout success page" />    
</p>

<br/>

<p align ="center"> 
  ## The following pages are also available, but only to the superuser on the site. ##
</p>

<br>

### 19. Add Product Page     <a name="addproductpage"></a>
The Add Product page can be found in the account admin dropdown. The superuser can add a product in the frontend as well as in the admin panel. It can be accessed via the account icon or with a button at the left and bottom of the products page.(which I found more intutive to user). This page has a form where you can add product details and add a product image, if an image is not added a generic image will be applied. When the product is added the user is redirected to the products page.

<br>

<p align ="center">      
     <img src="assets/readme/images/addproduct.jpg"  width="500"  alt="add product page" />    
</p>

<br/>

### 20. Edit Product Page     <a name="editproductpage"></a>
If you are a Superuser you can find the button to edit a product below the product Title in the products page and on the product detail page again below the product Title. The Edit Product Page has a form which allows the superuser to edit product details for individual products. When the product details have been edited and the form is submitted the superuser will be redirected to the product detail page for that specific product.

<br>

<p align ="center">      
     <img src="assets/readme/images/editproduct.jpg"  width="500"  alt="edit product page" />    
</p>

<br/>

### 21. Delete Product Page     <a name="deleteproductpage"></a>
If you are a Superuser you can find the button to delete a product below the product Title in the products page and on the product detail page below again under the product Title.The Delete Product Page has a form which allows the superuser to delete individual products. If you select to delete the product you will be redirected to the products page, where the product will have been removed. 

<br>

<p align ="center">      
     <img src="assets/readme/images/deleteproduct.jpg"  width="400"  alt="delete product page" />    
</p>

<br/>

### 22. Add Blog Page     <a name="addblogpage"></a>
 The Add Blog page can be found in the account admin dropdown.The button to access the add blog page is visible on the bottom and left of the blog page, only for the superuser, I found this more accessible to use generally.The Page has a form which allows the superuser to add a blog to the blog collection. The blogs all have a general focus on highlighting products on the site. This feature is only available to the Superuser as the content is generated to promote sales. It is also hoped to provide engaging content to encourage users to come back for more. These blogs will also be shared in social media to draw followers.

<br>

<p align ="center">      
     <img src="assets/readme/images/addblog.jpg"  width="500" alt="add blog page" />    
</p>

<br/>

### 23. Edit Blog Page     <a name="editblogpage"></a>
 The link to edit a blog can be found at the bottom of individual blogs in the blog page and the bottom left side of the page below the blog in the blog detail page. The Edit Blog Page has a form which allows the superuser to edit an existing blog. A Toast will tell the user that they are editing the blog. When the blog is edited, the changes will be updated in the blog on the blog page. 

<br>

<p align ="center">      
     <img src="assets/readme/images/editblog.jpg"  width="500"  alt="edit blog page" />    
</p>

<br/>

### 24. Delete Blog Page     <a name="deleteblogpage"></a>
The link to delete a blog can be found at the bottom of individual blogs in the blog page and the bottom left side of the page below the blog in the blog detail page.The Delete Page has a form which allows the superuser to delete an existing blog. The user will be returned to the Blog page and their blog will have been removed.

<br>

<p align ="center">      
     <img src="assets/readme/images/deleteblog.jpg"  width="400"  alt="products page" />    
</p>

<br/>

<p align ="center">
The following pages are available to all users on the site.
</p>

<br> 

###  25. Signup Page   <a name="signuppage"></a>

On the Signup Page, a new user can sign up for the EssenChelle Oils website by filling out and submitting the form. On registering they will be assigned a Profile for the site. On registering they will be sent an email confirming their registration. 

<br>

<p align ="center">      
     <img src="assets/readme/images/signup.jpg" width="400"  alt="Registration Page" />    
</p>

<br/>

###  26. Login Page   <a name="loginpage"></a>

A registered User can log in to the website by inputting their username and password and they will have full access to all the logged in features within the site. If they are logged in and are a superuser they will have extra functionality enabled. If the user forgets their email they can choose the forget password link and they will be sent an email to reset their password. They can then login with their new password. They can use the checkout box to be remembered, to make it easier for them to log in the next time.


<br>

<p align ="center">      
     <img src="assets/readme/images/login.jpg" width="400" alt="Login Page" />    
</p>

<br/> 

###  27. Logout Page   <a name="logoutpage"></a>

In the Logout Page, the User can confirm that they want to exit the website and they can then log out of the site.

<br>

<p align ="center">      
     <img src="assets/readme/images/logout.jpg" width="400"  alt="Logout Page" />    
</p>

<br/> 

### 28. Custom Error Pages  <a name="error pages"></a>

I have included custom Error Pages in the error folder within the templates folder(403,404,405,500), Below is the image from the 404 page, but they all look similar, barring the fault lines.

<br>

<p align ="center">      
     <img src="assets/readme/images/errorpage.png" width="500"  alt="Sample Error Page" />    
</p>

<br/> 

<p align ="center"> 
The following panel feature is available to the superuser.
</p>

<br>

### 29. Admin Panel  <a name="adminpanel"></a>

The admin panel allows the admin/superuser to perform a wide range of functionalities within the site. The admin can add, delete, edit products and they can review and add or change details in all admin areas. The admin can also approve reviews for individual products and comments for individual blogs.

<br>

<p align ="center">      
     <img src="assets/readme/images/adminsignin.png" width="200" alt="Admin sign in" />    
</p>

<br>

<p align ="center">      
     <img src="assets/readme/images/adminpanel.jpg" width="900" alt="Admin Panel" />    
</p>

<br/> 

### 30. Security Measures  <a name="security"></a>

To ensure security on the site, only logged in users can access certain features on the site. A logged in user can add a product review or comment for a blog in the blog section. A superuser can add, updata and delete products within the admin panel. The superuser also has access to add, edit and delete products within the product pages. The superuser can add, edit and delete blogs in the admin panel but they can also access these capabilities within the blog page. Only the Admin/Superuser can access the admin Panel(would need sign in credentials).The Database URL and secret key are stored in the env.py file to prevent unwanted connections to the Database. As I was following the boutique ado walkthrough, I had not realised the secret key was commited in the early stages of the development, after doing my research into the issue and with the advice from CI, I generated a new key, and this was immediately put in the env.py file, making the other key obselete. All secret keys were included in the env.py file. Cross-Site Request Forgery (CSRF) Tokens are used on all Forms within the App for added protection. All keys needed for the inclusion of the database, Cloudinary, Stripe and for Email were concealed for security purposes.

<br>

<p align ="center">      
     <img src="assets/readme/images/security.png"  alt="Can't Access Message" />    
</p>

<br/> 


 #### [Return to Table of Contents](#toc)
----

 ## 8. Future Implementation  <a name="future"></a>

 <br>

 This is my first E-Commerce Site, so the main goal is to have a fully functional site with customised models to expand on the original concept as defined in the Boutique Ado Walkthrough. There were a number of features that I would like to expand upon in the future.

 In relation to the products, I would like to expand the information relating to the product. Besides the description, I would ike to include directions for use and cautions. You could also sort products according to the health conditions that can be addressed by using them i.e. insomnia, anxiety, respiratory issues.

 In regards to the blogs I have just added a few basic blogs, with heavy emphasis on product spotlighting for marketing purposes. These blogs could also be broken down into further categories. I could add a do it yourself section, where you could provide simple instructions for users to use the products in creative ways, this is incorporated into the present blog in a small way, but would be a great way for users to learn how to integrate the products into their lives. I would also include a recipe category where you could provide the user with recipes using the essential oils. This could be a good way to get users to interact with the site. you could ask the users to contribute their own recipes via the social media channels or by contacting the company directly with the contact form. User's recipes could then be featured on the site. Healthy Living could also be a category and you could give advice on how to use oils in the home and provide tips for everyday living in relation to EssenChelle Oils. These measures should not only drive sales, but should help to create a a thriving community with a shared interest in essential oils in general.

 In regard to the profiles, I would customise it more for the user, in the previous project I had an image for the profile user, but I would rather ensure I meet all the project criteria first, and if there was time at the end I could have explored this possibility, but I would hope to introduce this in a future iteration.

 In regard to the review, I had looked into the idea of using the ratings in the reviews in the product rating, but time restraints made this impossible at this time. It would be easier at this time to use existing ratings, as it would take time to generate actual ratings and with this restraint new products would not have any rating, and this would not be ideal. 

 In regards to logging in, I would also include logging in from a social network provider like Facebook, Twitter, or Google to facilitate the user experience for users.

 In regards to deals I would introduce a range of deals to encourage the user to buy multiple products at a special rate, from a marketing perspective I feel this would be conducive to driving more sales. In the long term I would also introduce a loyalty scheme, so that users would be rewarded for their consumer buying behaviour.

 To increase CRUD capabilities in the frontend for the superuser I would like to allow them to approve reviews for products and comments for blogs without needing to access the admin panel by allowing the superuser to see the comments and reviews on pages within the application, much in the same way as they can use the CRUD for products and blogs. This could also be done for the contact messages, currently these messages are saved in the database and can be accessed in the panel and the message is sent to the admin/staff user, but it would good to have the option to access this information freely within the site's frontend.

 <br>

#### [Return to Table of Contents](#toc)
----

 ## 9. Tools and Technology  <a name="technology"></a>

### Language Used:

-   [Python 3.8.10](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)    
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://www.javascript.com/)
-   [Django](https://www.python.org/)

### Technology Used:

-   [Am I Responsive](http://ami.responsivedesign.is/) - was used to create the multi-device mock-up above.
-   [Bootstrap v5.2.3](https://getbootstrap.com/)
-   [Git:](https://git-scm.com/) - used for version control, updated and commited changes. 
-   [GitHub:](https://github.com/) - is the respository for all the git pushes.
-   [Gitpod](https://gitpod.io/) - was the IDE Editor.
-   [Heroku:](https://heroku.com) - used to deploy the application.
-   [Stripe](https://stripe.com/en-ie) - used for payments on site.
-   [Mailchimp](https://mailchimp.com/) - used for the newsletter.
-   [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for Testing Site.
-   [ResponsiveTestTool](https://responsivetesttool.com/) - used for Responsive Testing.
-   [Markdown](https://markdown-guide.readthedocs.io/en/latest/) - Markdown Guide.
-   [Cloudinary](https://cloudinary.com/) - used for images for the site.
-   [Elephant SQL](https://www.elephantsql.com/) – deployed project on Heroku uses an Elephant SQL database. 
-   [Draw.io](https://drawio-app.com/) - used for the database diagram.
-   [Iconify.Design](https://iconify.design/) - Icons used for the site.
-   [LogoMaker](https://www.logomaker.com/) - For creating the Logo for the site.
-   [Favicon.io](https://favicon.io) - for making the site favicon.
-   [tinyPNG](https://tinyjpg.com/) - for image compression.
-   [Pixelied](https://pixelied.com/) - used to convert PNG to WEBP.
-   [Figma](https://www.figma.com/) - used for making the wireframes for the site.
-   [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - used to validate Python in Project.
-   [Accesibility Test](https://accessibilitytest.org/) - free accessibility testing tool.
-   [Dr Link Checker](https://www.drlinkcheck.com/) - used in conjunction with manual testing of links.
-   [XML- Sitempap](https://www.xml-sitemaps.com/) - used to create a sitemap for the site.
-   [Diffchecker](https://www.diffchecker.com/) - which was useful for finding coding errors in development.
-   [Temp Email Site](https://temp-mail.org/en/) - used to test emails for registering and purchasing on site.
-   [Page Speed Insights](https://pagespeed.web.dev/) - used to test speed and performance of website.
-   [Image Resizer](https://imageresizer.com/) - Used to Compress & Resize Images.
-   [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML code.
-   [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) - Used to validate CSS code.
-   [Pep8ci](https://pep8ci.herokuapp.com/) - Used to validate Python code. 
-   [JSHint](https://jshint.com/) - Used to validate JS code.

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

## 10. Testing  <a name="testing"></a>

<br>

Go to the [TESTING DOCUMENT](TESTING.md)

#### [Return to Table of Contents](#toc)
----

 ## 11. Bugs and Issues  <a name="bugs"></a>

 There have been a number of issues during development. Initially there was major issues with images, both sourcing assets and resizing them so they are uniform on the site. I wanted the products to carry the brand of the site, so this meant they had to be customised within photoshop. The special offer images are different in that they have a coloured background, but the sizing is the same, so I could live with that.

 
<br>

 ### Resolved <a name="resolved"></a>

 The webhooks were problematic at times mostly in relation to the URLS for the endpoints and making sure the secret keys are in place and the endpoint is activated on the stripe dashboard. Without being able to test with the testhooks earlier it was hard to know why they are not working and how to fix them when they were not working. Again when the project is deploayed going through this procedure again and testing a seperate endpoint. I had thought I had kept the code close to the stripe code in the walkthrough project but did have an issue with the code, I had added an extra return which meant although the order was processing correctly it never triggered the success page or the confirmation email after an order was processed and received help from tutor support to resolve the issue, which was accomplished with a series of print statements. There was at the same time an issue with an extra blank line in the header of the confirmation_email_subject, when these issues were fixed I finally managed to get the email message confirmation printing in the terminal within gitpod and I subsequently could receive email confirmations with the deployed site.

 There has been an issue with the webhooks in the gitpod site, the address has changed, which means I have been having to update the webhook url at times, when it stops working I review the address, and it usually has just changed by one number, and when it is updated it works ok again, I now check for url changes if I experience any issues. The Heroku webhook has no such problems, so the checkout should work as normal after submission.

 I had an issue when updating the quantity selector so it works on both the desktop and mobile screens, for this I just used the fix advised during the walkthrough video, and although I updated the 3 files, it did not work, so used the code diff application and found no difference, but it still did not work, so I got on to tutor support and explaied the issue, by the means of print statements, the problem was found in the script on the bag page, while updating the dollar signs to the euro signs throughout the site, when I wanted the currency to show euros instead of dollars, I had mistakenly added a euro in a query instead of the required dollar, so this had caused a 500 error, which displayed in the termnal, when this was replaced, it started to work as it was supposed to.

 I had an issue with the sidebar in the blog page, it worked fine on bigger screens but caused issues with smaller screens, so experimented on making it work, but in the end I made a decision to remove the sidebar on smaller screens, I don't think it takes anything from the page itself and was in the end the best decision for the site. The carousel too is a feature that does not make it to a smaller screen, so the about us page just has an image and the introductory text, which is sufficient for an about page.  The FAG page had an issue with hiding information in the collapsibles but have added a scroll to ensure the user gets to see all the neccessary content in the collapsibles.

 <br>

 ### Unresolved <a name="unresolved"></a>

 There is an issue in regards to sizes of products at the moment you will be offered different sizes within cerain products, which you can select successfully, there is an issue with applying 2 different prices to seperate sizes of the one product, which would need to be addressed. You can have either a small or large essential oil product in some items, but currently both products will be priced the same, now I could content the smaller bottle is of a higher quality and the larger bottle is a weaker solution and this could account for the pricing, but moving forward I would add additional functionality to offer a greater range of sizes for a greater range of products with a differing range of costs.  I really didnt want to deviate too much from the existing scripts, as I felt this might have a detrimental effect on the whole buying procedure and the inclusion of the Stripe functioning, but this would be an area that would need more of a deep dive for building E-commerce sites in the future.

While testing with lighthouse and page speed, the scores were affected by the inclusion of third party code essential for the site, this was mainly in the area of Boostrap, Jquery and mailchimp. I did try some minor fixes for these issues. In regards to the JQuery I did try to change to a newer JQuery version (3.4.1 to 3.5.1) but it stopped some functionality I had in regards to the navigation, so left it as it was. Right at the end I tried this again and have managed to update the Jquery without losing functionality. The mailchimp is included in every page, and the functionality of the newsletter subscription is provided by mailchimp, so I was not in a position to alter this code.
However the inclusion of their link and script has been problematic if I leave it at the end of the page, you get the thank you for subscribing message which is simple and effective, but causes issues with lighhouse. If I add it at the top it will take you to the mailchimp page, which seems to offer a subscriper more options, but causes an error with lighthouse, frankly there is no way of getting the location right in my experience, I can tell you either way the subscribers are saved in my mailchimp account and I am updated on receiving subscribers, so I guess it serves it's purpose. 

I did change my images to new generation webp formats, as Lighhouse suggested this would be beneficial for the site. The Javascript in the site was provided by code institute and I did not want to make any alterations in case the Stripe payments could have been badly effected. 

I did try to lessen the effects of render blocking issues in particular for mobile screens and despite trying to change the placement of settings, not sure if it helped any, not sure about cacheing and this would be an area worth exploring further. It is hard to test with lighthouse, when each time you use it the page goes down, so will use page speed until I get to the bottom of that issue. 

 <br>

<p align ="center">      
     <img src="assets/readme/images/renderblocking.png" width="600" alt="Rendering Blocking Issues" />    
</p>

<br>

 #### [Return to Table of Contents](#toc)
----


 ## 12. Deployment <a name="deployment"></a>

 The Project used Heroku for deployment. I used GitPod for development within the project and pushed to the GitHub Repository. This in turn updated the Project in Heroku. I used DEBUG = 'DEV' in os.environ, during development and other than when testing, had it configured so that I could work both locally and could also test the deployed Project on an ongoing basis. I added all the config vars for Stripe, AWS, The Database URL, and the creds for email. I originally has disabled collectstatic and the creds for AWS but removed these when I changed to cloudinary for static and media files.

 <br>

GitHub

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

- I had already signed up for ElephantSQl so just needed to create a new instance, I gave my plan a name, chose the tiny turtle(free plan) and selected the region as Ireland. I ensured all data was entered correctly and created my instance.
- I then found the name of the newly created instance in the Dashboard. I copied the database url, and added the config var DATABASE_URL to the other config vars in the Heroku settings and then you have to alter some of your existing code in your project. 
- You need to install dj_database_url and psycopg2 and update your requirements.txt to include these packages. You need to import these into your settings file. You need to add

 ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
 
  ````

  - It's important not to commit the actual database string for security reasons.
  - In the terminal, run the showmigrations command to confirm you are connected to the external database.
  - You should see a list of migrations, you should now be able to migrate your database models to your new database with the following command, and then follow up with categories and products (important to load categories first):
  
  ````
   python3 manage.py migrate
   python3 manage.py loaddata categories
   python3 manage.py loaddata products

  ````
  - Create a new Superuser for the new database
  - To prevent exposing the database when pushing to GitHub delete it from the settings.py (this will be reset as an environment variable)
  - You can check if your migrations have been successful by going back to your ElephantSQL dashboard and you need to select the browser option.
  - Click the Table queries button, select auth_user. When you execute you wil be able to see the details for your new superuser.

<br>

### Cloudinary for Images
- Sign up for Cloudinary(I already had an account after working with it on 4th project)
- Install Cloudinary's module into your project
- Go to Media Library and create a folder for your images
- Upload your images to that folder
- Click the three dots and copy the URL
- Paste the URL to your workspace where you want your images to appear
- Add your cloudinary URL to your ENV.py
- Add Cloudinary URL to Heroku Config Vars
- Add DISABLE_COLLECTSTATIC to Heroku Config Vars(temporarily, must be removed before deployment)
- Add cloudinary to the list of INSTALLED_APPS in settings.py
- Add the following code in the settings file to tell Cloudinary to store media and static files
  
````
STATIC_URL = '/static/'
STATICFILES_STORAGE =
'cloudinary_storage.storage.StaticHashedCloudinaryS
torage'
STATICFILES_DIRS = [os.path.join(BASE_DIR,
'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
````

- Link file to the templates directory in Heroku Place under the BASE_DIR line
  
````  
TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
````

- Change the templates directory to TEMPLATES_DIR Place within the 
  
```` 
TEMPLATES array 'DIRS': [TEMPLATES_DIR]
````

- Add Heroku Hostname to:


````  
ALLOWED_HOSTS =
["PROJ_NAME.herokuapp.com", "localhost"]
````


### Add Stripe keys to Heroku
- Sign into your stripe account and click 'Developers' located in the top right of the navbar.
- You can select the webhook tab and on the page you can add an endpoint.you will need to input the link to your heroku app followed by /checkout/wh/. 
- You can click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
- Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
- Go to your heroku account and navigate to the config vars section in your settings tab. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
- Add these values under these keys:

````
- STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
- STRIPE_SECRET_KEY = 'insert your secret key'
- STRIPE_WH_SECRET = 'insert your webhooks secret key'
- In your setting.py file in django, insert the following near the bottom of the file:

- STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
- STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
- STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')    
````

When you go through the purchasing process on your site, you can check on your webhooks to see if they have succeeded. I enabled a webhook for the gitpod site and the deployed site. Every so often in the gitpod webhook, it would fail and you would have to check if the url had changed, it changes now and again usually by just one number, but it is enough to make it fail. In the early stages, I had not noticed the url change and figured it was an issue with the code, but as time went on and if there was an issue I just updated the endpoint address and it would work again. The endpoint for the deployed site does not change, but if the url changes after submission, the url in the gitpod site may be updated again and the webhook may fail(in gitpod site).

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

 All images on the site were sourced in Pexels, the initial template for the essential oil and massage oil bottles were sourced in freepics. These templates were used in photoshop in combination with a brand created with [LogoMaker](https://www.logomaker.com/) to create customised images with the essenchelle brand, to add authenticity to the website. The Doterra essential oil images were found on the Pexel's site, but they were referenced in the product description. A number of the Oil Burners were souced on a shopping site.

 The logo and Favicon were built with the online tools: [LogoMaker](https://www.logomaker.com/) and 
 [Favicon.io](https://favicon.io/)

 The Project began with the basic code used in the 'Boutique Ado' walkthrough Project, but was modified according to my own needs within the Project. As the Project developed, I sought out various Tutorials and consulted documentation for Django and Stripe. I also used some code from the Blog Walkthrough from Project 4.

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

Thank you also to Joshua, Jason and Holly, who helped me in a IDE issue near the end of the Project.

Thank you to my Mentor Brian Macharia for all your help and guidance for all my Projects.

<br>

 #### [Return to Table of Contents](#toc) 
----

## Author Info

Michelle Hickey, Full Stack Software Developer.
- [Linkedin](https://www.linkedin.com/in/michellehickey1/)
- [Portfolio](https://michellehickey.crevado.com/)
- [UX Portfolio](https://www.behance.net/michellehickey2)

<br>

[Back to the Top](#table-of-contents)