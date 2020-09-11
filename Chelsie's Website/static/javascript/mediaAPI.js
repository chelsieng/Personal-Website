//Displaying instagram feed
var request = new XMLHttpRequest();
request.open('GET', 'https://graph.instagram.com/me/media?fields=id,caption,media_url&access_token=IGQVJYWmh5dk82TUZACMDNEbnJraTF5d2JIVkhENFluN1VabmNsenBDWTZAtNXcyWWhCb0ZAPN3R6YXVPVTBGQnF4NEFlMVJqZAEpKeXBjeUt1TDFjRDBQaVUzVmZAkMlRNZAGlZAdTA4TkIxNHpfUUV0c3dDTQZDZD', true);

request.onload = function (container) {
    if (request.status >= 200 && request.status < 400) {
        // Success!
        let data = JSON.parse(request.responseText);
        for (let i = 0; i < 24; i++) {
            let container = document.getElementById('instafeed');
            let imgURL = data.data[i].media_url; //Getting ig post url
            let div = document.createElement('div');
            div.setAttribute('class', 'mb-3');
            container.appendChild(div); //<div class="container container-sm container-md container-lg"></div>
            let img = document.createElement('img');
            img.setAttribute('src', imgURL);
            img.setAttribute('class', 'img-fluid img-thumbnail')
            div.appendChild(img); //<img src="imgURL" class="img-fluid img-thumbnail" width="1080">
        }
    } else {
    }
};
request.onerror = function () {
    // There was a connection error of some sort
};
request.send();