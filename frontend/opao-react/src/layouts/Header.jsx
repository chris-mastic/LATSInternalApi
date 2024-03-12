import React, {useContext} from 'react'
import { Button } from 'react-native';
import {Context as AuthContext} from '../contexts/AuthContext'
import {useNavigate, Link} from 'react-router-dom'

function Header() {
  const {state : authState, changeJur, signout} = useContext(AuthContext);
  const navigate = useNavigate();

  return (
    <header className="w3-container-header w3-top w3-hide-medium w3-hide-small w3-black w3-xlarge "
    style={{zIndex:5}} >
{/* <a
href="javascript:void(0)"
className="w3-button w3-black w3-margin-right"
onClick={()=>{w3_open()}}
>

</a> */}
<Link className="w3-button w3-black w3-margin-right" 
  onClick={()=>{w3_close()}} 
  ></Link>
<div style={{flexDirection:'row',display : 'flex',justifyContent:'space-between'}}>
<div>OPAO Change Order Batch with header test  </div>
<div style={{marginRight:10, color:'white'}}>TAX YEAR {authState.taxyear} JUR {authState.jur}  {authState.userName}<Button title="LOGOUT" onPress={ ()=> { signout(); navigate("/")}}/></div>

</div>

</header>
  )
}

export default Header