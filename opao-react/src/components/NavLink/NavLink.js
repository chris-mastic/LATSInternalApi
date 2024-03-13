import React from 'react';
import {TouchableOpacity, Text} from 'react-native-web';
import styles from './NavLinkStyles'
import {useNavigate, Link} from 'react-router-dom'


const NavLink = (props) => {
  const navigate = useNavigate();
     
    //console.log('in props username ===  '+ props.info.username);

  return (
    <TouchableOpacity 
      onPress={()=>{navigate(props.route,{ 
                             state : {data :props.data}})}}>
     {/* <TouchableOpacity onPress={()=>{navigate(props.route,{username :props.state.username})}}></TouchableOpacity> */}
        <Text style={[styles.text,{color:props.color}]}>{props.text}</Text>
    </TouchableOpacity>
  )
}

export default NavLink