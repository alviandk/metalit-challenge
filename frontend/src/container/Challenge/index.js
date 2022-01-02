import React, { Component } from 'react';
import Axios from 'axios';
import "../../index.css";
import { Link } from "react-router-dom";

class Challenge extends Component{
    state={
        results:[]
    }

    componentDidMount(){
        Axios.get('http://127.0.0.1:8000/api/challenge?page=1').then(response=>{
            this.setState({
                results:response.data.results,
            })
        })
    }
    render(){
        return (
        <section class="py-5 bg-light">
            <div class="container">
                <div class="row text-center mb-5">
                    <div class="col-lg-8 mx-auto">
                        <h1 class="display-4">Metalit Challenge</h1>
                    </div>
                </div>

                <div class="row">
                {this.state.results.map((challenge)=>{
                    return (
                    <div class="col-md-4" key={challenge.id}>
                        <Link to={`/task/${challenge.id}`} className="text-reset text-decoration-none">
                        <div class="card p-3 mb-2">
                            <div class="d-flex justify-content-between">
                                <div class="d-flex flex-row align-items-center">
                                    <div class="icon"> <i class="bx bxl-mailchimp"></i> </div>
                                    <div class="ms-2 c-details">
                                        <h6 class="mb-0">Mailchimp</h6> <span>1 days ago</span>
                                    </div>
                                </div>
                                <div class="badge"> <span>{challenge.status}</span> </div>
                            </div>
                            <div class="mt-5">
                                <h3 class="heading">{challenge.name}</h3>
                                <h6 class="heading">{challenge.description}</h6>
                                <div class="mt-5">
                                    <div class="progress">
                                        <div class="progress-bar" role="progressbar">
                                        </div>
                                    </div>
                                    <div class="mt-3">
                                    	<span class="text1">
                                    		32 Applied <span class="text2">of 50 capacity</span>
                                    	</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </Link>
                    </div>
                    );
                  })}   
                </div>
            </div>
        </section>
      )
    }
}
export default Challenge