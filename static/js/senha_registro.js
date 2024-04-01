function togglePasswordsVisibility() {
    var password1 = document.getElementById('password1');
    var password2 = document.getElementById('password2');

    if (password1.type === "password") {
        password1.type = "text";
        password2.type = "text";
    } else {
        password1.type = "password";
        password2.type = "password";
    }
}
