import { BrowserRouter, Route, Routes } from "react-router-dom";
import { ProtectedRoutes } from "./ProtectedRoutes";
import React from 'react'
import Home1 from "../pages/Home/Home.jsx"
import ForgotPassword from "../pages/ForgotPassword/ForgotPassword.jsx";
import ChangeOrderAdd from "../pages/ChangeOrderAdd/ChangeOrderAdd.jsx"
import SignIn from "../pages/SignIn/SignIn.jsx"
import ResetPassword from "../pages/ResetPassword/ResetPassword.jsx"
import ChangeOrderSubmit from "../pages/ChangeOrderSubmit/ChangeOrderSubmit.jsx"
import ChangeOrderStatus from "../pages/ChangeOrderStatus/ChangeOrderStatus.jsx"
import NoPage from '../pages/NoPage/NoPage';
import Splash from '../pages/Splash/Splash.jsx'
// import Dashboard from "../Dashboard/Dashboard.jsx";
// import BatchAdd from "../pages/BatchAdd/BatchAdd.jsx"
// import BatchStatus from "../pages/BatchStatus/BatchStatus.jsx"
// import BatchSubmit from "../pages/BatchSubmit/BatchSubmit.jsx"
// import Test from '../Dashboard/Test.jsx'
import Test from "./Test.js";

import BatchAdd from '../pages/BatchAdd.js'
import BatchStatus from '../pages/BatchStatus.js'
import BatchSubmit from '../pages/BatchSubmit.js'
import BatchFields from '../pages/BatchFields.jsx'
import Home from '../pages/Home.js'






const ProjectRoutes = () => {
  return (
	<BrowserRouter >	
		<Routes >
    		{/* <Route path="/" element={<Splash />} />  */}
			<Route path="/" element={<Splash />} /> 
			<Route path="/test" element={<Test/>} />
			<Route path="/resetpassword" element={<ResetPassword />} /> 
			<Route path="/forgotpassword" element={<ForgotPassword />} /> 
			<Route path="/signin" element={<SignIn />} /> 
    		<Route path="*" element={<NoPage />} />
    		<Route element={<ProtectedRoutes />}>
				<Route path="/batchstatus" element={<BatchStatus />} /> 
				<Route path="/batchadd" element={<BatchAdd />} /> 
				<Route path="/batchsubmit" element={<BatchSubmit />} /> 
				<Route path="/batchfields" element={<BatchFields />} /> 
                <Route path="/changeordersubmit" element={<ChangeOrderSubmit/>} />
				<Route path="/changeorderstatus" element={<ChangeOrderStatus/>} />
				<Route path="/changeorderAdd" element={<ChangeOrderAdd/>} />
				<Route path="/home" element={<Home/>} />	
    		</Route>
      
    

  		</Routes>
	</BrowserRouter>

  )
}

export default ProjectRoutes
