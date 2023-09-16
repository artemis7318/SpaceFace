chrome.runtime.onInstalled.addListener(() => {
    console.log("Hello, World!");
});

chrome.contextMenus.create({
    id: "shopping", 
    title: "Search for:  \"%s\" on Amazon", 
    contexts: ["selection"],
})

chrome.contextMenus.onClicked.addListener(function(info, tab) {
    baseURL = "http://www.amazon.com/";
    var newURL = baseURL + info.selectionText;
    chrome.tabs.create({url: newURL});
})

chrome.runtime.onSuspend.addListener(function() {
    console.log("suspended");
})
