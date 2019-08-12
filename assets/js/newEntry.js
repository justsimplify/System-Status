$(document).ready(function () {
    function postRequest(link, data, callback) {
        Vue.http.post(link, data).then(function (response) {
            callback(response.data);
        }, function (error) {
            console.log(error.statusText);
        });
    }

    $(".newEntry").on("submit", function(e) {
        data = {
            "name": $(".name").val(),
            "description": $(".description").val(),
            "pingUrl": $(".pingUrl").val().split("http://").filter((item, p, s) => item != "").join("").split("https://").filter((item, p, s) => item != "").join(""),
            "waitTime": parseInt($(".waitTime").val()),
            "interval": parseInt($(".interval").val())
        };
        postRequest("/service/", data, function(d) {
            console.log(d);
        });
    });
});