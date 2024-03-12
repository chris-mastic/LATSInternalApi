import createDataContext from "./createDataContext";
import authReducer from "../reducers/authReducer";
import api from "../../config/api";
import initialState from "../data/initialState";


const tryLocalSignin = (dispatch) => {
    return  () => {
      console.log('from try local sign in');
        const dataString = localStorage.getItem('authkey');
        console.log("(11) AuthContext : data as string format................ " + dataString);
        const data = JSON.parse(data)
        console.log("(13) AuthContext : data as string format................ " + JSON.stringify(data));
        if (data) {
            dispatch({ type: 'SIGN_IN', payload: data })
        }
    }
}
const clearErrorMessage = (dispatch) => {
    return () => {
        dispatch({ type: 'clear_error_messade' })
    }
}

const replacePassword = (dispatch) => {
    return async ({ username }) => {
        try {
            const response = await authApi.post('signup', { email, password });
            await AsyncStorage.setItem('token', response.data.token);
            dispatch({ type: 'SIGN_UP', payload: response.data.token });
          

        } catch (err) {
            dispatch({ type: 'add_error', payload: "Something went wrong with sign up" })
        }

    }
}

const signin = (dispatch) => {
    return async (data ) => {      
        try {      
                         
            console.log('before dispatch ===  ' + JSON.stringify(data));    

            dispatch({ type: 'SIGN_IN', payload: data});           
         
        } catch (err) {
            dispatch({ type: 'add_error', payload: "Something went wrong with sign in" })
           
        }
    }
}

const signout = (dispatch) => {
    return async () => {
        try {    
            // const dataString = localStorage.getItem("authkey");
            // console.log("data saved as string from local storage  ==== " + dataString);
            // //const {token} = data;
            // const dataObject = JSON.parse(dataString);
            // console.log("data retrieved as object from local storage  ==== " + JSON.stringify(dataObject));


            // console.log("token for the bearer string " +(dataObject.token));
            // let bearerString = `Bearer ${dataObject.token}` ;
          

            // let config = {
                
            //     headers: {
            //       'Authorization': bearerString
            //     }
            // }           
            
            const response = await api.post('/logout');
            console.log(JSON.stringify(response));
            localStorage.removeItem('authkey');     
            dispatch({ type: 'SIGN_OUT'})         
                   

        } catch (err) {
            dispatch({ type: 'add_error', payload: "Something went wrong with sign in" })
        }

    }
}

const changeJur = (dispatch) => {
    return async (jur ) => {      
        try {      
            dispatch({ type: 'CHANGE_JUR', payload: {jur}});           
            console.log('changing jurisdiction ===  ' + jur);    
         
        } catch (err) {
            dispatch({ type: 'add_error', payload: "Something went wrong with sign in" })
           
        }
    }
}

const changeTaxYear = (dispatch) => {
    return async (taxyear) => {      
        try {      
            dispatch({ type: 'CHANGE_TAX_YEAR', payload: {taxyear}});           
            console.log('changing tax year ===  ' + taxyear);    
         
        } catch (err) {
            dispatch({ type: 'add_error', payload: "Something went wrong with sign in" })
           
        }
    }
}
export const { Provider, Context } = createDataContext(
    authReducer,
    { signout, signin, clearErrorMessage, tryLocalSignin, changeJur, changeTaxYear },
    initialState
);