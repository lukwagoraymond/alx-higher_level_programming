/*
    updates text color of the HTML tag HEADER to red
    when user clicks on the tag DIV#red_header
*/
$('DIV#red_header').click(function () {
    $('HEADER').css('color', '#FF0000');
});