import React from "react"
import { navigate } from "hookrouter"


const Home = () => {
    //window.getComputedStyle(document.documentElement).getPropertyValue("--clr-secondary")
    //document.documentElement.style.setProperty("--clr-secondary", "#00f")
    return (
        <div id="home">
            <h1>This is home page</h1>
            <button onClick={() => navigate("/login")}>Login</button>
        </div>
    )
}

export default Home
