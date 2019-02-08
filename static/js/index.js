// /**
//  * Created by shivam on 15-10-2018.
//  */


$(document).ready(function () {
//  $("#home_page").click(function() {
//     $('html,body').animate({
//         scrollTop: $(".header").offset().top},
//         'slow');
// });

   $("#about_us_page").click(function() {
       $('.content3').removeClass('add-margin-top');
       $('.content2').removeClass('add-margin-top');
    $('html,body').animate({
        scrollTop: $(".content1").offset().top},
        'slow');

    $('.content1').addClass('add-margin-top');
});

   $("#project_page").click(function() {
        $('.content1').removeClass('add-margin-top');
       $('.content3').removeClass('add-margin-top');
    $('html,body').animate({
        scrollTop: $(".content2").offset().top},
        'slow');
    $('.content2').addClass('add-margin-top');
});

   $("#contact_us_page").click(function() {
        $('.content1').removeClass('add-margin-top');
       $('.content2').removeClass('add-margin-top');
    $('html,body').animate({
        scrollTop: $(".content3").offset().top},
        'slow');
    // $('.content3').addClass('add-margin-top');
});
});

function home() {
    $("html, body").animate({ scrollTop: 0 }, "slow");
}

function contact_us() {
    var name = document.getElementById('name').value;
    if(name =='' || name==null){
        alert('Enter the Name');
        return false
    }
    var email = document.getElementById('email').value;
    if(email=='' || email==null){
        alert('Enter the Email');
        return false
    }
    var contact_no = document.getElementById('contact_no').value;
    var message = document.getElementById('message').value;
    if(message=='' || message==null){
        alert('Enter the Message');
        return false
    }
    else {
        $.ajax({
            url: '/contact_us/',
            type: 'POST',
            data: {'name': name, 'email': email, 'contact_no': contact_no, 'message': message},
            success: function (req) {
                if (req.success == true) {
                    alert(req.message);
                    document.getElementById('name').value = '';
                    document.getElementById('email').value = '';
                    document.getElementById('contact_no').value = '';
                    document.getElementById('message').value = '';
                }
                else {
                    alert(req.message);
                }
            }
        });
    }
}
