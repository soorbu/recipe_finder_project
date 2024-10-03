console.log('JavaScript file loaded!');
let ingredientCounter = 0;

document.addEventListener('DOMContentLoaded', function() {
    const addIngredientBtn = document.querySelector('#add-ingredient-btn');
    const ingredientSection = document.querySelector('#ingredients');

    console.log('Button:', addIngredientBtn);
    console.log('Ingredient section:', ingredientSection);

    addIngredientBtn.addEventListener('click', () => {
        // alert("button clicked");
        // console.log('Button clicked!');
        const newIngredientRow = document.createElement('div');
        newIngredientRow.classList.add('ingredient-row');
        newIngredientRow.innerHTML = `
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                <label for="ingredient_name_${ingredientCounter}">Ingredient Name:</label>
                <input type="text" id="ingredient_name_${ingredientCounter}" name="ingredient_name_${ingredientCounter}">
                <label for="quantity_${ingredientCounter}">Quantity:</label>
                <input type="text" id="quantity_${ingredientCounter}" name="quantity_${ingredientCounter}">
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 10px;">
                <button class="add-ingredient-btn">Add Ingredient</button>
                <div style="width: 20px;"></div>
                <button class="remove-ingredient-btn">Remove Ingredient</button>
            </div>
        `;
        ingredientSection.appendChild(newIngredientRow);

        // Add event listeners to the cloned buttons
        const clonedAddBtn = newIngredientRow.querySelector('.add-ingredient-btn');
        const clonedRemoveBtn = newIngredientRow.querySelector('.remove-ingredient-btn');

        clonedAddBtn.addEventListener('click', () => {
            // Add ingredient logic here
            addIngredientBtn.click();
        });
        clonedRemoveBtn.addEventListener('click', () => {
            // Remove ingredient logic here
            newIngredientRow.remove();
        });

        ingredientCounter++;
        console.log('New ingredient row added!');
    });
});