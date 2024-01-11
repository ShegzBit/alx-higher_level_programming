$('DIV#toggle_header').click(() => {
  const $header = $('header');
  const addedClass = ($header.hasClass('green') ? 'red' : 'green');
  const removedClass = (addedClass === 'red' ? 'green' : 'red');
  $header.removeClass(removedClass);
  $header.addClass(addedClass);
});
