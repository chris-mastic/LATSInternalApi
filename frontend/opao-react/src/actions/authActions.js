// import { AsyncStorage } from "react-native"
// import api from "../../config/api"



// export const tryLocalSignin = (dispatch) => {
//     return async () => {
//       console.log('from try local sign in')
//         const token = await AsyncStorage.getItem('authKey')
//         if (token) {
//             dispatch({ type: 'SIGN_IN', payload: token })
//             //navigate to main flow navigate('TrackList')
//         } else {
//             //navigate to authflow navigate('LoginFlow')
//         }
//     }
// }
// export const clearErrorMessage = (dispatch) => {
//     return () => {
//         dispatch({ type: 'clear_error_messade' })
//     }
// }

// export const replacePassword = (dispatch) => {
//     return async ({ username }) => {
//         try {
//             const response = await authApi.post('signup', { email, password });
//             await AsyncStorage.setItem('token', response.data.token)
//             dispatch({ type: 'SIGN_UP', payload: response.data.token })
          

//         } catch (err) {
//             dispatch({ type: 'add_error', payload: "Something went wrong with sign up" })
//         }

//     }
// }

// export const signin = (dispatch) => {
//     return  (userName,token,expiration) => {
//         try {
//             // console.log('called sign in with data')
//             // console.log('username: ' + username + ' password: ' + password)
//             // console.log('before call to LTC')
//             // console.log(api)
//             // const response =  api.post('/api/auth/v1/authenticate', { "username" :username, "password" :password });
//             // const {data} = response

//             // console.log(typeof response.data,JSON.stringify(response)) 
//             // console.log('after call to LTC')

//             //const {user_name, expiration, token} = response.data
//             AsyncStorage.setItem('authKey', JSON.stringify(data))
           
//             dispatch({ type: 'SIGN_IN', payload: {userName, expiration,token }})
            

//         } catch (err) {
//             dispatch({ type: 'add_error', payload: "Something went wrong with sign in" })
//         }

//     }
// }

// export const signout = (dispatch) => {
//     return () => {

//     }
// }