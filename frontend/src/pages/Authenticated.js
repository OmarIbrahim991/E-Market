import React from "react"
import { getPayload } from "../utils/auth"
import { GET } from "../utils/api"

const Authenticated = () => {
    const [response, setResponse] = React.useState(null)
    const [message, setMessage] = React.useState("Authenticating user...")

    React.useEffect(() => {
        try {
            const token = window.location.href.split("#")[1].split("&")[0].split("=")[1]
            GET("/users", setResponse, { "Authorization": `Bearer ${token}` })
            localStorage.setItem("jwt", token)
            localStorage.setItem("payload", JSON.stringify(getPayload(token)))
        } catch (e) {
            localStorage.setItem("jwt", "")
            setMessage("Failed to authenticate user.")
            console.log(e.message)
        }
        
        if (response && response["success"]) {
            if (response["user"]["verified"]) {
                localStorage.setItem("userData", JSON.stringify(response["user"]))
                window.location.href = "/"
            } else {
                window.location.href = "/profile"
            }
        } else {
            setTimeout(() => {
                localStorage.setItem("jwt", "")
                setMessage("Failed to authenticate user.")
            }, 5000);
        }
    })

    return (
        <div id="authenticated">
            {message}
        </div>
    )
}

export default Authenticated
