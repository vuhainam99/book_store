import Cookies from 'js-cookie';
var token = "";
const obj = {};
    $(document).ready(function () {
        function login(user, password) {
            var settings = {
                url: "http://192.168.1.83:8000/api/v1/login/",
                method: "POST",
                timeout: 0,
                contentType: "application/json",
                dataType: "json",
                data: JSON.stringify({ email: user, password: password }),
            };

            $.ajax(settings).done(function (response) {
                var status = response.status;
                if (status == '201') {
                    obj = response.data;
                    console.log(obj);

                    Cookies.set("userId", "asdf")
                    Cookies.set("userName", "absd")
                    
                    // window.location.href = "./index-base.html";
                    status = null;
                } else {
                    alert("Hello! I am an alert box!");
                }
            });
        }

        $("#login").on("click", function () {
            console.log(token);
            // var user = $("#exampleInputEmail").value;
            var user = document.getElementById('exampleInputEmail').value;
            // var password = $("#exampleInputPassword").value;
            var password = document.getElementById('exampleInputPassword').value;
            login(user, password);
            
        });
    });
    $('#cl').on('click', function() {
        var myCookie = Cookies.get("userId");
        console.log(myCookie);
    })