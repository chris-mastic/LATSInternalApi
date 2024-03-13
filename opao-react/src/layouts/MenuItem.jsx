import React,{useState} from 'react'
import '../../global.css'
import { Link } from 'react-router-dom'

function MenuItem({title, href, selected}) {
  return (
  //   <a
  //   href={href}
  //   onClick={()=>{w3_close()}}
  //   className="w3-bar-item w3-button w3-hover-white"
  //   style={selected === title ? {backgroundColor: 'grey'}: {}}
  // >
  //   {title}
  // </a>
  <Link className="w3-bar-item w3-button w3-hover-white" 
  to={href} onClick={()=>{w3_close()}} 
  style={selected === title ? {backgroundColor: 'grey'}: {}}>{title}</Link>
  )
}

export default MenuItem



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
    