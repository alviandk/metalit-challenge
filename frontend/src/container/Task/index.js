import React, { Component } from 'react';
import Axios from 'axios';
import { API_TASK } from '../../constant';

class Task extends Component{
  state={
    tasks:[],
    challenge:[]
  }

  componentDidMount(){
    const id = this.props.match.params.id;
    Axios.get(API_TASK+id).then(response=>{
      this.setState({
        tasks:response.data.tasks,
        challenge:response.data.challenge[0]
      })
    })
  }

  render(){
    return (
      <section className="py-5">
        <div className="container py-5">
          <div className="row text-center text-white mb-5">
            <div className="col-lg-8 mx-auto">
                <h1 className="display-4">{this.state.challenge['name']}</h1>
            </div>
          </div>

          <div className="row">
              <div className="col-lg-7 mx-auto">
                <div className="btn-task">
                  <button type="button" class="btn btn-light">Back</button>
                  <button type="button" class="btn btn-light">
                    Kerjakan challenge
                  </button>
                </div>

  
                  <ul className="timeline">
                    {this.state.tasks.map((task)=>{
                      return (
                        <li
                          className="timeline-item bg-white rounded ml-3 p-4 shadow"
                          key={task.id}

                        >
                          <div className="timeline-arrow"></div>
                          <h2 className="h5 mb-0">{task.name}</h2>
                          <span className="small text-gray">
                            <i class="fa fa-clock-o mr-1"></i>
                            Rp. {task.reward_amount.toLocaleString('en')}
                          </span>
                          <p className="text-small mt-2 font-weight-light">
                            {task.description}
                          </p>
                          <div className="d-flex justify-content-end">
                            <button type="button" class="btn btn-primary ">
                              Upload Bukti Pengerjaan Task
                            </button>
                          </div>
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