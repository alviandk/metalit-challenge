import React, { useState, useEffect } from "react";
import "../../index.css";

const Task = () => {
    return (
        <div class="container">
          <div class="page-header">
            <h1 id="timeline">Task</h1>
          </div>
              <ul class="timeline">
                <li>
                  <div class="timeline-badge"><i class="glyphicon glyphicon-check"></i></div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">task.results.name</h4>
                      <p><small class="text-muted"><i class="glyphicon glyphicon-time">task.challenge</i></small></p>
                    </div>
                    <div class="timeline-body">
                      <p>task.description</p>
                    </div>
                  </div>
                </li>
                <li>
                  <div class="timeline-badge"><i class="glyphicon glyphicon-check"></i></div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">task.results.name</h4>
                      <p><small class="text-muted"><i class="glyphicon glyphicon-time">task.challenge</i></small></p>
                    </div>
                    <div class="timeline-body">
                      <p>task.description</p>
                    </div>
                  </div>
                </li>
            </ul>
      </div>
    );
  };

export default Task