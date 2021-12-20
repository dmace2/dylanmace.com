// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("navbar");
console.log(header);

// Get the offset position of the navbar
var sticky = header.offsetTop;
// console.log(sticky);

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  console.log("scrolling");
  if (window.pageYOffset > sticky) {
    console.log(window.pageYOffset);
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}