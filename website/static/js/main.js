function myFunction() {
    document.querySelector(".authentication").style.display = "block";
};

function semiFunction() {
    document.querySelector(".login").style.display = "block";
    document.querySelector(".signup").style.display = "none";
    document.querySelector(".change1").style.color= "rgb(109, 109, 109)";
    document.querySelector(".change2").style.color= "black";
};


function changeFunction() {
    document.querySelector(".signup").style.display = "block";
    document.querySelector(".login").style.display = "none";
    document.querySelector(".change2").style.color= "rgb(109, 109, 109)";
    document.querySelector(".change1").style.color= "black";
};

function autCloseFunc(){
    document.querySelector(".authentication").style.display = "none";
}
