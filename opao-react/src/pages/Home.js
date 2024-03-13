import React,{useContext, useState} from 'react'
import {View} from 'react-native'
import * as Animatable from 'react-native-animatable'
import './global.css'
import Sidebar from '../layouts/Sidebar'
import Header from '../layouts/Header'
import HeaderSmall from '../layouts/HeaderSmall'

function Home() {
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

<Sidebar selected='Home' />
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
      <h1 className="w3-jumbo">
        <b>Home Website</b>
      </h1>
      <h1 className="w3-xxxlarge w3-text-red">
        <b>Page.</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
    </div>
    {/* Photo grid (modal) */}
    <div className="w3-row-padding">
      <div className="w3-half">
        <img
          src="https://www.w3schools.com/w3images/kitchenconcrete.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="Concrete meets bricks"
        />
        <img
          src="https://www.w3schools.com/w3images/livingroom.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="Light, white and tight scandinavian design"
        />
        <img
          src="https://www.w3schools.com/w3images/diningroom.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="White walls with designer chairs"
        />
      </div>
      <div className="w3-half">
        <img
          src="https://www.w3schools.com/w3images/atrium.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="Windows for the atrium"
        />
        <img
          src="https://www.w3schools.com/w3images/bedroom.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="Bedroom and office in one space"
        />
        <img
          src="https://www.w3schools.com/w3images/livingroom2.jpg"
          style={{ width: "100%" }}
          onClick={()=>{onClick(this)}}
          alt="Scandinavian design"
        />
      </div>
    </div>
    {/* Modal for full size images on click*/}
    <div
      id="modal01"
      className="w3-modal w3-black"
      style={{ paddingTop: 0 }}
    //   onClick="this.style.display='none'"
      onClick={()=>{alert('pressed')}}

    >
      <span className="w3-button w3-black w3-xxlarge w3-display-topright">
        ×
      </span>
      <div className="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
        <img id="img01" className="w3-image" />
        <p id="caption" />
      </div>
    </div>
    {/* Services */}
    <div className="w3-container" id="services" style={{ marginTop: 75 }}>
      <h1 className="w3-xxxlarge w3-text-red">
        <b>Services.</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
      <p>
        We are a interior design service that focus on what's best for your home
        and what's best for you!
      </p>
      <p>
        Some text about our services - what we do and what we offer. We are
        lorem ipsum consectetur adipiscing elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
        id est laborum consectetur adipiscing elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat.
      </p>
    </div>
    {/* Designers */}
    <div className="w3-container" id="designers" style={{ marginTop: 75 }}>
      <h1 className="w3-xxxlarge w3-text-red">
        <b>Designers.</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
      <p>The best team in the world.</p>
      <p>
        We are lorem ipsum consectetur adipiscing elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
        id est laborum consectetur adipiscing elit, sed do eiusmod tempor
        incididunt ut labore et quis nostrud exercitation ullamco laboris nisi
        ut aliquip ex ea commodo consequat.
      </p>
      <p>
        <b>Our designers are thoughtfully chosen</b>:
      </p>
    </div>
    {/* The Team */}
    <div className="w3-row-padding w3-grayscale">
      <div className="w3-col m4 w3-margin-bottom">
        <div className="w3-light-grey">
          <img src="https://www.w3schools.com/w3images/team2.jpg" alt="John" style={{ width: "100%" }} />
          <div className="w3-container">
            <h3>John Doe</h3>
            <p className="w3-opacity">CEO &amp; Founder</p>
            <p>
              Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse
              sodales pellentesque elementum.
            </p>
          </div>
        </div>
      </div>
      <div className="w3-col m4 w3-margin-bottom">
        <div className="w3-light-grey">
          <img src="https://www.w3schools.com/w3images/team1.jpg" alt="Jane" style={{ width: "100%" }} />
          <div className="w3-container">
            <h3>Jane Doe</h3>
            <p className="w3-opacity">Designer</p>
            <p>
              Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse
              sodales pellentesque elementum.
            </p>
          </div>
        </div>
      </div>
      <div className="w3-col m4 w3-margin-bottom">
        <div className="w3-light-grey">
          <img src="https://www.w3schools.com/w3images/team3.jpg" alt="Mike" style={{ width: "100%" }} />
          <div className="w3-container">
            <h3>Mike Ross</h3>
            <p className="w3-opacity">Architect</p>
            <p>
              Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse
              sodales pellentesque elementum.
            </p>
          </div>
        </div>
      </div>
    </div>
    {/* Packages / Pricing Tables */}
    <div className="w3-container" id="packages" style={{ marginTop: 75 }}>
      <h1 className="w3-xxxlarge w3-text-red">
        <b>Packages.</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
      <p>
        Some text our prices. Lorem ipsum consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
        ex ea commodo consequat. Duis aute irure
      </p>
    </div>
    <div className="w3-row-padding">
      <div className="w3-half w3-margin-bottom">
        <ul className="w3-ul w3-light-grey w3-center">
          <li className="w3-dark-grey w3-xlarge w3-padding-32">Basic</li>
          <li className="w3-padding-16">Floorplanning</li>
          <li className="w3-padding-16">10 hours support</li>
          <li className="w3-padding-16">Photography</li>
          <li className="w3-padding-16">20% furniture discount</li>
          <li className="w3-padding-16">Good deals</li>
          <li className="w3-padding-16">
            <h2>$ 199</h2>
            <span className="w3-opacity">per room</span>
          </li>
          <li className="w3-light-grey w3-padding-24">
            <button className="w3-button w3-white w3-padding-large w3-hover-black">
              Sign Up
            </button>
          </li>
        </ul>
      </div>
      <div className="w3-half">
        <ul className="w3-ul w3-light-grey w3-center">
          <li className="w3-red w3-xlarge w3-padding-32">Pro</li>
          <li className="w3-padding-16">Floorplanning</li>
          <li className="w3-padding-16">50 hours support</li>
          <li className="w3-padding-16">Photography</li>
          <li className="w3-padding-16">50% furniture discount</li>
          <li className="w3-padding-16">GREAT deals</li>
          <li className="w3-padding-16">
            <h2>$ 249</h2>
            <span className="w3-opacity">per room</span>
          </li>
          <li className="w3-light-grey w3-padding-24">
            <button className="w3-button w3-red w3-padding-large w3-hover-black">
              Sign Up
            </button>
          </li>
        </ul>
      </div>
    </div>
    {/* Contact */}
    <div className="w3-container" id="contact" style={{ marginTop: 75 }}>
      <h1 className="w3-xxxlarge w3-text-red">
        <b>Contact.</b>
      </h1>
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
      <p>
        Do you want us to style your home? Fill out the form and fill me in with
        the details :) We love meeting new people!
      </p>
      <form action="/action_page.php" target="_blank">
        <div className="w3-section">
          <label>Name</label>
          <input
            className="w3-input w3-border"
            type="text"
            name="Name"
            required=""
          />
        </div>
        <div className="w3-section">
          <label>Email</label>
          <input
            className="w3-input w3-border"
            type="text"
            name="Email"
            required=""
          />
        </div>
        <div className="w3-section">
          <label>Message</label>
          <input
            className="w3-input w3-border"
            type="text"
            name="Message"
            required=""
          />
        </div>
        <button
          type="submit"
          className="w3-button w3-block w3-padding-large w3-red w3-margin-bottom"
        >
          Send Message
        </button>
      </form>
    </div>
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
  
  export default Home


  
  // <Animatable.View animation='fadeInUpBig' style={styles.footer}>
  //     <Text style={styles.title}>Start Change Orders</Text>
  //     <Text style={styles.text}>Start Processing Change Orders with Ease</Text>
  //     <TouchableOpacity style={styles.signIn} onPress={()=> navigate('signin') }>
  //         <Text style={styles.textSign}>Get Started</Text>
  //         <MaterialIcons name='navigate-next'
  //             color='white'
  //             size={20} />
  //     </TouchableOpacity>
  // </Animatable.View>
