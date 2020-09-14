# Data Centric Milestone Project - [Kool Recipes](https://kool-recipes.herokuapp.com/)
Developed by: Christopher Koolman

![N|Solid](https://www.linkpicture.com/q/koolrecipereadmeimg.jpg)

## Table Of content
1. [Database Schema](#dbsch)
2. [User Experience Approach](#ux)
3. [Technologies Used](#techu)
4. [Testing](#test)
5. [How To Deploy](#deploy)
6. [How To Deploy To Heroku From GitPod](#deplgitp)
7. [Credits](#credit)

#### Milestone Project Description:

The project is focused on Project Idea Nr. 1. 
To develop an Online Cookbook/Recipe website/app, which the site owner's goal is to promote a brand of cooking tools. The website/app gives the user the ability to Create, Read, Update and Delete (CRUD) functionalities.
The user should be able to view and access the cooking recipes. The user is also able to enjoy the additional features such as, Promos Ad Page (Ads of Cookingware on the landing page, and dedicated page illustrating promotions) and option to "Like" a recipe.  

<a name="dbsch"></a>
## Databse Schema

The project has been created with the following MongoDB Collections:
- Recipes
- Categories
- Ads

The main collection is the "Recipes" collection, because it basically includes the related collection selection possibility in order to complete the complete recipe page.


Recipes are added by completing the [Add Recipe](https://kool-recipes.herokuapp.com/add_recipe), Categories by completing the [Add Category](https://kool-recipes.herokuapp.com/add_category), and Ads can be edited by selecting ad>edit button to be directed to the edit page from the [Ad](https://kool-recipes.herokuapp.com/get_ads)
All fields included in a recipe: 
- Recipe Name
- Recipe Author
- Likes (Ability to click & add a Like and show how many likes have been given)
- Image URL Link (Used to display card image and full recipe page)
- Category Name
- Short Description
- Preparation Time
- Cooking Time
- Total Time
- Servings
- Ingredients
- Instructions

All related fields are populated as follow, "Home Page"(Recipes are puplated on a Materialize Card(with functionality of revealing more info and directing to recipe page)) and "Recipe Page"(full page with all fields populated)

All fields included in a category: 
- Category Name
- Category Description
- Category Image Url (Used to display card background image)

Categories are populated on the "Categories Page".

All fields included in a ads: 
- Ad Promo Name
- Ad Promotion Url (Used to display card image)

Ads are dynamically populated on the "Home Page", "Recipe Page" and "Promos Page".

<a name="ux"></a>
## User Experience Approach

#### User stories

1. The home provides dynamically generated Materialze Cards with "Recipe" details (Picture, Recipe Name and Likes)
2. The user can click on the Recipe Card in order to reveal additional info from the revealed content.
3. In the revealed content the user can see Prep Time, Cooking Time, Servings and have the ability to view Recipe(redirected to Recipe Page) or Promo(redirected to Ads Page)
4. All users can Create, Read, Update and Delete (Recipes)
5. Users are only able to Add and Edit Categories
6. Users are only able to edit Ads.
7. Users can Like a recipe from the "Recipes Page"(landing page with all dynamically generated Recipe Cards) or in the "Recipe Page"(Recipe Specific Page illustrating the complete Recipe)

<a name="techu"></a>
## Technologies used:
- [HTML](https://www.w3schools.com/html/) - W3C Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser.
- [CSS](https://www.w3schools.com/css/) - W3C Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
- [Python](https://www.python.org/) - Programming Language to create the backend that decides upon the responses to the user's input.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - python web framework to hold all the code and templates together as one site.
- [MongoDB](https://www.mongodb.com/) - Non-relational database to store all information about the recipes, cuisines etc.
- [GitPod](https://www.gitpod.io/) & [GitHub](https://www.github.com/) -for version control and backup of code

##### Libraries I needed to install
- [JQuery](https://jquery.com)
    - The use for **JQuery** si to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

<a name="test"></a>
## Testing

#### Create Read Update Delete (CRUD) Testing

I strarted with the basic functionalities which included: Create, Read, Update and Delete of 2 collections (Recipes, Categories), the Ads collection only has the Create, Read na Update functionalities, deleting would eliminate the option of promotin cooking tools. 
Testing for Creating a Recipe included that all fields were recorded accordingly in the database. Another feature that I tested was the recipe "Likes" option, to verify if the button was triggering incremental "likes" writing in the database.

 
#### Cross-Device and Browser Testing
The browser that I used for developing in GitPod was Chrome. I also tested on Mozilla Firefox which didn't show any issues.The only remaining issue is the classes redering of Like Button in the Safari Browser.
As the most important approach being Mobile First Approach, it was important to test the responsiveness on different devices and browser simulators.
Website used for testing responsivenes [Am I Responsive ?](http://ami.responsivedesign.is/#)

#### Devices tested on included:

- iPhone 6, 7, 8, X, XS, XS Max
- Samusng Galaxy S5, S9, S9+
- Goole Pixel 2, 2XL
- iPad, iPad Mini, iPad Air, iPad Pro

Overall responsiveness is to my satisfaction. (See image below for cross device responsiveness)

![N|Solid](https://www.linkpicture.com/q/crossdevicetesting.png)


#### Code Validation
Good Coding Practice Requires that all codes are validated through online validators, in order to check if there are errors.
- [The W3C CSS Validation Service](jigsawjigsaw.w3.org)
- [The W3C Markup Validation Service](validator.w3.org)
- [pep8online](http://pep8online.com) - for Python

#### Development Troubleshooting

<a name="deploy"></a>
## How To Deploy
- The project was deployed on [Heroku](https://www.heroku.com)
- Dependencies require that a Procfile and requirements.txt are generated/created.
- Created New Heroku App and set environment variables.
- Added the environment variables as good practice.
- Proceeded to link the environment and Github with Heroku
- Pushed code to Heroku.
- Link the existing [Mongodb](https://www.mongodb.com)
- Deployed website can be found [here](https://kool-recipes.herokuapp.com/).

<a name="deplgitp"></a>
## How to Deploy to Production on Heroku from GitPod


In order to deploy this project on Heroku, please follow these steps:
1. Sign-in or Sign-up on [Heroku](https://www.heroku.com) account
2. Install Heroku CLI in the gitpod terminal if it hasn't been installed


```console
$ sudo snap install --classic heroku

```

3. If Heroku CLI has been installed, type in the below to login Heroku in order to login from CLI instead of opening a browser window

```console
$ heroku login -i

```

4. If you have already created an app on the Heroku website you can skip this step, if not type the following command in the CLI so you can create a new app from the CLI. Replace `<the_name_of_the_project>` with the name of your new app for expample: Kool Recipes, heroku will notify if the App Name is available.  

```console
$ heroku create <name_of_the_project>

```

5. To create a repository enter the following () 

```console
$ git remote -v
```

6. Install dotenv with pip3 (will assist for production deployment)

```console
$ pip install python-dotenv
```

7. Create a Procfile which inidcates which file needs to be used to get the app running, by running the following command 

```console
$ echo web: python app.py > Procfile
```

8. Your app requires key dependencies to run, in order to inlude these run the following command in the CLI 

```console
$ pip3 freeze --local > requirements.txt 
```

9. Don't forget to commit the project to github

```console
$ git add . && git commit -m "Added Procfile and Requirements.txt"
```

10. You can now push your code to Heroku Master:

```console
$ git push heroku master
```

11. IMPORTANT Detail before opening the deployed App URL from Heroku. You will need to add the following environment variables from the CLI to Heroku. Replace `<user>`, `<password>` and `<dbname>`

```console
$ heroku config:set MONGODB_URI='mongodb+srv://`<user>`:`<password>`'@cluster0,lc0dy.mongodb.net/`<dbname>`?retryWrites=true'
$ heroku config:set MONGO_DBNAME='`<dbname>`'
```

12. Congratulations, the app has been deployed and you can find the URL from the Heroku dashboard `https://dashboard.heroku.com/apps/<projectname>`.

<a name="credit"></a>
## Credits

* Google Fonts: https://fonts.google.com
* Materializecss: https://materializecss.com
* Pixabay: https://www.pixabay.com
* Pexels: https://www.pexels.com
* Color Hex: http://www.color-hex.com
* Pine Tools: https://pinetools.com
* Pixlr Photo Editor: https://pixlr.com
* Photo Resizer: https://www.photoresizer.com
* jQuery: https://code.jquery.com/
* W3Newbie Tutorials: https://w3newbie.com/w3newbie-tutorials/
* W3School (HTML and CSS): https://www.w3schools.com/default.asp
* Code Institute Modules: Course Resources from all Modules 
* Stackoverflow: https://stackoverflow.com/ 
* GitHub: https://www.github.com
* GitPod: https://www.gitpod.io
* Animate.CSS: https://animate.style/

### Media
* Pixabay: https://www.pixabay.com
* Google: https://www.google.com
* Pexels: https://www.pexels.com
* Poster My Wall: https://www.postyermywall.com
* Link Picture: https://www.linkpicture.com

### Acknowledgements
- [All Recipes](https://www.allrecipes.com/recipes/) for utilizing their recipes for my mongodb entries and content.
- All Credits Go to the Authors/Chefs of all the recipes included.

