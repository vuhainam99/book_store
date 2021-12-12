function getCategory() {
    var postApi = 'http://192.168.1.83:8000/api/v1/list_geres/'
    fetch(postApi)
        .then(function (response) {
            return response.json();
            // JSON.parse: JSON -> Js types
        })
        .then(function (posts) {

            datas = posts.data;
            console.log('h');
            console.log(datas)
            const queryString = window.location.search;
            console.log(queryString);
            const urlParams = new URLSearchParams(queryString);
            const username = urlParams.get('username');
            const userid = urlParams.get('userid');
            console.log(username);
            document.getElementById("get--username").innerHTML = username;


            html = '';
            var htmls = datas.map(function (data, index) {
                html += '<li><a href="#">s</a></li>';
           
                return html;
            });

            // var html = htmls.join('');
            document.getElementById('product--list').innerHTML = html;
        })
}
getData();