//Displaying instagram feed
var request = new XMLHttpRequest();
request.open('GET', 'https://graph.instagram.com/me/media?fields=id,caption,media_url&access_token=IGQVJVbU1OVTdpeUJlRUpQX2hIYldFTXZAfMmdQWDAydW0tbTF4R3Q0UHNuSHJnbkVWY1dRUW5rMGFiN0ZAObWw4dk45Y2kwU3N0MW9pS2U0M3RIdFoxbnFtMjFpa3VFX1JHR2p6YWRB', true);

request.onload = function (container) {
    if (request.status >= 200 && request.status < 400) {
        // Success!
        let data = JSON.parse(request.responseText);
        for (let i = 0; i < data.data.length; i++) {
            let container = document.getElementById('instafeed');
            let imgURL = data.data[i].media_url; //Getting ig post url
            let div = document.createElement('div');
            div.setAttribute('class', 'container container-sm container-md container-lg');
            container.appendChild(div); //<div class="container container-sm container-md container-lg"></div>
            let img = document.createElement('img');
            img.setAttribute('src', imgURL);
            img.setAttribute('class', 'img-fluid img-thumbnail')
            img.setAttribute('width', '1080')
            div.appendChild(img); //<img src="imgURL" class="img-fluid img-thumbnail" width="1080">
        }
    } else {
    }
};
request.onerror = function () {
    // There was a connection error of some sort
};
request.send();