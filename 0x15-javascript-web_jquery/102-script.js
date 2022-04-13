window.onload = () => {
  $('#btn_translate').click(() => {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    const valueLan = $('#language_code').val();
    $.get(url + valueLan, (data) => {
      $('#hello').html(data.hello);
    });
  });
};
