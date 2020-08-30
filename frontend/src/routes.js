import React from "react"
import Home from "./pages/Home"
import Profile from "./pages/Profile"
import Authenticated from "./pages/Authenticated"
import Header from "./components/Header"

const Routes = {
    "/": () => <Home Header={Header} />,
    "/home": () => <Home Header={Header} />,
    "/profile": () => <Profile Header={Header} />,
    "/authenticated": () => <Authenticated Header={Header} />,
}

export default Routes
