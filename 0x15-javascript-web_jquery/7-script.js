// Fetches the StarWars character name from
// 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, (data, status) => {
  if (status === 'success') {
    $('#character').append(data.name);
  }
});
