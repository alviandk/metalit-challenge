import React, { Component } from 'react';
import "../../index.css";
import Axios from 'axios';

class Task extends Component{
  state={
    count:null,
    next:null,
    previous:null,
    results:[]
  }

  componentDidMount(){
    const id = this.props.match.params.id;
    Axios.get('http://127.0.0.1:8000/api/task/'+id).then(response=>{
      this.setState({
        results:response.data.results,
        count:response.data.count,
        next:response.data.next,
        previous:response.data.previous
      })
    })
  }

  render(){
    console.log(this.state.results)
    return (
      <section class="py-5 bg-info">
        <div class="container py-5">
          <div class="row text-center text-white mb-5">
            <div class="col-lg-8 mx-auto">
                <h1 class="display-4">TASK</h1>
            </div>
          </div>

          <div class="row">
              <div class="col-lg-7 mx-auto">
                  <ul class="timeline">
                    {this.state.results.map((task)=>{
                      return (
                        <li
                          class="timeline-item bg-white rounded ml-3 p-4 shadow"
                          key={task.id}

                        >
                          <div class="timeline-arrow"></div>
                          <h2 class="h5 mb-0">{task.name} 1</h2>
                          <span class="small text-gray"><i class="fa fa-clock-o mr-1"></i>{task.reward_amount}</span>
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