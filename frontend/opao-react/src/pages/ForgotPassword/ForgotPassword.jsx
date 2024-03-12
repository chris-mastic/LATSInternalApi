import React, { useState } from "react";
import styles from "./ForgotPasswordStyles";
import { CheckBox,View, Text, Button, Image, TouchableOpacity , TextInput} from 'react-native'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons'
import * as Animatable from 'react-native-animatable'
import FontAwesome from 'react-native-vector-icons/FontAwesome'
import Ionicons from 'react-native-vector-icons/Ionicons'

// import Feather from 'react-native-vector-icons/Feather'
// import AsyncStorage from "@react-native-async-storage/async-storage";
// import axios from "axios";
import NavLink from "../../components/NavLink/NavLink";
import HorizontalSpacer from "../../components/HorizontalSpacer/HorizontalSpacer";
import { credentialHandler } from "../../utils/authUtils";
import { useRoute } from "@react-navigation/native";



/**
 * 

   
                <FontAwesome name='user-o' color='#05375a' size={20}
                />
                <TextInput placeholder="Your Username" style={styles.textInput}
                value= {userName.length === 0? '' : userName}
                    autoCapitalize="none" onChangeText={(input) => {credentialHandler(input,setUserName)  }}
                />
 */

let defaultData = { username: '', password: '', valid_username: false, valid_password: false,hash: '' }
const ForgotPasswordPage = () => {
    const route = useRoute();
    const [userName, setUserName]= useState(route.params?.username);

    const [data, setData] = useState(defaultData);
  
    const usernameInputHandler = (val) => {
        if (val.trim().length !== 0) {
            setData({
                ...data,
                username: val,
                valid_username: true,
                isValidUser: true
            });
        } else {
            setData({
                ...data,
                username: val,
                valid_username: false,
                isValidUser: false
            });
        }
    }

    const passwordInputHandler = (val) => {
        if (val.trim().length !== 0) {
            setData({
                ...data,
                password: val,
                valid_password: true,
                isValidUser: true
            });
        } else {
            setData({
                ...data,
                password: val,
                valid_password: false,
                isValidUser: false
            });
        }
    }
  
    return <View style={styles.container}>
        {/* <StatusBar backgroundColor='white' barStyle="light-content"/> */}
        <View style={styles.header}>
            <Text style={styles.text_header}>Forgot Password</Text>
        </View>
        <Animatable.View style={styles.footer} animation='fadeInUpBig'>
            <View style={styles.action}>             
                    <Ionicons name='mail-sharp' color='#05375a' size={20}
                />
                <TextInput placeholder="Enter Your Username" style={styles.textInput}
                value= {userName.length === 0? '' : userName}
                    autoCapitalize="none" onChangeText={(input) => {credentialHandler(input,setUserName)  }}
                />
            </View>
       
           
            <View style={styles.button}>
            <TouchableOpacity //onPress={()=>handleLogin(data.username,data.password) }
                                         
                style={[styles.signIn,{backgroundColor:'#009387'}]}>
                <Text style={{color:'white'}}>Send New Password</Text>           
            </TouchableOpacity>    
  
          
            </View>
            
        </Animatable.View>

    </View>
}

export default ForgotPasswordPage;