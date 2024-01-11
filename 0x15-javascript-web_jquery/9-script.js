const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, (res, status) => { $('DIV#hello').text(res.hello); });
