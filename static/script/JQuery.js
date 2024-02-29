document.addEventListener("DOMContentLoaded", function() {
    const getStartedButton = document.querySelector(".get-started-button");
    
    getStartedButton.addEventListener("click", function() {
        getStartedButton.style.marginLeft = "1000px";
        getStartedButton.style.opacity = "0";
    });
});
