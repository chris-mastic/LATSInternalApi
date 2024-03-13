
const initialState = {
    userName : null, 
    userId : null,
    token : null,
    roles : [],
    errorMessage : '', 
    isLoading :  true,
    isLoggedIn : false,
    expiration : null , 
    jur : 1,
    taxyear :  (new Date().getFullYear()) + 1,
    sub_data : [],  // subset of full data based on jurisdiction 
    full_data : [], // full data of all valid parid and tax year (except invalid parid or tax year)
    error_data : [] // error array due to invalid parid or tax year
}

export default initialState;

