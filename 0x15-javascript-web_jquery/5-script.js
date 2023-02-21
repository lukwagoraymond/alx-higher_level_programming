/*
    Includes a new item to particular ul class
*/
$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
});