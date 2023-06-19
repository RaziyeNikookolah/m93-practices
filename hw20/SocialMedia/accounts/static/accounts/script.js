$(document).ready(function() {
  $('tbody tr').each(function() {
    var href = '/user_details/{{id}}/' + $(this).find('td:first').text();
    $(this).wrap('<a href="' + href + '"></a>');
  });
});