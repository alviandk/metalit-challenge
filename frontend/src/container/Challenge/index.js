import React, { Component } from 'react';
import Axios from 'axios';
import { Link } from "react-router-dom";
import { API_CHALLENGE } from '../../constant';

class Challenge extends Component{
    state={
        results:[]
    }

    componentDidMount(){
        Axios.get(API_CHALLENGE).then(response=>{
            this.setState({
                results:response.data.results,
            })
        })
    }
    render(){
        return (
        <section className="py-5">
            <div className="container">
                <div className="row text-center mb-5">
                    <div className="col-lg-8 mx-auto">
                        <h1 className="display-4 text-white">Metalit Challenge</h1>
                    </div>
                </div>

                <div className="row">
                {this.state.results.map((challenge)=>{
                    return (
                    <div class="col-md-4" key={challenge.id}>
                        <Link to={`/task/${challenge.id}`} 
                            className="text-reset text-decoration-none">
                            <div className="card p-3 mb-2">
                                <div className="d-flex justify-content-between mb-4">
                                    <div>
                                        <h3 className="heading">{challenge.name}</h3>
                                        <h6 className="heading">{challenge.description}</h6>
                                        <h6 className="heading">Rp. {challenge.budget.toLocaleString('en')}</h6>
                                    </div>
                                    <div className="badge">
                                        <span>{challenge.status}</span>
                                    </div>
                                </div>
                                <button type="button" class="btn btn-primary">
                                Lihat Task
                                </button>
                                <br class="mb-3"/>
                                <button type="button" class="btn btn-primary">
                                    Kerjakan Challenge
                                </button>
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