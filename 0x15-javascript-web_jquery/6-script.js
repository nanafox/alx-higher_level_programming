// Updates the text of the `<header>` element to 'New Header!!!' when the user
// clicks on the `div#update_header` element

$('div#update_header').on('click', () => {
  $('header').text('New Header!!!');
});
