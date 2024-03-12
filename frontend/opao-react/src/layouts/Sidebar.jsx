import React from 'react'
import '../../global.css'
import MenuItem from './MenuItem'
import {Link} from "react-router-dom"

function Sidebar({selected}) {
  console.log('sidebar')

  return (
  
  <nav
  className="w3-sidebar w3- w3-collapse w3-top w3-dark-green w3-large w3-padding"
  style={{ zIndex: 3, width: 300, fontWeight: "bold" }}
  id="mySidebar"
>
  <br />
  {/* <a
    href="javascript:void(0)"
    onClick={()=>{w3_close()}}
    className="w3-button w3-hide-large w3-display-topleft"
    style={{ width: "100%", fontSize: 22 }}
  >
    Close Menu
  </a> */}
  <Link className="w3-button w3-hide-large w3-display-topleft" 
  onClick={()=>{w3_close()}} 
  style={{ width: "100%", fontSize: 22,backgroundColor :'grey' }}>Close Menu</Link>
  
  <div className="w3-container">
    <h3 className="w3-padding-64">
      <b>
        Home side  bar created
        <br />
        Page
      </b>
    </h3>
  </div>
  <div className="w3-bar-block">

<MenuItem title='Home' href='/' selected = {selected}/>
<MenuItem title='Batch Fields' href='/batchfields' selected = {selected} />
<MenuItem title='Showcase' href='#showcase' selected = {selected}/>
<MenuItem title='Services' href='#services' selected = {selected}/>
<MenuItem title='Designers' href='#designers' selected = {selected} />
<MenuItem title='Contact' href='#contact' selected = {selected} />
<MenuItem title='Batch Add' href='/batchadd' selected = {selected}/>
<MenuItem title='Batch Submit' href='/batchsubmit' selected = {selected}/>
<MenuItem title='Batch Status' href='/batchstatus' selected = {selected}/>


  </div>
</nav>
  )
}

export default Sidebar




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
  