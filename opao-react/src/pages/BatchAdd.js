import React,{useContext, useState} from 'react'
import {Button, View, ScrollView,Text} from 'react-native'
import {Button as x,Text as T} from 'react-native-paper'
import Select from 'react-dropdown-select'
import * as Animatable from 'react-native-animatable'
import './global.css'
import Sidebar from '../layouts/Sidebar'
import Header from '../layouts/Header'
import HeaderSmall from '../layouts/HeaderSmall'
import './BatchAdd.css'
import {Context} from '../contexts/AuthContext'
import { jurOptions } from '../data/jurOptions'
import { taxyearOptions } from '../data/taxyearOptions'
import * as XLSX from "xlsx";
import ExcelToJsonConverter from '../components/ExcelToJSONConverter'


function BatchAdd() {
  const {state,changeJur, changeTaxYear} = useContext(Context);
  const [parid, setParid]= useState("");
  const [jur,setJur] = useState(state.jur);
  const [taxyear,setTaxYear] = useState(state.taxyear);
  const [showBatchField, setShowBatchField ]= useState({showTaxYear : false, showJur : false});
  const [data, setData] = useState([]);
  const [isMutipleActive, setIsMultipleActive] = useState(false);

  const handleFileUpload = (e) => {
    const reader = new FileReader();
    reader.readAsBinaryString(e.target.files[0]);
    reader.onload = (e) => {
      const data = e.target.result;
      const workbook = XLSX.read(data, { type: "binary" });
      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];
      const parsedData = XLSX.utils.sheet_to_json(sheet);
      setData(parsedData);
    };
  }

  const changeParidHandler = (e) => {
    setParid(e.target.value)

  }

  const handleJurChange = (e) => { 
    console.log('value of e is === ' + JSON.stringify(e))
    // setItem(e[0].value); changeJurisdiction(e[0].value)}
    console.log('value of jur is === ' + jur)

    changeJur(e[0].value);setJur(e[0].value); 
    setShowBatchField({...showBatchField,showJur: false, showTaxYear : false})
  }

  const handleTaxYearChange = (e) => { 
      console.log('value of e is === ' + JSON.stringify(e))
      // setItem(e[0].value); changeJurisdiction(e[0].value)}
      console.log('value of taxyear is === ' + taxyear)

       setTaxYear(e[0].value);changeTaxYear(e[0].value);
       setShowBatchField({...showBatchField,showJur: false, showTaxYear : false})
      }
      

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
  {/* header with logo*/}

 <Header />

<Sidebar selected='Batch Add' />
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
      {/* <h1 className="w3-xxxlarge w3-text-red">
        <b>Page.</b>
      </h1> */}
      <hr style={{ width: 50, border: "5px solid red" }} className="w3-round" />
    </div>
    
    <h2>Select change order option</h2>

    {/* Modal for full size images on click*/}
    <div
      id="modal01"
      className="w3-modal w3-black"
      style={{ paddingTop: 0 }}
    //   onClick="this.style.display='none'"
      onClick={()=>{alert('pressed')}}

    >
      <span className="w3-button w3-red w3-xxlarge w3-display-topright">
        ×
      </span>
      <div className="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
        <h1>HELLO</h1>
        <img id="img01" className="w3-image" />
        <p id="caption" />
      </div>
    </div>
    {/* Services */}


    <div className="tab">
  <button className="tablinks " onClick={()=>{openCity(event, 'single'); setIsMultipleActive(false)}}>Single Change Order</button>
  <button className="tablinks" onClick={()=>{openCity(event, 'multiple'); setIsMultipleActive(true)}}>Multiple Change Orders</button>

</div>

<div id="single" className="tabcontent">
  <h3>Single Change Orders</h3>
  <p>Single Change Orders Here.</p>
  <div>
    <div style={{flexDirection : "row"}}> 
    <Text> Enter Parid : </Text> 
    <input   label='Parid' type='text' value={parid} 
      name='Parid' placeholder='Enter Parid' onChange={changeParidHandler} 
      ></input>     
     </div>
    <div style={{flexDirection : "row"}}>
    <Text>District : </Text>
    <Text>{jur}</Text>
    </div>
    <div style={{flexDirection : "row"}}>
    <Text>Tax Year: </Text>
    <Text>{state.taxyear}</Text>
    </div>

    parid value == {parid}

      

  </div>
</div>
{/************ Multiple Change Orders Start************/}
<div id="multiple" className="tabcontent">
  <h3>Multiple Change Orders</h3>
  <p>Multiple Change Orders Here.</p>
</div>
{/************ Multiple Change Orders END OF LINE************/}

<div id="button-container" style={{ alignItems : "row"}}>
    <Button style={{backgroundColor :"red"}} title="CREATE BATCH" 
        />
    <Button style={{backgroundColor :"red"}} title="EDIT TAX YEAR" 
          onPress={()=>{setShowBatchField({...showBatchField,showTaxYear : true ,showJur : false})}}/>
    <Button style={{backgroundColor :"red"}} title="EDIT DISTRICT" 
     onPress={()=>{setShowBatchField({...showBatchField,showJur : true ,showTaxYear : false})}}/>
  </div>

  {
    showBatchField.showTaxYear === false && showBatchField.showJur === false  ? 
    <></>:showBatchField.showTaxYear === true ? 
    <>  <Select options={taxyearOptions} 
    placeholder="Select or type tax year"
        onChange={(e) => { handleTaxYearChange(e)}} />;</> : 
        <><Select options={jurOptions} 
        placeholder="Select or type jurisdiction"    
         onChange={(e) => handleJurChange(e)} 
         />;</>
  }
{isMutipleActive?
     <ScrollView>
 <ExcelToJsonConverter />
</ScrollView>  :
<></>


}

 
    {/* <ScrollView>
 <ExcelToJsonConverter />
</ScrollView> */}
     
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

// Modal Image Gallery
function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
}
function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
  export default BatchAdd


  // {data.length > 0 && (
  //   <table className="table">
  //     <thead>
  //       <tr>
  //         {Object.keys(data[0]).map((key) => (
  //           <th key={key}>{key}</th>
  //         ))}
  //       </tr>
  //     </thead>
  //     <tbody>
  //       {data.map((row, index) => (
  //         <tr key={index}>
  //           {Object.values(row).map((value, index) => (
  //             <td key={index}>{value}</td>
  //           ))}
  //         </tr>
  //       ))}
  //     </tbody>
  //   </table>
  // )}