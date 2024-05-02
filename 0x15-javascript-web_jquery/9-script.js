// Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the
// value of hello from that fetch in the HTML tag div#hello.

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, (data) => {
  $('div#hello').text(data.hello);
});
