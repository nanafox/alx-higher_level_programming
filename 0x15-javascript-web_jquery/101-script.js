// adds, removes and clears `<li> elements from a list when the user clicks
$(document).ready(() => {
  $('div#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').on('click', () => {
    $('ul.my_list li').last().remove();
  });

  $('div#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
