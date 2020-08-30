import React from "react"
import Product from "../components/Product"

const Home = ({ Header }) => {
    //window.getComputedStyle(document.documentElement).getPropertyValue("--clr-secondary")
    //document.documentElement.style.setProperty("--clr-secondary", "#00f")

    return (
        <div id="home">
            <Header />
            <h1>This is home page</h1>
            <Product imgLink="https://cdn.spacetelescope.org/archives/images/wallpaper2/heic2007a.jpg" imgTitle="star birth" />
        </div>
    )
}

export default Home
