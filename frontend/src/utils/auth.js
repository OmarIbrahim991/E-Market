export const AUTH0_DOMAIN = process.env.AUTH0_DOMAIN
export const CLIENT_ID = process.env.CLIENT_ID
export const AUDIENCE = process.env.AUDIENCE
export const SCOPE = process.env.SCOPE
export const REDIRECT_URI = process.env.REDIRECT_URI

const DEFAULT_LOGIN_PARAMS = {
    audience: AUDIENCE,
    client_id: CLIENT_ID,
    redirect_uri: REDIRECT_URI,
    response_type: "token"
}

const DEFAULT_LOGOUT_PARAMS = {
    returnTo: window.location.origin,
    client_id: CLIENT_ID
}

export const login = (parameters={}) => {
    const params = {...DEFAULT_LOGIN_PARAMS, ...parameters}
    const paramString = Object.entries(params).map(param => `${param[0]}=${param[1]}`).join("&")

    window.location.href = `https://${AUTH0_DOMAIN}/authorize?${paramString}`
}

export const signup = (parameters={}) => {
    login({...parameters, "login_mode": "signup"})
}

export const logout = (parameters={}) => {
    localStorage.setItem("jwt", "")
    localStorage.setItem("payload", JSON.stringify({}))
    localStorage.setItem("userData", JSON.stringify({}))

    const params = {...DEFAULT_LOGOUT_PARAMS, ...parameters}
    const paramString = Object.entries(params).map(param => `${param[0]}=${param[1]}`).join("&")

    window.location.href = `https://${AUTH0_DOMAIN}/v2/logout?${paramString}`
}

export const isAuthenticated = () => {
    const jwt = localStorage.getItem("jwt")
    if (jwt && jwt.split(".").length === 3) { return true }
    return false
}

export const getPayload = accessToken => {
    const base64Url = accessToken.split(".")[1]
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/")
    const jsonPayload = decodeURIComponent(atob(base64).split("").map(c => {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2)
    }).join(""))
    return JSON.parse(jsonPayload)
}
