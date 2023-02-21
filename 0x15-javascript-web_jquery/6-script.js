/*
    Updates the text of the <header> element to 'New Header!
    when user clicks on DIV#update_header
*/
$('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
});