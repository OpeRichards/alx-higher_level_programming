$(document).ready(function() {
    const movieList = $('UL#list_movies');
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: (data) => {
            const listItems = data.results.map(movie => `<li>${movie.title}<li>`).join('');
            movieList.append(listItems);
        }
    });
});
