import React from 'react'
import { View } from 'react-native'
import '../../../w3.css'

function BatchAdd() {
  return (
    <>
 



    <meta charSet="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Poppins"
    />
    <style
      dangerouslySetInnerHTML={{
        __html:
          '\nbody,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}\nbody {font-size:16px;}\n.w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}\n.w3-half img:hover{opacity:1}\n'
      }}
    />

  
    {/* Sidebar/menu */}
    <nav
      className="w3-sidebar w3-dark-green w3-collapse w3-top w3-large w3-padding"
      style={{ zIndex: 3, width: 300, fontWeight: "bold" }}
      id="mySidebar"
    >
      <br />
      <a
        href="javascript:void(0)"
        onClick={()=>{w3_close()}}
        className="w3-button w3-hide-large w3-display-topleft"
        style={{ width: "100%", fontSize: 22 }}
      >
        Close Menu
      </a>
      <div className="w3-container">
        <h3 className="w3-padding-64">
          <b>
            Company
            <br />
            Name
          </b>
        </h3>
      </div>
      <div className="w3-bar-block">
        <a
          href="#"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Home
        </a>
        <a
          href="#showcase"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Showcase
        </a>
        <a
          href="#services"
          onClick={()=>{()=>{w3_close()}}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Services
        </a>
        <a
          href="#designers"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Designers
        </a>
        <a
          href="#packages"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Packages
        </a>
        <a
          href="#contact"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Contact
        </a>
        <a
          href="/batchadd"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Batch Add
        </a>
        <a
          href="/batchstatus"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Batch Status
        </a>
        <a
          href="/batchsubmit"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Batch Submit
        </a>
        <a
          href="/dashboard"
          onClick={()=>{w3_close()}}
          className="w3-bar-item w3-button w3-hover-white"
        >
          Dashboard
        </a>
      </div>
    </nav>
    {/* Top menu on small screens */}
    <header className="w3-container w3-top w3-hide-large w3-red w3-xlarge w3-padding">
      <a
        href="javascript:void(0)"
        className="w3-button w3-red w3-margin-right"
        onClick={()=>{w3_open()}}
      >
        ☰
      </a>
      <span>Company Name</span>
    </header>
    {/* Overlay effect when opening sidebar on small screens */}
    <div
      className="w3-overlay w3-hide-large"
      onClick={()=>{w3_close()}}
      style={{ cursor: "pointer" }}
      title="close side menu"
      id="myOverlay"
    />
    {/* !PAGE CONTENT! */}

     
   
  </>
  


  )
}

function w3_open() {

  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;

}

export default BatchAdd

