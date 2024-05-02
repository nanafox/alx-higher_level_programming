// Toggles the class of the `<header>` element when the user clicks on the tag
// `div#toggle_header`

$('div#toggle_header').on('click', () => {
  $('header').toggleClass('green red');
});
