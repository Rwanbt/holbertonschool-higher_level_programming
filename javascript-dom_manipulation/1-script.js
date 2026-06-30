const redHeaderButton = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderButton.addEventListener('click', () => {
  headerElement.style.color = '#FF0000';
});
