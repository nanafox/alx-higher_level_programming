// Adds an `<li>` element to a list when the user clicks ont the `div#add_item`
// tag

$('div#add_item').on('click', () => {
  $('ul.my_list').append('<li>Item</li>');
});
