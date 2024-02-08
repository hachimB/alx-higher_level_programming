$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    for (let i = 0; i < response.results.length; i++) {
      $('UL#list_movies').append('<li>' + response.results[i].title + '</li>');
    }
  }
}).fail(function (error) {
  console.log(error);
});
