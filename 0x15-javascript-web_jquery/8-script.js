const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (res, status) => {
  $.each(res.data.results, (index, result) => {
    $('UL#list_movies').append($('<li></li>').text(result.title));
  });
});
