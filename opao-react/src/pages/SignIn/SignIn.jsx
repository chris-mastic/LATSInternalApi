import React, { useContext, useState } from "react";
import styles from "./SignInStyles";
import { CheckBox,View, Text, Image, TouchableOpacity } from 'react-native'
import * as Animatable from 'react-native-animatable'
import FontAwesome from 'react-native-vector-icons/FontAwesome'
import Feather from 'react-native-vector-icons/Feather'
import NavLink from "../../components/NavLink/NavLink";
import HorizontalSpacer from "../../components/HorizontalSpacer/HorizontalSpacer";
import InputField from "../../components/InputField";
import CheckIcon from "../../components/CheckIcon";
import { Context as AuthContext } from "../../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import useLocalStorage from '../../hooks/useLocalStorage'
import api from "../../../config/api";
import '../../../w3.css'

let defaultData = { username: '', password: '', valid_username: false, 
                    valid_password: false,  hash: '',secureTextEntry : true }
const SignInPage = (props) => {
    const [cookie, setCookie] = useLocalStorage("authkey")
    const navigate = useNavigate()
    const {signin,state} = useContext(AuthContext);
 
    const [data, setData] = useState(defaultData);   
    const updateSecureEntry = () => {
        setData({ ...data, secureTextEntry: !data.secureTextEntry }) }
  
    const usernameInputHandler = (e) => {
            setData({...data, username: e.target.value, 
                   valid_username: e.target.value.trim().length !== 0 ? true : false })     }

    const passwordInputHandler = (e) => {

        setData({...data, password: e.target.value, 
               valid_password: e.target.value.trim().length !== 0 ? true : false })}
     
    const handleLogin = async (username, password)=>{
        try{
      console.log("username == " + username + ", password == " + password);
		await api.post("/login", {	username: username,password: password})
        .then((res) => {	
            console.log("response object === " + JSON.stringify(res));
            console.log("response data === " + JSON.stringify(res.data));    
          
               signin({...state,...res.data});
               localStorage.setItem("authkey",JSON.stringify({...state,...res.data}));

            
            })
        }catch(e){
            console.log(e);

        }     
    }
    return <View style={styles.container}>
        <View  style={styles.header}>
            <Text style={styles.text_header}>Welcome</Text>
            {/* <a href="./" className=" w3-hover-orange ">News</a> */}
        </View>
        <Animatable.View style={styles.footer} animation='fadeInUpBig'>
        <Text  style={styles.text_footer}>Username</Text>
        <View style={styles.action}>
            <InputField 
                   label='Username' type='text' value={data.username} secureTextEntry={false}
                   name='Username' placeholder='Enter Username' onChange={usernameInputHandler} 
                   leftIcon ={<FontAwesome name='user-o' color='#05375a' size={20} />}  />                        
             
             <CheckIcon value={data.valid_username} />                        
            </View>
            <Text style={[styles.text_footer, { marginTop: 35 }]}>Password</Text>

            <View style={styles.action}>
                <InputField 
                    label='Password' type='password' value={data.password} secureTextEntry={data.secureTextEntry}
                    name='Password' placeholder='Enter Password' onChange={passwordInputHandler} 
                    leftIcon ={<FontAwesome name='lock' color='#05375a' size={20} />}  
                    right={  <TouchableOpacity onPress={updateSecureEntry}>
             
                    {data.secureTextEntry ?
                    <Feather name='eye-off' color='brown' size={20} />
                    :
                    <Feather name='eye' color='brown' size={20} />}
                </TouchableOpacity>}
                
                />   
               <CheckIcon value={data.valid_password} />

            </View>
            <View style={styles.button}>
            <TouchableOpacity onPress={()=>{ handleLogin(data.username,data.password).then(()=>navigate('/home')) }
                                         
                                }
                                         
                style={[styles.signIn,{backgroundColor:'#009387'}]}>
                    <Text>{data.password}   {data.username}</Text>
                <Text style={{color:'white'}}>Sign In</Text>           
            </TouchableOpacity>
            {<Text>username {state.userName} expiration {state.expiration} </Text>}


            <View style={styles.nav_buttons}>
            <View style={{flex: 1,alignItems:'flex-start'}}>
             <NavLink route='/forgotpassword' text='Forgot Password?' color='#009387' data={ data.username}/>
             <HorizontalSpacer space={200}/>
             </View>
             <View style={{alignItems:'flex-end'}}>
             <NavLink route='/resetpassword' text='Reset Password?' color='#009387' data={ data.username} />   
             </View>     

            </View>
            <View style={styles.checkbox_remember_me}>
             
             <CheckBox />
             <Text>Remember Me</Text>    
             </View>
            </View>
            
        </Animatable.View>

    </View>
}

export default SignInPage;