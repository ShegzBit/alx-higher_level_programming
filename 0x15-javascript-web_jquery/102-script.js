const url = 'https://hellosalut.stefanbohacek.dev/';

$('INPUT#btn_translate').click(() => {
  $.ajax({
    url,
    data: { lang: $('INPUT#language_code').val() },
    success: (res) => {
      $('DIV#hello').text(res.hello);
    }
  });
});
