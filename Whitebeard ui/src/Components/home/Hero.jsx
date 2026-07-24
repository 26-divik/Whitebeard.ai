import React from 'react'
import { Link,useNavigate } from 'react-router-dom'
import logo from '../../assets/logo.svg'
import Button from '../ui/Button'
import MessageBar from '../ui/MessageBar'
const Hero = () => {
  const navigate = useNavigate();
  return (
    <>
      <div className='xl:h-screen h-fit xl:my-0 my-20 xl:flex xl:items-center'>
        <div className='flex flex-col items-center gap-9 h-fit w-full font-bold mt-20 xl:mt-0 text-primary font-jersey-25 tracking-widest'>
          <h1 className='lg:text-3xl'>INTRODUCING</h1>
          <img src={logo} alt="Logo" className='lg:w-1/2 w-9/10' />
          <MessageBar />
          <Button onClick={() => {navigate('/signup')}} text="JOIN THE CREW ➥" />
          <h1 className='lg:text-xl text-xs'>ALREADY A MEMBER? <Link className='text-tertiary hover:opacity-90 transition-opacity' to="/login">LOGIN</Link></h1>
        </div>
      </div>
    </>
  )
}
    
export default Hero
