import React,{useState} from 'react'
import {Button} from "react-native"
import axios from 'axios';
import Cookies from 'js-cookie'


const api =  axios.create({
      
    baseURL: 'http://10.10.1.236:5000/api' ,
    headers:{
        'Content-Type': 'application/json',
        "Accept":'application/json',
        // 'Access-Control-Allow-Origin': '*',        

    }  
})   



function Test() {
    const [auth,setAuth] = useState({});
    const [cookie,setCookie] = useState('')

    const handleLogin = async () =>{
        try{
        await api.post("/login", {	username: "sdmagee",password: "GsEdAj2i"})
    .then((res) => {	
        console.log("response object === " + JSON.stringify(res));
        console.log("response data === " + JSON.stringify(res.data));    
        setAuth(JSON.stringify(res.data));
    
           localStorage.setItem("authkey",JSON.stringify(res.data));
           //setCookie(Cookies.get('session'))
        
        })
    }catch(e){
        console.log(e);
    }
    }
    const handleLogout = async () =>{
        try{

            console.log("calling handle logout.........................")
        //const  data = await fetch('http://localhost:5000');
        console.log("remove key from storage.........................")

        localStorage.removeItem("authkey");
        console.log("acalling api to logout.........................")

        const data = await api.post("/logout" )    
        console.log("response received after logout.........................")
    
        console.log(JSON.stringify(data)) ;
        console.log("remove cookie from browser after logout.........................")
       // Cookies.remove('session', { path: '' }) // removed!
        //Cookies.remove('session', { path: '/' /*, domain: '.yourdomain.com'*/ })
        console.log("show document cookie.........................",typeof document.cookie,document.cookie)

       


        setAuth(JSON.stringify(data));

//         const api = axios.create({
      
//                 baseURL: 'https://testapi.latax.la.gov/api' ,
//                 headers:{
//                     'Content-Type': 'application/json',
//                     "Accept":'application/json',
//                     'Authorization': localStorage.getItem("authkey")
//                     // 'Access-Control-Allow-Origin': '*',        
            
//                 }})

                
// //Add interceptors to instance
// api.interceptors.response.use(
//     response => response,
//     error => {
//         if (!error.response) {
//             setAuth(JSON.stringify(error))
//         }
//         else if (error.response.status === 401) {
//             setAuth(JSON.stringify(error))

//         }
//         return error;
//     });
//         const dataString = localStorage.getItem("authkey");
//         console.log("data saved as string from local storage  ==== " + dataString);
//         //const {token} = data;
//         const dataObject = JSON.parse(dataString);
//         console.log("data retrieved as object from local storage  ==== " + JSON.stringify(dataObject));

//         console.log("token for the bearer string " +(dataObject.token));
//         const {token} = dataObject
//         let bearerString = `Bearer ${token}` ;
//         console.log("bearer string === " + bearerString)

        
        
//         const response = await api.post('/Users/v1/logout')
//         .then((res) => {	
//             console.log("response object === " + JSON.stringify(res));
//             console.log("response data === " + JSON.stringify(res.data));    
//             setAuth(JSON.stringify(res.data));
//             localStorage.removeItem("authkey");
        
//             //setCookie(res.data.token);                           
            
//             });   
        // console.log(JSON.stringify(response));
        // setAuth(JSON.stringify(response))
        // localStorage.removeItem('authkey');     
           
     
       // await AsyncStorage.setItem('authkey', null);            
               

    } catch (err) {
        console.log(err)
    }

}

    
  return (
    <div>
    <div>Test</div>
    <Button style={{width:60, height : 10 }} title="login" onPress={handleLogin} />
    <Button style={{width:60, height : 10 }} title = "logout" onPress={handleLogout}/>
    <div style={{margin :70}}></div>
    <h1>Response String </h1>
    <h5>{JSON.stringify(auth)}</h5>
    <div style={{margin :30}}></div>
    <h1>Cookie String </h1>
    <h5>{cookie}</h5>

    </div>
  )
}

export default Test