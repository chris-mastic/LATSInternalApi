import { View} from 'react-native'
import * as Animatable from 'react-native-animatable'
import Feather from 'react-native-vector-icons/Feather'
import React from 'react'

const CheckIcon = (props) => {
  return (
    <>
        {props.value ?
                    <Animatable.View animation='bounceIn'>
                        <Feather name='check-circle' color='green' size={15} />
                    </Animatable.View>
                    : <Feather name='check-circle' color='white' size={15} />}
    </>
  )
}

export default CheckIcon