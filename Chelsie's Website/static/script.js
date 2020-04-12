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

//Displaying instagram feed
var request = new XMLHttpRequest();
request.open('GET', 'https://graph.instagram.com/me/media?fields=id,caption,media_url&access_token=IGQVJVbU1OVTdpeUJlRUpQX2hIYldFTXZAfMmdQWDAydW0tbTF4R3Q0UHNuSHJnbkVWY1dRUW5rMGFiN0ZAObWw4dk45Y2kwU3N0MW9pS2U0M3RIdFoxbnFtMjFpa3VFX1JHR2p6YWRB', true);

request.onload = function (container) {
    if (request.status >= 200 && request.status < 400) {
        // Success!
        let data = JSON.parse(request.responseText);
        for (let i = 0; i < data.data.length; i++) {
            let container = document.getElementById('instafeed');
            let imgURL = data.data[i].media_url;
            let div = document.createElement('div');
            div.setAttribute('class', 'container container-sm container-md container-lg');
            container.appendChild(div);
            let img = document.createElement('img');
            img.setAttribute('src', imgURL);
            img.setAttribute('class', 'img-fluid img-thumbnail')
            img.setAttribute('width', '1080')
            div.appendChild(img);
        }
    } else {
    }
};
request.onerror = function () {
    // There was a connection error of some sort
};
request.send();

//Displaying github repositories
var requestGithub = new XMLHttpRequest();
requestGithub.open('GET', 'https://api.github.com/users/chelsieng/repos', true);

requestGithub.onload = function (container) {
    if (requestGithub.status >= 200 && requestGithub.status < 400) {
        // Success!
        let data = JSON.parse(requestGithub.responseText);
        // console.log(data);
        for (let i = 0; i < dataM
            .length; i++) {
            let repoName = data[i].name;
            let repoDescription = data[i].description;
            let repoLang = data[i].language;
            let repoUpdate = data[i].updated_at;
            let container = document.getElementById('user-repositories')
            let div = document.createElement('div');
            div.setAttribute('class', 'display-4');
            div.appendChild(repoName);
            // div.appendChild(repoName);
            // let p = document.createElement('p');
            // p.appendChild(repoDescription);
            // let h6 = document.createElement('h6');
            // h6.appendChild(repoLang);
            // h6.appendChild(repoUpdate);
            // let repoURL = data.data[i].html_url;
            // console.log(repoURL);
            // let div = document.createElement('div');
            // div.setAttribute('class', 'container container-sm container-md container-lg');
            // container.appendChild(div);
            // let img = document.createElement('img');
            // img.setAttribute('src', imgURL);
            // img.setAttribute('class', 'img-fluid img-thumbnail')
            // img.setAttribute('width', '1080')
            // div.appendChild(img);
        }
    } else {
    }
};

requestGithub.onerror = function () {
    // There was a connection error of some sort
};
requestGithub.send();


