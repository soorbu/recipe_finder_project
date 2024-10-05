Recipe Finder Project
Recipe Finder is a web application that allows users to discover, add, and search for recipes based on ingredients and categories. The project aims to make cooking easier by offering a simple and intuitive way for users to search for recipes that match their available ingredients or culinary preferences.

Key Features
User Accounts: Users can create accounts and log in to save their favorite recipes or add their own.
Recipe Search: Users can search for recipes by ingredients or select from multiple categories.
Add Recipes: Users can contribute their own recipes by entering details such as title, ingredients, instructions, and categories.
Ingredient and Category Filtering: Recipes can be filtered using a combination of multiple ingredients or categories, allowing for more personalized results.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS (with a plain homepage and a background image)
Database: SQLite (db.sqlite3) with tables for recipes, ingredients, and categories connected through many-to-many relationships.
User Authentication: Custom user models with fields for username, password, and name, integrated into the account creation system.
Project Setup
Clone the repository:

git clone https://github.com/soorbu/recipe_finder_project.git
Navigate to the project folder:

cd recipe_finder_project
Install dependencies and run the Django migrations:

pip install -r requirements.txt
python manage.py migrate
Run the development server:

python manage.py runserver
Access the app at http://127.0.0.1:8000.

Database
The project uses db.sqlite3 as the default database. You can create your own database using Django's migration system or populate the database with test data through fixtures.

Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!
