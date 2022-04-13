window.onload = () => {
  $('#btn_translate').click(translate);
  document.querySelector('#language_code').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      translate();
    }
  });
};

function translate () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  const valueLan = $('#language_code').val();
  $.get(url + valueLan, (data) => {
    $('#hello').html(data.hello);
  });
}
