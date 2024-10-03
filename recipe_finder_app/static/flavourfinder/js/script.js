// Get the animation element
const cursorAnimation = document.querySelector('.cursor-animation');

// Get the button element
const getStartedButton = document.querySelector('.btn');

// Add an event listener to the button to trigger the animation
getStartedButton.addEventListener('mouseover', () => {
  cursorAnimation.classList.add('animate');
});

getStartedButton.addEventListener('mouseout', () => {
  cursorAnimation.classList.remove('animate');
});