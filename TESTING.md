# EssenChelle Oil: Testing


Back to the [README](README.md)

Testing has taken place continuously throughout the development of the project. When faults were detected they were fixed on an ongoing basis. These were fixed locally in GitPod and committed to GitHub regularly. Faults fixed and outstanding can be found in the README.md Document.

# Table of Contents <a name="toc"></a>

1. [Cross Browser Testing](#browsertesting)
2. [Responsive Testing](#responsivetesting)
3. [Validator Testing](#validatortesting)
     1. [W3C Validator](#w3c)
     2. [CSS Validator](#css)
     3. [Python](#python)
     4. [Lighthouse](#lighthouse)
     5. [Accessabilty](#accessability)
     6. [Contrast Checker](#contrastchecker)
     7. [WAVE](#wave)
     8. [Link Checker](#linkchecker)
4. [Manual Testing](#manual)
5. [User Story Testing](#userstorytesting)  

#### [Return to README.md](README.md)
----


## Cross Browser Testing<a name="browsertesting"></a>

  The site was tested in Google Chrome, Microsoft Edge and Mozilla Firefox on the Desktop. The site was tested on a Lenovo Laptop, and a Xiomai Redmie Note 11. 

<br/>


#### [Return to Table of Contents](#toc)

----
## Responsive Testing<a name="responsivetesting"></a>

   I regularly tested the responsiveness of the site using Google Chrome Developer tools, information on this can be found [here](https://developer.chrome.com/docs/devtools/). I also used Window Resizer and a Responsive Design Tester Application available in the Google Chrome Store. I also used the Am I responsive site to test the site and the image below is from that Testing:

   <br/>

   <p align ="center">      
      <img src="assets/readme/images/responsive.png" width="600" alt="AmIResponsive results"/>   
   </p>

   <br/> 


#### [Return to Table of Contents](#toc)

----
## Validator Testing<a name="validatortesting"></a>

1. W3C Validator <a name="w3c"></a>

Using [https://validator.w3.org/](https://validator.w3.org/) All Pages were tested with the validator, the results of the HTML validation can be seen below:


<br/>

<p align ="center">      
     <img src="assets/readme/images/html validation.png"  width="700" alt="HTML Validation results"/>   
</p>
<br/>  
  
2. Jigsaw CSS Validator   <a name="css"></a>
 
Using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) 
The result can be seen below:

<br/>
<p align ="center">      
     <img src="assets/readme/images/cssvalidation.png" width="700" alt="CSS Validation results"/>   
</p>
<br/>

3. Python Validation   <a name="python"></a>
  Python testing was done without the use of Pep8 as the site was down, instead an extension was added which highlighted errors and showed them in the problems panel within gitpod. Most errors during the build related to long lines, which I rectified. I also used [Code Institute Python Linter](https://pep8ci.herokuapp.com/)

  <br/>

  <p align ="center">      
     <img src="assets/readme/images/pep8.png" width="600" alt="python validation"/>   
  </p>
  
  <br>


4. Lighthouse Testing   <a name="lighthouse"></a>


<p align ="center">      
     <img src=assets/readme/images/ width="600"  alt="lighouse testing specs" />    
</p>
<br/> 

5. Accessability Testing   <a name="accessability"></a>
Used this tool, [Accesibility Test](https://accessibilitytest.org/) which carries out a range of tests on the site and the score can be seen below:

<p align ="center">      
     <img src="assets/readme/images/" width="700" alt="accessabilty testing specs" />    
</p>

<br/> 

6. Contrast Checker  <a name="contrastchecker"></a>
  
  Using [https://color.a11y.com/](https://color.a11y.com/)   See images Below.

<br/>
  <p align ="center">      
     <img src="assets/readme/images/colourcontrast.png"  width="700" alt="contrast results"/>   
  </p>
  
  <br>

7. Wave (Web Accesability Evaluation tool)   <a name="wave"></a>
  
<br/>

  <p align ="center">      
     <img src="assets/readme/images/wave.png"  alt="wave test result"/>   
  </p>
  
  <br>

8. Link Checker   <a name="linkchecker"></a>
Besides manually checking links on the site I used this tool as an extra measure for testing and the result can be seen below:

<br/>

  <p align ="center">      
     <img src="assets/readme/images/linkchecker.png"  alt="linkchecker result"/>   
  </p>
  
  <br>


 #### [Return to Table of Contents](#toc)
----  

### 4. Manual Testing   <a name="manual"></a>

I have broken the manual testing into 2 sections, the first gives an overview of how the site works and whether it does what is expected. In the second section I have more specific testing of different elements within each page and the subsequent results.

<h3 align ="center">      
    Manual Testing (Overview of how the Site works in general)   
</h3>


### On the Site:
- Start Screen displays when Heroku link is used.   :heavy_check_mark:
- The searchbar shows the results when search criteria is entered and selected.  :heavy_check_mark:
- The Account Link displays correctly for a user that is not logged in, it show Register and Login.  :heavy_check_mark:
- The Register link opens up the sign up form and allows a User to register for the site.  :heavy_check_mark:
- The Login Link opens up the login form and allows the User to login into the site.  :heavy_check_mark:
- The Account Icon displays a new set of options in the dropdown menu when the user is logged in and it is selected. :heavy_check_mark:
- The Product Management dropdown item takes you to the add product page.  :heavy_check_mark:
- The My Profile dropdown item takes you to the profile page.   :heavy_check_mark:
- The Product Favourites dropdown item takes you to the product favourites page.  :heavy_check_mark:
- The Logout link displays when the user has logged in.  :heavy_check_mark:
- The Logout dropdown item takes you to the Log out page.  :heavy_check_mark:
- The Logout link opens up the logout form and allows the User to logout of the site.  :heavy_check_mark:
- The Shopping Icon takes you to the Shopping Bag Page.  :heavy_check_mark:
- The all products link in the navbar shows the dropdown menu with the different options available  :heavy_check_mark:
- The by price options shows all products in order of price.  :heavy_check_mark:
- The by price options shows all products in order of rating.  :heavy_check_mark:
- The by price options shows all products in order of category.  :heavy_check_mark:
- The all products options shows all products.  :heavy_check_mark:
- The EssenChelle Products link in the navbar shows the dropdown menu with the different options available.
- The Essential Oils option shows all products in the Essential range.  :heavy_check_mark:
- The Massage Oils option shows all products in the Massage range.  :heavy_check_mark:
- The Oil Burner option shows all products in the Oil Burner range.  :heavy_check_mark:
- The all products options shows all products in the EssenChelle range.  :heavy_check_mark:  
- The Our Story link in the navbar shows the dropdown menu with the different options available.  :heavy_check_mark:
- The About us option takes you to the about us page.  :heavy_check_mark:
- The Our Products option takes you to the our products page.  :heavy_check_mark:
- The Blog option takes you to the blog page.  :heavy_check_mark:
- The Special Offers link in the navbar shows the dropdown menu with the different options available.
- The New Arrivals option shows the new arrival products.  :heavy_check_mark:
- The Deals option shows the new deals in products.  :heavy_check_mark:
- The Clearance option shows all the clearance products.  :heavy_check_mark:
- The all products options shows all products in Special Offers.  :heavy_check_mark: 
- The Contact link in the navbar shows the dropdown menu with the contact form option available.  :heavy_check_mark:
- The contact form opens up the contact page with the contact form for messaging.  :heavy_check_mark: 



<details>
  <summary>Manual Testing(part 2)</summary>

<br>

### Navigation (on all pages)

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Logo              | Navigation Link               | Click On |   ✔       | 
|  Home              | Navigation Link               | Click On |   ✔       |
|              | Navigation Link               | Click On |   ✔       |
|            | Navigation Link               | Click On |   ✔       |
|  Account           | Dropdown Menu                 | Click On |   ✔       |
|  Sign Up           | Navigation Link               | Click On |   ✔       |
|  log In            | Navigation Link               | Click On |   ✔       |
|  Profile           | Navigation Link               | Click On |   ✔       |
|  Log Out           | Navigation Link               | Click On |   ✔       |

<br>