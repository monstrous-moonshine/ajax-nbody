$(document).ready(function () {
    let radius = 5.0e10;
    let animate = false;
    let id;
    let params = [ 
        [-3.5e10, 0.0e00, 0.0e00,  1.4e03, 3.0e28], 
        [-1.0e10, 0.0e00, 0.0e00,  1.4e04, 3.0e28], 
        [ 1.0e10, 0.0e00, 0.0e00, -1.4e04, 3.0e28], 
        [ 3.5e10, 0.0e00, 0.0e00, -1.4e03, 3.0e28]];
    let draw = function () {
        let canvas = $("#nbody")[0];
        let ctx = canvas.getContext("2d");
        let w = canvas.width;
        let h = canvas.height;
        ctx.clearRect(0, 0, w, h);
        for (body of params) {
            let x = w / 2 * (1 + body[0] / radius);
            let y = h / 2 * (1 - body[1] / radius);
            ctx.beginPath();
            ctx.arc(x, y, 10, 0, 2 * Math.PI);
            ctx.fill();
        }
    };
    draw();
    let update = function () {
        $.post(
            "nbody",
            {"params": params},
            function (data, status) {
                params = data["params"];
                draw();
            }
        );
    }
    $("button").click(function () {
        if (animate) {
            clearInterval(id);
            animate = false;
            $("button").text("Start");
        } else {
            id = setInterval(update, 15);
            animate = true;
            $("button").text("Stop");
        }
    });
});