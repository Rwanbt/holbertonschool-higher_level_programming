const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMoviesElement = document.querySelector('#list_movies');

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const newli = document.createElement('li');
    newli.textContent = movie.title;
    listMoviesElement.appendChild(newli);
    });
  })
