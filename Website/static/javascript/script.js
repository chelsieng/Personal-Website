//Validating email from contact.html
function validateEmail() {
    const email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const email_input = document.getElementById("email");
    email_input.value = email_input.value.trim(); //removing space
    //email is valid
    if (email_regex.test(email_input.value)) {
        email_input.className = "form-control is-valid"; //valid feedback
        document.getElementById("submit").disabled = false; //enable button

    } else {
        email_input.className = "form-control is-invalid"; //invalid feedback
    }
}

//Validating password from signup.html
function validatePassword() {
    //At least 6 character, 1 lower case, 1 upper case and 1 digit
    const pwd_regex = /^(?=.*[A-z])(?=.*[A-Z])(?=.*[0-9])\S{6,}$/;
    const pwd_input1 = document.getElementById("signup_pwd1");
    pwd_input1.value = pwd_input1.value.trim(); //removing space
    // Password is valid
    if (pwd_regex.test(pwd_input1.value)) {
        pwd_input1.className = "form-control is-valid"; //valid feedback
    } else {
        pwd_input1.className = "form-control is-invalid"; //invalid feedback
    }
    pwdEquals();
}

//Validating equality of passwords from signup.html
function pwdEquals() {
    const pwd_regex = /^(?=.*[A-z])(?=.*[A-Z])(?=.*[0-9])\S{6,}$/;
    const pwd_input1 = document.getElementById("signup_pwd1");
    const pwd_input2 = document.getElementById("signup_pwd2");
    pwd_input1.value = pwd_input1.value.trim(); //removing space
    pwd_input2.value = pwd_input2.value.trim(); //removing space
    // Confirming both passwords
    if ((pwd_input1.value === pwd_input2.value)) {
        pwd_input2.className = "form-control is-valid"; //valid feedback
        if (pwd_regex.test(pwd_input2.value)) {
            document.getElementById("submitSignUp").disabled = false; //enable button
        }
    } else {
        pwd_input2.className = "form-control is-invalid"; //invalid feedback
    }
}

//Validating post from justForFun.html
function validatePost() {
    const post_regex = /^\b(\w*never have i ever\w*)\b/i; // should start with never have i ever
    const post = document.getElementById("write");
    var text = post.value.trim();
    //Post is valid
    if (post_regex.test(text)) {
        post.className = "form-control is-valid"; //valid feedback
        document.getElementById("post").disabled = false; //enable button
    } else {
        post.className = "form-control is-invalid"; //invalid feedback
    }
}

//Prompting user to log in from justForFun.html
//When user not in session
function promptLogIn() {
    have = document.getElementById("have");
    have_not = document.getElementById("have_not");
    post = document.getElementById("Post");
    // aler box pops up and prompts user to log in
    if (have.value == "I Have") {
        window.alert("Haha, don't forget to log in!");
    }
    if (have_not.value == "I Have Not") {
        window.alert("Haha, don't forget to log in!");
    }
    if (post.value == "Post") {
        window.alert("Haha, don't forget to log in!");
    }
}


