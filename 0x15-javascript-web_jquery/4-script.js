$('#toggle_header').click(toggle)

function toggle(){
    if ($('header').hasClass('red')) {
        $('header').css('color', 'green');
        $('header').removeClass('red').addClass('green');
    }else{
        $('header').css('color', 'red');
        $('header').removeClass('green').addClass('red');
    }
}
