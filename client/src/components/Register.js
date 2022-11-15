import axios from 'axios';
import React, {useState, useEffect} from 'react'
import { useNavigate, Link } from 'react-router-dom';

const Register = (props) => {
    // const {setSuccessMsg} = props;
    const navigate = useNavigate();
    const [userEmail, setUserEmail] = useState('');
    const [username, setUsername] = useState('');
    const [userPassword, setUserPassword] = useState('');
    const [errors, setErrors] = useState({});

    useEffect(()=> {
        // setSuccessMsg('')
    },[])

    const handleRegister = async (e) => {
        e.preventDefault();
        const postData = {
            email: userEmail,
            username,
            password: userPassword,
        };
        
        try{
            console.log(postData)
            await axios.post('/api/auth/register/', postData);
            navigate('/login');
        }catch(err){
            console.log(err)
            setErrors(err.response.data)
        }
    }
    

    return (
        <div className='container'>
            <div className='row'>
                <div className='border border-dark rounded mx-auto my-4 p-3 column col-10 col-sm-8 col-md-6 col-lg-6'>
                    <h1>Register New User</h1>
                    <form onSubmit={handleRegister} className='d-flex flex-column mx-auto w-50'>
                        <div className='m-3'>
                            <label className='mx-4'>Enter Email</label>
                            <input type = 'text' value = {userEmail} 
                            onChange={(e)=>setUserEmail(e.target.value)}/>
                        </div>
                        <div className='m-3'>
                            <label className='mx-4'>Enter Username</label>
                            <input type = 'text' value = {username} 
                            onChange={(e)=>setUsername(e.target.value)}/>
                        </div>
                        <div className='m-3'>
                            <label className='mx-3'>Enter Password</label>
                            <input type = 'password' value = {userPassword}
                            onChange={(e)=>setUserPassword(e.target.value)}/>
                        </div>
                        <div>
                            <button className='btn btn-warning'>Register</button>
                        </div>
                    </form>
                    {
                        !errors.email ? 
                        null
                        :errors.email[0][0] =='E' ?
                        <p className='errColor my-3'>{errors.email[0]}</p>
                        :<p className='errColor my-3'>Email {errors.email[0].slice(11)}</p>
                    }
                    {
                        !errors.password ? 
                        null
                        :errors.password[0].length > 30 ? 
                        <p className='errColor my-3'>Password must be {errors.password[0].slice(22)}</p>
                        :<p className='errColor my-3'>Password {errors.password[0].slice(11)}</p>
                    }
                    {/* {
                        errors.password && errors.password[0].length < 30 ? 
                        <p className='errColor my-3'>Password {errors.password[0].slice(11)}</p>: null
                    } */}
                    
                    <div className='mt-3'>

                        <Link to='/login'>Back to Login</Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Register;