import React from 'react'
import { Link } from 'react-router-dom'
const Button = ({ onClick , text}) => {
  return (
    <>
        <h1 onClick={onClick} className='font-bold font-jersey-25 cursor-pointer text-center px-3 py-2 bg-tertiary text-secondary lg:text-2xl text-lg text-nowrap tracking-widest rounded-4xl hover:opacity-90 transition-opacity'>{text}</h1>
    </>
  )
}
export default Button;