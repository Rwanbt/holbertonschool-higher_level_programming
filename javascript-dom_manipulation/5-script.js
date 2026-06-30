const updateHeaderButton = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateHeaderButton.addEventListener('click', () => {
  headerElement.textContent = 'New Header!!!';
});
