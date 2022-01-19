import React from "react";
import Banner from "../../components/Banner";

const Payouts = () => {
  return (
      <main>
        <Banner/>

        <section class="pt-0">
          <div class="container">
            <div class="row">

              <div class="col-xl-3">
                <nav class="navbar navbar-light navbar-expand-xl mx-0">
                  <div class="offcanvas offcanvas-end"
                    tabindex="-1"
                    id="offcanvasNavbar"
                    aria-labelledby="offcanvasNavbarLabel">

                    <div class="offcanvas-header bg-light">
                      <h5 class="offcanvas-title"
                        id="offcanvasNavbarLabel">My profile
                      </h5>
                      <button type="button"
                        class="btn-close text-reset" 
                        data-bs-dismiss="offcanvas" 
                        aria-label="Close"> 
                      </button>
                    </div>

                    <div class="offcanvas-body p-3 p-xl-0">
                      <div class="bg-dark border rounded-3 pb-0 p-3 w-100">

                        <div class="list-group list-group-dark list-group-borderless">
                          <a class="list-group-item" 
                            href="/">
                            <i class="bi bi-ui-checks-grid fa-fw me-2"></i>
                            Dashboard
                          </a>
                          <a class="list-group-item" 
                            href="/">
                            <i class="bi bi-card-checklist fa-fw me-2"></i>
                            My Subscriptions
                          </a>
                          <a class="list-group-item" 
                            href="/">
                            <i class="bi bi-basket fa-fw me-2"></i>
                            My Courses
                          </a>
                          <a class="list-group-item"
                            href="/">
                            <i class="bi bi-credit-card-2-front fa-fw me-2"></i>
                            Payment info
                          </a>
                          <a class="list-group-item" 
                            href="/">
                            <i class="bi bi-cart-check fa-fw me-2"></i>
                            Wishlist
                          </a>
                          <a class="list-group-item" 
                            href="/order">
                            <i class="bi bi-folder-check fa-fw me-2"></i>
                            Orders
                          </a>
                          <a class="list-group-item active" 
                            href="/payouts">
                            <i class="bi bi-wallet2 fa-fw me-2"></i>
                            Payouts
                          </a>
                          <a class="list-group-item" 
                            href="/edit-profile">
                            <i class="bi bi-pencil-square fa-fw me-2"></i>
                            Edit Profile
                          </a>
                          <a class="list-group-item" 
                            href="/setting">
                            <i class="bi bi-gear fa-fw me-2"></i>
                            Settings
                          </a>
                          <a class="list-group-item" 
                            href="/instructor-delete-account.html">
                            <i class="bi bi-trash fa-fw me-2"></i>
                            Delete Profile
                          </a>
                          <a class="list-group-item text-danger bg-danger-soft-hover" 
                            href="/sign-out">
                            <i class="fas fa-sign-out-alt fa-fw me-2"></i>
                            Sign Out
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </nav>
              </div>

              <div class="col-xl-9">
                <div class="row g-4 mb-4">
                  <div class="col-sm-6 col-md-4">
                    <div class="border p-3 rounded-3 h-100">
                      <div class="d-flex mb-1 justify-content-between align-items-center">
                        <h6 class="mb-0">
                          Last month payout
                        </h6>
                        <span class="badge bg-success bg-opacity-10 text-success ms-2 mb-0">
                          Paid
                        </span>
                      </div>
                      <h2 class="mb-2 mt-2">$12,825</h2>
                      <a href="/">View transaction</a>
                    </div>
                  </div>

                  <div class="col-sm-6 col-md-4">
                    <div class="border p-3 rounded-3 h-100">
                      <h6 class="mb-0">This month earning</h6>
                      <h2 class="mb-2 mt-2">$15,356</h2>
                      <p class="mb-0">Expected payout on 05/08/2021</p>
                    </div>
                  </div>

                  <div class="col-sm-6 col-md-4">
                    <div class="bg-primary bg-opacity-10 h-100 p-3 rounded-3">
                      <h6 class="mb-0">Balance</h6>
                      <h2 class="mb-2 mt-2">$8,485</h2>
                      <a href="/" 
                        class="btn btn-sm btn-primary mb-0">
                        Withdraw Earning
                      </a>
                    </div>
                  </div>
                </div>

                <div class="card border rounded-3">
                  <div class="card-header border-bottom">
                    <h3 class="mb-0">Payouts</h3>
                  </div>

                  <div class="card-body">
                    <div class="row g-3 align-items-center justify-content-between mb-4">
                      <div class="col-md-8">
                        <form class="rounded position-relative">
                          <input class="form-control pe-5 bg-transparent" 
                            type="search" 
                            placeholder="Search" 
                            aria-label="Search"/>
                          <button class="btn bg-transparent px-2 py-0 position-absolute top-50 end-0 translate-middle-y" 
                            type="submit">
                            <i class="fas fa-search fs-6 "></i>
                          </button>
                        </form>
                      </div>

                      <div class="col-md-3">
                        <form>
                          <select class="form-select js-choice border-0 z-index-9 bg-transparent"
                            aria-label=".form-select-sm">
                            <option value="">Sort by</option>
                            <option>Free</option>
                            <option>Newest</option>
                            <option>Oldest</option>
                          </select>
                        </form>
                      </div>
                    </div>

                    <div class="table-responsive border-0">
                      <table class="table table-dark-gray align-middle p-4 mb-0 table-hover">
                        <thead>
                          <tr>
                            <th scope="col" class="border-0 rounded-start">Payout</th>
                            <th scope="col" class="border-0">Amount</th>
                            <th scope="col" class="border-0">Status</th>
                            <th scope="col" class="border-0 rounded-end">Date</th>
                          </tr>
                        </thead>

                        <tbody>
                          <tr>
                            <td>
                              <h6 class="mt-2 mt-lg-0 mb-0">
                                <a href="/">Successful payout #102356</a>
                              </h6>
                            </td>

                            <td>$3,999
                              <a href="/"
                                class="h6 mb-0"
                                role="button" id="dropdownShare"
                                data-bs-toggle="dropdown" 
                                aria-expanded="false">
                                <i class="bi bi-info-circle-fill"></i>
                              </a>
                              <ul class="dropdown-menu dropdown-w-sm dropdown-menu-end min-w-auto shadow rounded" 
                                aria-labelledby="dropdownShare">
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Commission
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>

                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="me-4 small">
                                      Us royalty withholding
                                    </span>
                                    <span class="text-danger small">
                                      -$0.00
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>
                                
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Earning
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                </li>
                              </ul>
                            </td>

                            <td class="text-center text-sm-start">
                              <span class="badge bg-success bg-opacity-10 text-success">
                                Paid
                              </span>
                            </td>

                            <td>18/8/2021</td>
                          </tr>

                          <tr>
                            <td>
                              <h6 class="mt-2 mt-lg-0 mb-0">
                                <a href="/">Successful payout #102589</a>
                              </h6>
                            </td>

                            <td>$4,875
                              <a href="/" 
                                class="h6 mb-0" 
                                role="button" 
                                id="dropdownShare1" 
                                data-bs-toggle="dropdown" 
                                aria-expanded="false">
                                <i class="bi bi-info-circle-fill"></i>
                              </a>
                              <ul class="dropdown-menu dropdown-w-sm dropdown-menu-end min-w-auto shadow rounded" 
                                aria-labelledby="dropdownShare1">
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Commission
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>

                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="me-4 small">
                                      Us royalty withholding
                                    </span>
                                    <span class="text-danger small">
                                      -$0.00
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>
                                
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Earning
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                </li>
                              </ul>
                            </td>

                            <td class="text-center text-sm-start">
                              <span class="badge bg-success bg-opacity-10 text-success">
                                Paid
                              </span>
                            </td>

                            <td>12/8/2021</td>
                          </tr>

                          <tr>
                            <td>
                              <h6 class="mt-2 mt-lg-0 mb-0">
                                <a href="/">Successful payout #108645</a>
                              </h6>
                            </td>

                            <td>$1,800
                              <a href="/" 
                                class="h6 mb-0" 
                                role="button" 
                                id="dropdownShare2" 
                                data-bs-toggle="dropdown" 
                                aria-expanded="false">
                                <i class="bi bi-info-circle-fill"></i>
                              </a>
                              <ul class="dropdown-menu dropdown-w-sm dropdown-menu-end min-w-auto shadow rounded" 
                                aria-labelledby="dropdownShare2">
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Commission
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>

                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="me-4 small">
                                      Us royalty withholding
                                    </span>
                                    <span class="text-danger small">
                                      -$0.00
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>
                                
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Earning
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                </li>
                              </ul>
                            </td>

                            <td class="text-center text-sm-start">
                              <span class="badge bg-danger bg-opacity-10 text-danger">
                                Cancelled
                              </span>
                            </td>

                            <td>22/8/2021</td>
                          </tr>

                          <tr>
                            <td>
                              <h6 class="mt-2 mt-lg-0 mb-0">
                                <a href="/">Successful payout #108645</a>
                              </h6>
                            </td>

                            <td>$6,800
                              <a href="/" 
                                class="h6 mb-0" 
                                role="button" 
                                id="dropdownShare3" 
                                data-bs-toggle="dropdown" 
                                aria-expanded="false">
                                <i class="bi bi-info-circle-fill"></i>
                              </a>
                              <ul class="dropdown-menu dropdown-w-sm dropdown-menu-end min-w-auto shadow rounded" 
                                aria-labelledby="dropdownShare3">
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Commission
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>

                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="me-4 small">
                                      Us royalty withholding
                                    </span>
                                    <span class="text-danger small">
                                      -$0.00
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>
                                
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Earning
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                </li>
                              </ul>
                            </td>

                            <td class="text-center text-sm-start">
                              <span class="badge bg-success bg-opacity-10 text-success">
                                Paid
                              </span>
                            </td>

                            <td>28/8/2021</td>
                          </tr>

                          <tr>
                            <td>
                              <h6 class="mt-2 mt-lg-0 mb-0">
                                <a href="/">Successful payout #108645</a>
                              </h6>
                            </td>

                            <td>$3,576
                              <a href="/" 
                                class="h6 mb-0" 
                                role="button" 
                                id="dropdownShare4" 
                                data-bs-toggle="dropdown" 
                                aria-expanded="false">
                                <i class="bi bi-info-circle-fill"></i>
                              </a>
                              <ul class="dropdown-menu dropdown-w-sm dropdown-menu-end min-w-auto shadow rounded" 
                                aria-labelledby="dropdownShare4">
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Commission
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>

                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="me-4 small">
                                      Us royalty withholding
                                    </span>
                                    <span class="text-danger small">
                                      -$0.00
                                    </span>
                                  </div>
                                  <hr class="my-1"/>
                                </li>
                                
                                <li>
                                  <div class="d-flex justify-content-between">
                                    <span class="small">
                                      Earning
                                    </span>
                                    <span class="h6 mb-0 small">
                                      $86
                                    </span>
                                  </div>
                                </li>
                              </ul>
                            </td>

                            <td class="text-center text-sm-start">
                              <span class="badge bg-orange bg-opacity-10 text-orange">
                                Pending
                              </span>
                            </td>

                            <td>12/8/2021</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>

                    <div class="d-sm-flex justify-content-sm-between align-items-sm-center mt-4 mt-sm-3">
                      <p class="mb-0 text-center text-sm-start">
                        Showing 1 to 8 of 20 entries
                      </p>

                      <nav class="d-flex justify-content-center mb-0" 
                        aria-label="navigation">
                        <ul class="pagination pagination-sm pagination-primary-soft mb-0 pb-0">
                          <li class="page-item mb-0">
                            <a class="page-link" 
                              href="/" tabindex="-1">
                              <i class="fas fa-angle-left"></i>
                            </a>
                          </li>
                          <li class="page-item mb-0">
                            <a class="page-link" href="/">1</a>
                          </li>
                          <li class="page-item mb-0 active">
                            <a class="page-link" href="/">2</a>
                          </li>
                          <li class="page-item mb-0">
                            <a class="page-link" href="/">3</a>
                          </li>
                          <li class="page-item mb-0">
                            <a class="page-link" href="/">
                              <i class="fas fa-angle-right"></i>
                            </a>
                          </li>
                        </ul>
                      </nav>
                    </div>
                  </div>

                </div>

              </div>

            </div>
          </div>
        </section>

      </main>

    );
  };

export default Payouts;