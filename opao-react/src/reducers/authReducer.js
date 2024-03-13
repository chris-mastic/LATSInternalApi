import initialState from "../data/initialState"

const authReducer = (state, action) => {
    switch (action.type) {
  
        case 'SIGN_IN':
            return { ...state, ...action.payload.data}
        case 'SIGN_OUT':
            return {... state, 
                userName : null, 
                userId : null,
                token : null,
                taxyear :  (new Date().getFullYear()) + 1,
                roles : [],
                errorMessage : '', 
                isLoading :  true,
                expiration : null , 
                jur : 1,
                sub_data : [],  // subset of full data based on jurisdiction 
                full_data : [], // full data of all valid parid and tax year (except invalid parid or tax year)
                error_data : [] // error array due to invalid parid or tax year
            } 
        case 'RETRIEVE_TOKEN':
            return { ...state, token: action.payload.token,userName: action.payload.userName}
        case 'CLEAR_TOKEN':
            return {...state, token: null, userName: '' }
        case 'CHANGE_JUR':  
        console.log("storage before jur change............"+JSON.parse(localStorage.getItem("authkey")))  
        console.log("result change jur " +JSON.stringify({...state,...JSON.parse(localStorage.getItem("authkey")), jur : action.payload.jur}))

            state =  {...state,...JSON.parse(localStorage.getItem("authkey")), jur : action.payload.jur};
            console.log("new state " +JSON.stringify(state));
            localStorage.setItem("authkey",JSON.stringify(state));
            console.log("new auth key " +localStorage.getItem("authkey"));


            return state;
        case  'CHANGE_TAX_YEAR':
            console.log("storage before tax year change............"+JSON.parse(localStorage.getItem("authkey"))) 
            console.log("new tax year " + action.payload.taxyear);
            console.log("result change tax year " +JSON.stringify({...state,...JSON.parse(localStorage.getItem("authkey")), taxyear : action.payload.taxyear}))

            state =  {...state,...JSON.parse(localStorage.getItem("authkey")), taxyear : action.payload.taxyear};
            console.log("new state " +JSON.stringify(state));
            localStorage.setItem("authkey",JSON.stringify(state));
            console.log("new auth key " +localStorage.getItem("authkey"));
            return state
    
    

        default: state;
    }
}

export default authReducer;