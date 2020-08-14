import { useRoutes } from "hookrouter"
import Routes from "./routes"
import NotFound from "./pages/NotFound"

const App = () => {
    const Page = useRoutes(Routes)

    return Page || NotFound
}

export default App
