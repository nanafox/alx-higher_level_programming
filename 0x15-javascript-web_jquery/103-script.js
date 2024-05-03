// fetches and prints how to say “Hello” depending on the language

const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

$(document).ready(() => {
  $('input#btn_translate').on('click', () => {
    const lang = $('input#language_code').val();
    $.get(url + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').on('keypress', (e) => {
    if (e.key === 'Enter') {
      const lang = $('input#language_code').val();
      $.get(url + lang, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
