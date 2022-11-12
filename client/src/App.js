import './App.css';
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import Main from './components/Main';
import Form from './components/Form';
// import Day from './components/Day';
// import Update from './components/Update';
// import Login from './components/Login';
// import Register from './components/Register';
import About from './components/About';
import {useState, useEffect} from 'react';
import axios from 'axios';

function App() {
  const [food, setFood] = useState('');
  const [calories, setCalories] = useState(0);
  const [foodList, setFoodList] = useState([]);
  const [dailyList, setDailyList] = useState([]);
  const [date, setDate] = useState('');
  const [loaded, setLoaded] = useState(false)


  const [data, setData] = useState({})

 
  
  return (
    <BrowserRouter>
      <div>
        <Routes>
            <Route 
              path='/' 
              element={
                <Main 
                  loaded={loaded} 
                  setLoaded={setLoaded}
                  data={data}
                  setData={setData}
                />}
            />
            
            <Route
              path='/new'
              element={
                <Form
                  food = {food} 
                  setFood = {setFood}
                  calories = {calories} 
                  setCalories = {setCalories} 
                  foodList={foodList} 
                  setFoodList={setFoodList}
                  dailyList={dailyList} 
                  setDailyList={setDailyList} 
                  date={date} 
                  setDate={setDate}
                />}
            />

            <Route path='/about' element={<About/>}/>
            
        </Routes>
      </div>
    </BrowserRouter>
    // <BrowserRouter>
    //   <div className="App d-flex flex-column">
    //     <h1>This is react with django!!</h1>
    //   {
    //     loaded ? 
    //     <p>{loaded}</p>:<p>{'Not worked'}</p>
    //   }
        /* <Routes>
          <Route 
            path = '/foodlog/home' 
            element = {<Main 
                            foodList={foodList} 
                            setFoodList={setFoodList}
                            dailyList={dailyList} 
                            setDailyList={setDailyList} 
                            setSuccessMsg={setSuccessMsg}
                      />} 
          />
          <Route 
            path = '/foodlog/new' 
            element = {<Form  
                            food = {food} 
                            setFood = {setFood}
                            calories = {calories} 
                            setCalories = {setCalories} 
                            foodList={foodList} 
                            setFoodList={setFoodList}
                            dailyList={dailyList} 
                            setDailyList={setDailyList} 
                            newDate={newDate} 
                            setNewDate={setNewDate}
                        />} 
          />
          <Route 
            path = '/foodlog/view/:id' 
            element = {<Day 
                            foodList={foodList} 
                            setFoodList={setFoodList}
                      />}
          />
          <Route 
            path = '/foodlog/update/:id' 
            element = {<Update 
                            food = {food} 
                            setFood = {setFood}
                            calories = {calories} 
                            setCalories = {setCalories} 
                            foodList={foodList} 
                            setFoodList={setFoodList}
                            dailyList={dailyList} 
                            setDailyList={setDailyList} 
                            newDate={newDate} 
                            setNewDate={setNewDate}
                      />}
          />
          {/* <Route path = '/foodlog/register' element = {<Register setSuccessMsg={setSuccessMsg}/>} />
          <Route path = '/foodlog/login' element = {<Login successMsg={successMsg} setSuccessMsg={setSuccessMsg}/>} />
          <Route path = '/foodlog/about' element = {<About/>} />
          <Route path = '/' element = {<Navigate to = '/foodlog/login'/>} /> */
          /* </Routes> */
          /* <p
          >Made by<a className='mx-1' id='githubLink' href='https://github.com/Jeremy-Hirschler' target={'_blank'}>Jeremy</a></p> */
          /* </div>*/
  );
  
}
export default App;
