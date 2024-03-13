import React,{useContext, useState} from 'react'
import { Text } from 'react-native-web'
import * as Animatable from 'react-native-animatable'
import './global.css'
import Sidebar from '../layouts/Sidebar'
import Header from '../layouts/Header'
import HeaderSmall from '../layouts/HeaderSmall'
import Select from 'react-dropdown-select'
import {Context as AuthContext} from '../contexts/AuthContext'
import { jurOptions } from '../data/jurOptions'
import { taxyearOptions } from '../data/taxyearOptions'


import './BatchAdd.css'

function Jurisdiction() {
  // const {state,changeJurisdiction} = useContext(JurisdictionContext);
  const {state : authState, changeJur, changeTaxYear} = useContext(AuthContext);

  const [item, setItem] = useState({ value: authState.jur, label: `JUR = ${authState.jur}`});

  const handleJurChange = (e) => { 
    console.log('value of e is === ' + JSON.stringify(e))
    // setItem(e[0].value); changeJurisdiction(e[0].value)}
    setItem(e[0].value); changeJur(e[0].value)}

  const handleTaxYearChange = (e) => { 
      console.log('value of e is === ' + JSON.stringify(e))
      // setItem(e[0].value); changeJurisdiction(e[0].value)}
      setItem(e[0].value); changeTaxYear(e[0].value)}


  console.log("tax year options", JSON.stringify(taxyearOptions));

  
  return (

<>
  <title>W3.CSS Template</title>
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
  {/* header with logo*/}

 <Header />

<Sidebar selected='Batch Fields' />
<HeaderSmall />
  {/* Top menu on small screens */}
 

  {/* Overlay effect when opening sidebar on small screens */}
  <div
    className="w3-overlay w3-hide-large"
    onClick={()=>{w3_close()}}
    style={{ cursor: "pointer" }}
    title="close side menu"
    id="myOverlay"
  />



  {/* !PAGE CONTENT! */}
  <div className="w3-main" style={{ marginLeft: 340, marginRight: 40 }}>

  <Animatable.View animation='slideInRight' duration={1000}>

    {/* Header */}
    <div className="w3-container" style={{ marginTop: 80 }} id="showcase">
     
      <h1 className="w3-xxxlarge w3-text-black">
        <b>Change Jurisdiction</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid black" }} className="w3-round" />
    </div>
    {/* Photo grid (modal) */}
    <div className="w3-row-padding">

    <Select options={jurOptions} 
    placeholder="Select or type jurisdiction"

     onChange={(e) => handleJurChange(e)} />;

<Select options={taxyearOptions} 
placeholder="Select or type tax year"
     onChange={(e) => handleTaxYearChange(e)} />;

    </div>
    <h1>the values of new option is {item.value}</h1>
    <Text>the values of new option is  
      {(item.label)}</Text>
      {(new Date().getFullYear()) + 1}
      <Text>{JSON.stringify(taxyearOptions)}</Text>

    {/* Modal for full size images on click*/}
























 
    {/* The Team */}
    
    {/* End page content */}

    </Animatable.View>

  </div>
  {/* W3.CSS Container */}
</>

  )
}



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


  
  export default Jurisdiction

