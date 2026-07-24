import { createRoutesFromElements, Route, createBrowserRouter } from "react-router-dom";
import MainLayout from '../components/layouts/MainLayout'
import Home from '../pages/Home'
import Login from '../pages/Login'
import Signup from '../pages/Signup'
import Chats from '../pages/Chats'
const router = createBrowserRouter(createRoutesFromElements(
    <Route path="/" element={<MainLayout/>} >
        <Route path="/" element={<Home/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/signup" element={<Signup/>} />
        <Route path="/chats" element={<Chats/>} />
    </Route>
))

export {router}