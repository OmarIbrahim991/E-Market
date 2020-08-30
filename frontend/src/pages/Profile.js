import React from "react"
import { PATCH } from "../utils/api"
import { isAuthenticated } from "../utils/auth"

const Profile = ({ Header, userData={} }) => {
    const token = localStorage.getItem("jwt")
    const savedUserData = localStorage.getItem("userData") ? JSON.parse(localStorage.getItem("userData")) : {}
    const [user, updateUser] = React.useState({...savedUserData, ...userData})
    const [response, setResponse] = React.useState(null)

    React.useEffect(() => {
        if (response && response["success"]) {
            localStorage.setItem("userData", JSON.stringify(response.user))
            updateUser(response.user)
        }
    })

    const firstName = React.useRef()
    const lastName = React.useRef()

    const saveData = () => {
        PATCH(
            `/users`,
            setResponse,
            { "Authorization": `Bearer ${token}` },
            { first_name: firstName.current.value, last_name: lastName.current.value }
        )
    }

    return (
        <div id="profile">
            <Header />
            {
                isAuthenticated() ?
                <React.Fragment>
                    <p>{user.first_name}</p>
                    <p>{user.last_name}</p>
                    <input name="first_name" type="text" ref={firstName} />
                    <input name="last_name" type="text" ref={lastName} />
                    <button onClick={saveData}>Save</button>
                </React.Fragment>
                :
                <div>
                    <h1>Login first.</h1>
                </div>
            }
            </div>
    )
}

export default Profile
