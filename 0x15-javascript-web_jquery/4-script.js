/*
    toggles the class of the HTML tag HEADER to red
    or green when the user clicks on the tag
    DIV#toggle_header
*/
$('DIV#toggle_header').click(function () {
    $('HEADER').toggleClass('green red');
});