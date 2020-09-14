import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('recipes.html')
    
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', 
    recipes=mongo.db.recipes.find())

# This functionality allows user to click on the Like button and it will increment the total count
@app.route('/like/<recipe_id>', methods=["POST"])
def like(recipe_id):
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$inc":
                                                               {'likes': 1}})
    return redirect(url_for('recipe_complete', recipe_id=recipe_id))

# Option to insert a specific recipe into the database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# This functionality will render the addrecipe page to insert fields and create a new recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', 
    categories=mongo.db.categories.find())

# This route will find the specific recipe id and render the recipecomplete.html page displaying all the details
@app.route('/recipe/<recipe_id>')
def recipe_complete(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipecomplete.html", recipe=the_recipe, 
    ads=mongo.db.ads.find())

# This route will render the editrecipe.html page displaying so the specific recipe can be edited/updated.
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)

# This route will POST any updated fields to the database.
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_author_name':request.form.get('recipe_author_name'),
        'category_name':request.form.get('category_name'),
        'recipe_description':request.form.get('recipe_description'),
        'recipe_prep_time':request.form.get('recipe_prep_time'),
        'recipe_cooking_time':request.form.get('recipe_cooking_time'),
        'recipe_total_time':request.form.get('recipe_total_time'),
        'recipe_servings':request.form.get('recipe_servings'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_instructions':request.form.get('recipe_instructions'),
        'recipe_img_url':request.form.get('recipe_img_url')
    })
    return redirect(url_for('get_recipes'))

# This route will send the remove command to the database in order to remove the specific recipe permanently
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

# This route will render all categories on the categories.html page
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())  

# This route will render the editcategory.html page in order to edit the specific category selected  
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html', 
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

# This route will POST any updated fields to the database.
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories = mongo.db.categories
    categories.update({'_id': ObjectId(category_id)},
    {
            'category_name':request.form.get('category_name'),
            'category_description':request.form.get('category_description'),
            'category_img_url':request.form.get('category_img_url')
            
    })
    return redirect(url_for('get_categories'))

# This route will insert a new category into the database.
@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {
        'category_name': request.form.get('category_name'),
        'category_description': request.form.get('category_description'),
        'category_img_url': request.form.get('category_img_url')
    }
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))

# This route will render the addcategory page   
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

# This route will render the ads page to view ads    
@app.route('/get_ads')
def get_ads():
    return render_template('ads.html', 
    ads=mongo.db.ads.find())

# This route will render the editad.html page in order to edit the specific ad selected  
@app.route('/edit_ad/<ad_id>')
def edit_ad(ad_id):
    return render_template('editad.html', 
    ad=mongo.db.ads.find_one({'_id': ObjectId(ad_id)}))

# This route will update the specific ad into the database.
@app.route('/update_ad/<ad_id>', methods=['POST'])
def update_ad(ad_id):
    ads = mongo.db.ads
    ads.update({'_id': ObjectId(ad_id)},
    {
            'ad_url_one':request.form.get('ad_url_one'),
            'ad_promo_name':request.form.get('ad_promo_name')
            
    })
    return redirect(url_for('get_ads'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)