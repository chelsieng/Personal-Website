//Validating email from contact.html
function validateEmail() {
    const email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const email_input = document.getElementById("email");
    email_input.value = email_input.value.trim();
    if (email_regex.test(email_input.value)) {
        email_input.className = "form-control is-valid";
        document.getElementById("submit").disabled = false;

    } else {
        email_input.className = "form-control is-invalid";
    }
}

//Validating password from signup.html
function validatePassword() {
    //At least 6 character, 1 lower case, 1 upper case and 1 digit
    const pwd_regex = /^(?=.*[A-z])(?=.*[A-Z])(?=.*[0-9])\S{6,}$/;
    const pwd_input1 = document.getElementById("signup_pwd1");
    pwd_input1.value = pwd_input1.value.trim();
    if (pwd_regex.test(pwd_input1.value)) {
        pwd_input1.className = "form-control is-valid";
    } else {
        pwd_input1.className = "form-control is-invalid";
    }
    pwdEquals();
}

//Validating equality of passwords from signup.html
function pwdEquals() {
    const pwd_regex = /^(?=.*[A-z])(?=.*[A-Z])(?=.*[0-9])\S{6,}$/;
    const pwd_input1 = document.getElementById("signup_pwd1");
    const pwd_input2 = document.getElementById("signup_pwd2");
    pwd_input1.value = pwd_input1.value.trim();
    pwd_input2.value = pwd_input2.value.trim();
    if ((pwd_input1.value === pwd_input2.value)) {
        pwd_input2.className = "form-control is-valid";
        if (pwd_regex.test(pwd_input2.value)) {
            document.getElementById("submitSignUp").disabled = false;
        }
    } else {
        pwd_input2.className = "form-control is-invalid";
    }
}

//Validating post from justForFun.html
function validatePost() {
    const post_regex =/^\b(\w*never have i ever\w*)\b/i;
    const post = document.getElementById("write");
    post.value = post.value.trim();
    console.log(post.value)
    if (post_regex.test(post.value)) {
        post.className = "form-control is-valid";
        document.getElementById("post").disabled = false;
    } else {
        post.className = "form-control is-invalid";
    }
}



