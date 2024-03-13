import FontAwesome from 'react-native-vector-icons/FontAwesome'
import Feather from 'react-native-vector-icons/Feather'
import { StyleSheet, TouchableOpacity } from 'react-native'
import React from 'react'

const EyeIcon = (props) => {
  return (
    <TouchableOpacity onPress={props.updateSecureEntry}>
             
        {props.secureTextEntry ?
        <Feather name='eye-off' color='brown' size={20} />
        :
        <Feather name='eye' color='brown' size={20} />}
    </TouchableOpacity>
  )
}

export default EyeIcon

