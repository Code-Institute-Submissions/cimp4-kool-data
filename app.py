
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)