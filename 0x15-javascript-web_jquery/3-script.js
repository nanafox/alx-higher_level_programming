// Adds the class `red` to the `<header>` element when the user clicks on the
// tag `div#red_header`
$('div#red_header').on('click', () => {
  $('header').addClass('red');
});
