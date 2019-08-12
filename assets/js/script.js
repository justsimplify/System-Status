$(document).ready(function () {
    function getRequest(link, callback) {
        Vue.http.get(link).then(function (response) {
            callback(response.data);
            return response.data;
        }, function (error) {
            console.log(error.statusText);
        });
    }

    function checkStatusOfUrl(pk, callback) {
        getRequest(`/service/produce_data/${pk}/`, function (v) {
            console.log(v);
            callback(pk);
        });
    }

    function initInterval(d) {
        let interval = d.interval;
        let pk = d.pk;

        setInterval(function () {
            checkStatusOfUrl(pk, function (data) {
                console.log(data);
                getRequest(`/service/getData/${data}`, function (d) {
                    c = `.${data}`;
                    console.log($(c).find(".status").text());
                    $(c).find(".status").text(d.status ? "Up" : "Down");
                });
            });
        }, interval * 1000);
    }

    function replaceElementValue(ele, value) {
        var app = new Vue({
            el: ele,
            data: {
                message: value
            }
        });
    }

    getRequest("/service/getData/", function (data) {
        data.forEach((d) => {
            initInterval(d);
        });
        replaceElementValue("#vals", data);
    });
});