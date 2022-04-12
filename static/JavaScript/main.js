const texts = ["Find answers of your doubts"]
let count=0;
let index=0;
let currenttext="";
let letter="";

(function type(){

    if (count === texts.length){
        count=0;
    }
    currenttext=texts[count]
    letter = currenttext.slice(0,++index);

    document.querySelector('.typing').textContent = letter;
    if(letter.length === currenttext.length){

        index=0;
    }
    setTimeout(type,125);
})();

window.onload= function (){
     document.getElementById("transparent-container").style.color="white";
     document.getElementById("transparent-container").style.transform="scale(1.1)";
     document.getElementById("transparent-container").style.transition="2s";
}
var Image_Id = document.getElementById("changeimg");
function change1() {
  Image_Id.src = "https://telegra.ph/file/2eaf44c648b4d41108682.png";
}
function change2() {
  Image_Id.src = "https://telegra.ph/file/48600d0fd95914f6c9a4e.png";
}
function change3() {
  Image_Id.src = "https://telegra.ph/file/8df378cb7aa15159686c2.png";
}
function change4() {
  Image_Id.src = "https://telegra.ph/file/6d77e78c84ad15a42f9e1.png";
}
function change5() {
  Image_Id.src = "https://telegra.ph/file/5ce7df0a05195b92c8ece.png";
}
function change6() {
  Image_Id.src = "https://telegra.ph/file/e1d3dadf20e09ed2d474e.png";
}  

let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

// menu bar js
/*  
var open = false;

function Drop(n) {
  var i;
  if (open == false) {
    for (i = n; i < 5; i++) {
      Drp(i)
    }
    open = true
  } else if (open == true) {
    for (i = n; i < 5; i++) {
      Cls(i)
    }
    open = false
  }
}

function Drp(n) {
  var elem = document.getElementsByClassName("menu-con")[n];
  var pos = -1 * window.innerHeight - n * 100;
  var id = setInterval(frame, 5);

  function frame() {
    if (pos >= -10) {
      clearInterval(id);
      elem.style.top = 0 + 'px';
    } else {
      pos += 10;
      elem.style.top = pos + 'px';
    }
  }
}

function Cls(n) {
  var elems = document.getElementsByClassName("menu-con")[n];
  var poss = 0;
  var ids = setInterval(frames, 5);

  function frames() {
    if (poss <= -1 * window.innerHeight) {
      clearInterval(ids);
      elems.style.top = -1 * window.innerHeight + 'px';
    } else {
      poss += -7 - n * 2;
      elems.style.top = poss + 'px';
    }
  }
}
*/


