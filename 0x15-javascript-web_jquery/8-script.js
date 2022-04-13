$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const res of data.results) {
    $('#list_movies').append(`<li>${res.title}</li>`);
  }
});
