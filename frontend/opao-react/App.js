import Routes from './src/routes/ProjectRoutes';
import { Provider as AuthProvider } from './src/contexts/AuthContext';
import { ActivityIndicator } from 'react-native-paper';
import {useNavigate} from "react-router-dom";

const App = () => {
  const {state, tryLocalSignin} = useContext(AuthContext);
  const navigate = useNavigate();

  // //setNavigator(props.navigation)

  useEffect(() => {
    console.log("use effect called *******************************")
  
    tryLocalSignin();
    const data = localStorage.getItem("authkey");
    if(data){
      navigate("/home");
    }else{
      navigate("/");
    }    
     
  }, [])

  if( state.isLoading ) {
    return(
      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
        <ActivityIndicator size="large"/>
      </View>
    );
  }
  

}




export default () => {
  return <AuthProvider > 
    <Routes >      
    <App />
    </Routes>

  </AuthProvider>
};






// const App = () =>{
//   return (   
//     <AuthProvider>
//       <Routes />
//     </AuthProvider>  
//   )
// }

// export default App;














