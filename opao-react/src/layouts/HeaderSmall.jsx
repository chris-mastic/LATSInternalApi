import React from 'react'
import '../../global.css'
import { Link } from 'react-router-dom'

function HeaderSmall() {
  return (
    <header className="w3-container-header w3-top w3-hide-large w3-black w3-xlarge ">
   
    <Link className="w3-button w3-black w3-margin-right" 
  onClick={()=>{w3_open()}} >☰</Link>
    <span>OPAO Change Order Batch</span>
  </header>
  )
}

export default HeaderSmall


  // Script to open and close sidebar
  function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
  }
   
  function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
  }
  
  // // Modal Image Gallery
  // function onClick(element) {
  //   document.getElementById("img01").src = element.src;
  //   document.getElementById("modal01").style.display = "block";
  //   var captionText = document.getElementById("caption");
  //   captionText.innerHTML = element.alt;
  // }
  
  // Modal Image Gallery
  function onClick(element) {
      document.getElementById("img01").src = element.src;
      document.getElementById("modal01").style.display = "block";
      var captionText = document.getElementById("caption");
      captionText.innerHTML = element.alt;
  }
