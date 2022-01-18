import React from "react";
import image1 from '../../assets/images/avatar/09.jpg';

const Banner = () => {
  return (
    <section class="pt-0">
      <div class="container-fluid px-0">
        <div class="card bg-blue h-100px h-md-200px rounded-0 pattern">
        </div>
      </div>
      <div class="container mt-n4">
        <div class="row">
          <div class="col-12">
            <div class="card bg-transparent card-body pb-0 ps-0 mt-2 mt-sm-0">
              <div class="row d-sm-flex justify-sm-content-between mt-2 mt-md-0">

                <div class="col-auto">
                  <div class="avatar avatar-xxl position-relative mt-n3">
                    <img class="avatar-img rounded-circle border border-white border-3 shadow"
                      src={image1} alt=""/>
                    <span class="badge bg-success text-white rounded-pill position-absolute top-50 start-100 translate-middle mt-4 mt-md-5 ms-n3 px-md-3">Pro
                    </span>
                  </div>
                </div>

                <div class="col d-sm-flex justify-content-between align-items-center">
                  <div>
                    <h1 class="my-1 fs-4">Lori Stevens</h1>
                    <ul class="list-inline mb-0">
                      <li class="list-inline-item me-3 mb-1 mb-sm-0">
                        <span class="h6">255</span>
                        <span class="text-body fw-light"> points</span>
                      </li>
                      <li class="list-inline-item me-3 mb-1 mb-sm-0">
                        <span class="h6">7</span>
                        <span class="text-body fw-light"> Completed courses</span>
                      </li>
                      <li class="list-inline-item me-3 mb-1 mb-sm-0">
                        <span class="h6">52</span>
                        <span class="text-body fw-light"> Completed lessons</span>
                      </li>
                    </ul>
                  </div>

                  <div class="mt-2 mt-sm-0">
                    <a href="student-course-list.html"
                      class="btn btn-outline-primary mb-0">
                      View my courses
                    </a>
                  </div>
                </div>
              </div>
            </div>

            <hr class="d-xl-none"/>
            <div class="col-12 col-xl-3 d-flex justify-content-between align-items-center">
              <a class="h6 mb-0 fw-bold d-xl-none"
                href="#">Menu
              </a>
              <button class="btn btn-primary d-xl-none"
                  type="button"
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasNavbar"
                  aria-controls="offcanvasNavbar">
                <i class="fas fa-sliders-h"></i>
              </button>
            </div>

          </div>
        </div>
      </div>
    </section>
    );
  };

export default Banner;