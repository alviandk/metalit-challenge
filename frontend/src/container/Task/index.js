import React, { Component } from 'react';
import Axios from 'axios';

class Task extends Component{
  state={
    tasks:[],
    challenge:[]
  }

  componentDidMount(){
    const id = this.props.match.params.id;
    Axios.get('http://127.0.0.1:8001/api/challenge-task/'+id).then(response=>{
      this.setState({
        tasks:response.data.tasks,
        challenge:response.data.challenge[0]
      })
    })
  }

  render(){
    return (
      <section class="py-5">
        <div class="container py-5">
          <div class="row text-center text-white mb-5">
            <div class="col-lg-8 mx-auto">
                <h1 class="display-4">{this.state.challenge['name']}</h1>
            </div>
          </div>

          <div class="row">
              <div class="col-lg-7 mx-auto">
                  <ul class="timeline">
                    {this.state.tasks.map((task)=>{
                      return (
                        <li
                          class="timeline-item bg-white rounded ml-3 p-4 shadow"
                          key={task.id}

                        >
                          <div class="timeline-arrow"></div>
                          <h2 class="h5 mb-0">{task.name}</h2>
                          <span class="small text-gray">
                            <i class="fa fa-clock-o mr-1"></i>
                              {task.reward_amount.toLocaleString('en')}
                          </span>
                          <p class="text-small mt-2 font-weight-light">{task.description}</p>
                        </li>
                      );
                    })}  
                  </ul>

              </div>
          </div>
        </div>
      </section>
   )
  }
}
export default Task