import axios from "axios";

const API_ROOT_URL =  'http://10.10.1.236:5000/api'
const api =  axios.create({
      
    baseURL: API_ROOT_URL ,
    headers:{
        'Content-Type': 'application/json',
        "Accept":'application/json'
    }
  
})

export default api




