import React from "react"
import { login, signup, logout, isAuthenticated } from "../utils/auth"

const Header = () => {
    let userData
    try {
        userData= JSON.parse(localStorage.getItem("userData"))
    } catch (e) {
        userData = {verified: false}
    }

    return (
        isAuthenticated() ?
        <header>{userData.verified ? <h3>{`${userData.first_name} ${userData.last_name}`}</h3> : null}<button onClick={logout}>Logout</button></header> :
        <header><button onClick={login}>Login</button><button onClick={signup}>Signup</button></header>
    )
}

export default Header
