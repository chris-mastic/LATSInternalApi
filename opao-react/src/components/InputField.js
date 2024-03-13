import { StyleSheet, Text, View} from 'react-native'
import { TextInput } from 'react-native-paper'
import FontAwesome from 'react-native-vector-icons/FontAwesome'
import Feather from 'react-native-vector-icons/Feather'
import React from 'react'


const InputField = (props) => {
  return (
    <>
   
    {props.leftIcon}
    <TextInput
      type={props.type}
      value={props.value}
      name={props.name}      
      placeholder={props.placeholder}
      onChange={props.onChange}
      autoCapitalize ='none'
      style = {[styles.textInput]} 
      secureTextEntry={props.secureTextEntry}
      right={props.right}
      />

    
    </>
  )
}

const styles = StyleSheet.create({
    container: {
      flex: 1, 
      backgroundColor: '#009387',
      alignItems:'center'
    },
    header: {
        flex: 1,
        justifyContent: 'flex-end',
        paddingHorizontal: 20,
        paddingBottom: 50
    },
    footer: {
        flex: 5,
        backgroundColor: '#fff',
        borderTopLeftRadius: 30,
        borderTopRightRadius: 30,
        borderBottomLeftRadius: 30,
        borderBottomRightRadius: 30,
        paddingHorizontal: 20,
        paddingVertical: 30,
        marginLeft:100,
        marginRight:100,
        marginTop:40,
        marginBottom:300,
        minWidth : 500,
        width : 300,
        
        
        
    },
    text_header: {
        color: '#fff',
        fontWeight: 'bold',
        fontSize: 30,
        alignSelf:'center'
    },
    text_footer: {
        color: '#05375a',
        fontSize: 18
    },
    action: {
        flexDirection: 'row',
        marginTop: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#f2f2f2',
        paddingBottom: 5
    },
    textInput: {
        flex: 1,
        marginTop: -12,
        paddingLeft: 10,
        color: '#05375a',
    },
    button: {
        alignItems: 'center',
        marginTop: 50
    },
    signIn: {
        width: '100%',
        height: 50,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 10
    },
    textSign: {
        fontSize: 18,
        fontWeight: 'bold'
    },
    textPrivate: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        marginTop: 20
    },
    color_textPrivate: {
        color: 'grey'
    },
    nav_buttons:{
        flexDirection:'row',
        
    },
    checkbox_remember_me:{
        alignItems:'flex-start',
        flexDirection:'row',
        alignSelf:'flex-start'
    }
    
  });

export default InputField
