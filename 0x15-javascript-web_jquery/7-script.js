$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function (response) {
    $('DIV#character').text(response.name);
  }
}).fail(function (error) {
  console.log(error);
});
