const PROXY = process.env.PROXY
const DEFAULT_HEADERS = {"Content-Type": "application/json"}

export const GET = (endpoint, setResp, headers={}, parameters={}) => {
    const paramString = Object.entries(parameters).map(param => `${param[0]}=${param[1]}`).join("&")
    const urlString = paramString ? `${PROXY}${endpoint}?${paramString}` : `${PROXY}${endpoint}`
    window.fetch(urlString, { headers: {...DEFAULT_HEADERS, ...headers} })
    .then(resp => resp.json()).then(jsonResp => setResp(jsonResp))
    .catch(e => console.log(e))
}

export const POST = (endpoint, setResp, headers={}, body={}) => {
    window.fetch(`${PROXY}${endpoint}`, {
        method: "POST",
        headers: {...DEFAULT_HEADERS, ...headers},
        body: JSON.stringify(body)
    }).then(resp => resp.json()).then(jsonResp => setResp(jsonResp))
    .catch(e => console.log(e))
}

export const PATCH = (endpoint, setResp, headers={}, body={}) => {
    window.fetch(`${PROXY}${endpoint}`, {
        method: "PATCH",
        headers: {...DEFAULT_HEADERS, ...headers},
        body: JSON.stringify(body)
    }).then(resp => resp.json()).then(jsonResp => setResp(jsonResp))
    .catch(e => console.log(e))
}

export const PUT = (endpoint, setResp, headers={}, body={}) => {
    window.fetch(`${PROXY}${endpoint}`, {
        method: "PUT",
        headers: {...DEFAULT_HEADERS, ...headers},
        body: JSON.stringify(body)
    }).then(resp => resp.json()).then(jsonResp => setResp(jsonResp))
    .catch(e => console.log(e))
}

export const DELETE = (endpoint, setResp, headers={}) => {
    window.fetch(`${proxy}${endpoint}`, {
        method: "DELETE",
        headers: {...DEFAULT_HEADERS, ...headers}
    }).then(resp => resp.json()).then(jsonResp => setResp(jsonResp)).catch(e => console.log(e))
}
