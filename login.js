$(document).ready(function(){
    $('#login').submit(function(event){
        event.preventDefault();
        const email = $('#email').val();
        const pwd = $('#pwd').val();
        if (email === 'nhathuyle22@gmail.com' && pwd === '123456'){
            alert('Logged in successfully!');
            window.location.href='home.html';
        }
        else{
            alert('Login error!');
        }
    });
});