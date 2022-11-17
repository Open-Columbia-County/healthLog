import React from 'react'
import {NavLink} from 'react-router-dom';

const Navbar = () => {
    return (
            <div className='d-flex justify-content-evenly mx-5 '>
                <NavLink to='/dashboard'>Home</NavLink>
                <NavLink to='/about'>About</NavLink>
                <NavLink to='/week'>Create New Week</NavLink>
                <NavLink to='/add/medication'>Medication List</NavLink>
                <NavLink to='/user/dashboard'>Profile</NavLink>
                <button>Logout</button>
            </div>
    )
}

export default Navbar;