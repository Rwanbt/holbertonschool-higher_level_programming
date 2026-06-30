document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElement = document.querySelector('#hello');

  fetch(url)
    .then((reponse) => {
        return reponse.json();
    })
    .then(data => {
        helloElement.textContent = data.hello;
    });
});
