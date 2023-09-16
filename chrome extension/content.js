document.body.style.backgroundColor = 'white';
console.log("CONTENT");

chrome.runtime.sendMessage({greeting: "hello"}, function(response) {
    console.log(response.farewell);
})