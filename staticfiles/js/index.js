var toggle = document.getElementById("toggle");
var menu = document.getElementById("hidden-menu");
console.log(toggle);

function change(){
    if (menu.style.display == "flex"){
        menu.style.display = "none"
    }
    else{
        menu.style.display = "flex"
    }
}

function copyToClipboard() {
    const text = document.getElementById("text").innerText;
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    // Change button text to "Copied!" for 2 seconds
    const button = document.querySelector("button");
    button.innerText = "Copied!";
    setTimeout(() => {
        button.innerText = "Copy Text";
    }, 2000);
}