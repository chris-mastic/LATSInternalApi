import React,{useContext} from "react";
import styles from "./SplashStyles";
import { View, Text, Button, Image, TouchableOpacity , TextInput} from 'react-native'
import * as Animatable from 'react-native-animatable'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons'
import { useNavigate } from "react-router-dom";
import { Context as AuthContext } from "../../contexts/AuthContext";


const SplashPage = () => { 
    const navigate = useNavigate();
    return <View style={styles.container}>
        
        <View style={styles.header}>
            <Animatable.Image
                animation='bounceIn'  duration={1500} style={styles.logo}
                source={require('../../../assets/OPAO_SEAL.jpg')}                
            />
         <Text style={styles.logo_name}>OPAO CHANGE ORDERS</Text>

        </View>
        <Animatable.View animation='fadeInUpBig' style={styles.footer}>
            <Text style={styles.title}>Start Change Orders</Text>
            <Text style={styles.text}>Start Processing Change Orders with Ease</Text>
            <TouchableOpacity style={styles.signIn} onPress={()=> navigate('signin') }>
                <Text style={styles.textSign}>Get Started</Text>
                <MaterialIcons name='navigate-next'
                    color='white'
                    size={20} />
            </TouchableOpacity>
        </Animatable.View>
   


    </View>
}

export default SplashPage;