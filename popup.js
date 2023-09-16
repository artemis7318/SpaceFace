document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("button1").addEventListener("click", function() {
        document.getElementById("button1").addEventListener("click", function() {
            alert("You passed the security check");
            var body = document.getElementsByTagName("body")[0].style.backgroundColor = "green";
        })
    }, false)
    document.getElementById("button2").addEventListener("click", function() {
        document.getElementById("button2").addEventListener("click", function() {
            chrome.tabs.create({url: "https://www.google.com/search?q=invader&oq=invader&aqs=chrome..69i57j0i271l2.790j0j1&sourceid=chrome&ie=UTF-8"});
            alert("You failed the security check");
            var body = document.getElementsByTagName("body")[0].style.backgroundColor = "red";
            // chrome.declarativeNetRequest.redirect("https://amazon.com");
        })
    }, false)
}), false;
