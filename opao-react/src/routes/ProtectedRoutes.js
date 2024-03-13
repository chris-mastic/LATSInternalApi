import {useContext} from "react";
import { Navigate,  Outlet } from "react-router-dom";
import { Context } from "../contexts/AuthContext";

export const ProtectedRoutes = () => {
  const {state, tryLocalSignin} = useContext(Context);

    try{
      const dataString = localStorage.getItem("authkey");         

      console.log('ProtectedRoute.js checking protected route using authkey in ..................');
      console.log('value of token ======  ' + dataString);
      console.log('value of context ======  ' + JSON.stringify(state));

      if ( dataString ){
      
        return <Outlet/>
      }else{
        return  <Navigate to="/"/>
      }
       
    }catch(e){
      console.log(e);
    }
};
