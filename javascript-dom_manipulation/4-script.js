const addItemButton = document.querySelector('#add_item');
const listElement = document.querySelector('.my_list');

addItemButton.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  listElement.appendChild(newLi);
});
