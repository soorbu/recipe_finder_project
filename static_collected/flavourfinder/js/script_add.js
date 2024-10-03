// console.log('JavaScript file loaded!');
// let ingredientCounter = 0;

// document.addEventListener('DOMContentLoaded', function() {
//     const addIngredientBtn = document.querySelector('#add-ingredient-btn');
//     const ingredientSection = document.querySelector('#ingredients');

//     console.log('Button:', addIngredientBtn);
//     console.log('Ingredient section:', ingredientSection);

//     addIngredientBtn.addEventListener('click', () => {
//         alert("button clicked");
//         console.log('Button clicked!');
//         const newIngredientRow = document.createElement('div');
//         newIngredientRow.classList.add('ingredient-row');
//         newIngredientRow.innerHTML = `
//             <label for="ingredient_name_${ingredientCounter}">Ingredient Name:</label>
//             <input type="text" id="ingredient_name_${ingredientCounter}" name="ingredient_name_${ingredientCounter}">
//             <label for="quantity_${ingredientCounter}">Quantity:</label>
//             <input type="text" id="quantity_${ingredientCounter}" name="quantity_${ingredientCounter}">
//         `;
//         ingredientSection.appendChild(newIngredientRow);
//         ingredientCounter++;
//         console.log('New ingredient row added!');
//     });
// });

console.log('JavaScript code executed!');

const addIngredientBtn = document.getElementById('add-ingredient-btn');
console.log(addIngredientBtn);

addIngredientBtn.addEventListener('click', () => {
  console.log('Button clicked!');
  alert('Button clicked!');
});