import { View, Text } from 'react-native'
import {Button} from 'react-native'
import React, {useState, useContext} from 'react'
import {useNavigate} from 'react-router-dom' 
import {signout} from '../../contexts/AuthContext'
import { Context as AuthContext } from '../../contexts/AuthContext'


const Home = () => {
  const {state,signout} = useContext(AuthContext);
  
  const navigate = useNavigate()
  const [userState,setUserState] = useState({});

  const setData = ()=>{
    setUserState({...userState,...state})
  }

  const getData =  ()=>{
    const dataString = localStorage.getItem('authkey');    
    setUserState(state);
    return dataObject
  }

  
  const logouthandler = () =>{

    signout();
    console.log('navigate to splash')
    navigate('/');


  }
  try{
   //getData();
//   console.log(JSON.stringify(data));
//   console.log("line 17",username)
//   AsyncStorage.getItem('authkey').then((valueString)=>{
//     console.log('value of data on line 34 IN HOME', valueString);
//     const valueObject = JSON.parse(valueString);
//     console.log(typeof valueObject, valueObject)
//     const {token, expiration, userName} = valueObject
//    setstate(...state,{token, expiration, userName})
//  });
//    console.log(typeof dataObject,JSON.stringify(dataObject));
  
  }catch(e){
    console.log(e)
  }

 
  return (
    <View>
      <Text>Home</Text>
      <Text>user data from asyncstorage</Text>
      <Text>  userName ==={userState.userName}</Text>
      <Text>  expiration ==={userState.expiration}</Text>
      <Text>  token ==={userState.token}</Text>
      <Text>user data from context</Text>
      <Text>  userName ==={state.userName}</Text>
      <Text>  expiration ==={state.expiration}</Text>
      <Text>  token ==={state.token}</Text>
     
      <Button title='LOGOUT' onPress={logouthandler}/>
    </View>
  )
}

export default Home