$(document).ready(function() {

    //curMonImage = document.getElementById("curMonImage");
    //curOppImage = document.getElementById("curOppImage");

    var c = document.getElementById("cvsGame");
    ctx = c.getContext("2d");

    ctx.canvas.width = $("#mws-explore-area").innerWidth();
    ctx.canvas.height = $("#mws-explore-area").innerHeight();

    cvsWidth = Math.floor(ctx.canvas.width / 16 + 1) * 16;
    cvsHeight = Math.floor(ctx.canvas.height / 16 + 1) * 16;

    if (cvsWidth > 1024) {
        cvsWidth = 1024;
    }
});