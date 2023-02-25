$(document).ready(() => {
    $('INPUT#btn_translate').click(function(){
        const langCode = $('INPUT#language_code').val();
        const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
        $.get(url, function(data, textStatus) {
            console.log(url, data, textStatus);
            if(data.code !== 'none') {
                $('DIV#hello').text(data.hello);
            } else {
                $('DIV#hello').text(data.hello);
            }
        });
    });
});