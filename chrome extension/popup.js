document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("button1").addEventListener("click", function() {
        document.getElementById("button1").addEventListener("click", function() {
            alert("You passed the security check");
            var body = document.getElementsByTagName("body")[0].style.backgroundColor = "green";
        })
    }, false)
    document.getElementById("button2").addEventListener("click", function() {
        document.getElementById("button2").addEventListener("click", function() {
            alert("You failed the security check");
            var body = document.getElementsByTagName("body")[0].style.backgroundColor = "red";
        })
    }, false)
}), false;
