let ingredientRowCounter = 0;

// Add event listener to add ingredient button
document.getElementById('add-ingredient-btn').addEventListener('click', (event) => {
    event.preventDefault();
    const ingredientsDiv = document.getElementById('ingredients');
    const newIngredientRow = document.createElement('div');
    newIngredientRow.className = 'ingredient-row';

    const ingredientNameField = document.createElement('input');
    ingredientNameField.type = 'text';
    ingredientNameField.name = `ingredient_name_${ingredientRowCounter}`;
    ingredientNameField.placeholder = 'Ingredient Name';

    const quantityField = document.createElement('input');
    quantityField.type = 'text';
    quantityField.name = `quantity_${ingredientRowCounter}`;
    quantityField.placeholder = 'Quantity';

    const removeButton = document.createElement('button');
    removeButton.className = 'remove-btn';
    removeButton.textContent = 'Remove';

    newIngredientRow.appendChild(ingredientNameField);
    newIngredientRow.appendChild(quantityField);
    newIngredientRow.appendChild(removeButton);

    ingredientsDiv.appendChild(newIngredientRow);
    ingredientRowCounter++;
});