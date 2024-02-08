$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (response) {
      $('DIV#hello').text(response.hello);
    }
  }).fail(function (error) {
    console.log(error);
  });
});
